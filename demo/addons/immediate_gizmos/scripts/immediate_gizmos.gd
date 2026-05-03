@tool
extends Node
class_name EditorImmediateGizmos;

##########################################################################

const target_process_priority = -999;
const __expected_id : int = 0x1eaf1e55;
@onready var __id := __expected_id;

##########################################################################

static var gizmo_root : EditorImmediateGizmos = null;
static var gizmo_material_line_2d : ShaderMaterial = preload("res://addons/immediate_gizmos/materials/immediate_gizmos_line_2d.tres");
static var gizmo_material_line_3d : ShaderMaterial = preload("res://addons/immediate_gizmos/materials/immediate_gizmos_line_3d.tres");
static var gizmo_material_text_2d : ShaderMaterial = preload("res://addons/immediate_gizmos/materials/immediate_gizmos_text_2d.tres")
static var gizmo_material_text_3d : ShaderMaterial = preload("res://addons/immediate_gizmos/materials/immediate_gizmos_text_3d.tres")
const gizmo_default_color := Color.TRANSPARENT; # Key
const gizmo_text_viewport_size := Vector2i(4096, 4096); # Key

static var draw_color : Color = Color.WHITE;
static var draw_2d_transform : Transform2D = Transform2D.IDENTITY;
static var draw_3d_transform : Transform3D = Transform3D.IDENTITY;
static var draw_font : Font = ThemeDB.fallback_font;
static var draw_font_size : int = 20;
static var draw_font_max_width : int = 512;
static var draw_required_selection : Node = null;

static func is_required_selection_met() -> bool:
	if (draw_required_selection == null): 
		return true;
	if (!Engine.is_editor_hint()):
		return false;
	
	var sceneRoot := get_scene_root();
	var selected := draw_required_selection;
	
	var editorInterface := Engine.get_singleton("EditorInterface");
	while (editorInterface != null && selected != sceneRoot):
		if (editorInterface.get_selection().get_selected_nodes().has(selected)):
			return true;
		selected = selected.get_parent();
	return false;	

static func _get_color(color : Color) -> Color:
	if (color == EditorImmediateGizmos.gizmo_default_color):
		return EditorImmediateGizmos.draw_color;
	return color
	
static func reset() -> void:
	draw_color = Color.WHITE;
	draw_2d_transform = Transform2D.IDENTITY;
	draw_3d_transform = Transform3D.IDENTITY;
	draw_font = ThemeDB.fallback_font;
	draw_font_size = 20;
	draw_font_max_width = 512;
	draw_required_selection = null;
	
##########################################################################

@abstract class RenderBlock:
	var mesh_instances : Array[Node] = []
	var meshes : Array[ImmediateMesh] = []
	var instance_counter : int = 0;
	var is_3d : bool;
	var material : ShaderMaterial;
	var duplicate_material : bool;
	
	func _init(is3d : bool, _material : ShaderMaterial, duplicateMaterial : bool) -> void:
		is_3d = is3d;
		material = _material;
		duplicate_material = duplicateMaterial;
	
	func _add_instance() -> void:
		var meshInstance : Node = null;
		var mesh : ImmediateMesh = ImmediateMesh.new();
		var mat := material.duplicate() if (duplicate_material) else material;
		
		if (is_3d):
			meshInstance = MeshInstance3D.new();
			meshInstance.mesh = mesh;
			meshInstance.material_override = mat;
		else:
			meshInstance = MeshInstance2D.new();
			meshInstance.mesh = mesh;
			meshInstance.top_level = true;
			meshInstance.material = mat;
		
		meshes.append(mesh);
		mesh_instances.append(meshInstance);
		EditorImmediateGizmos.get_root().add_child(meshInstance);

	func _is_usable_mesh(index : int) -> bool:
		assert(0 <= index &&  index < meshes.size()); 
		return meshes[index].get_surface_count() < RenderingServer.MAX_MESH_SURFACES;
			
	func _get_usable_mesh() -> ImmediateMesh:
		var index : int = instance_counter;
		while (index < meshes.size()):
			if (_is_usable_mesh(index)):
				return meshes[index];
			index += 1;
		_add_instance();
		instance_counter = meshes.size() - 1;
		return meshes[index];

	func clear() -> void:
		for mesh : ImmediateMesh in meshes:
			mesh.clear_surfaces()
		instance_counter = 0;

class LineRenderBlock:
	extends RenderBlock;
	
	func _init(is3d : bool):
		if (!is3d):
			super(false, EditorImmediateGizmos.gizmo_material_line_2d, false);
		else:
			super(true, EditorImmediateGizmos.gizmo_material_line_3d, false);
	
	func draw_line_2d(points : Array[Vector2], color : Color) -> void:
		var mesh := _get_usable_mesh();
		mesh.surface_begin(Mesh.PRIMITIVE_LINE_STRIP);
		mesh.surface_set_color(EditorImmediateGizmos._get_color(color));
		for point : Vector2 in points:
			mesh.surface_add_vertex_2d(EditorImmediateGizmos.draw_2d_transform * point);
		mesh.surface_end();
	
	func draw_line_3d(points : Array[Vector3], color : Color) -> void:
		var mesh := _get_usable_mesh();
		mesh.surface_begin(Mesh.PRIMITIVE_LINE_STRIP);
		mesh.surface_set_color(EditorImmediateGizmos._get_color(color));
		for point : Vector3 in points:
			mesh.surface_add_vertex(EditorImmediateGizmos.draw_3d_transform * point);
		mesh.surface_end();

class TextRenderBlock:
	extends RenderBlock;
	
	var textAtlases : Array[TextAtlas] = [];
	
	func _init(is3d : bool):
		if (!is3d):
			super(false, EditorImmediateGizmos.gizmo_material_text_2d, true);
		else:
			super(true, EditorImmediateGizmos.gizmo_material_text_3d, true);
	
	func _add_text_atlas() -> void:
		var subViewport := SubViewport.new();
		subViewport.size = Vector2i(gizmo_text_viewport_size.x, gizmo_text_viewport_size.y);
		subViewport.transparent_bg = true;
		var textAtlas = TextAtlas.new(subViewport);
		textAtlases.append(textAtlas);
		subViewport.add_child(textAtlas);
		EditorImmediateGizmos.get_root().add_child(subViewport);
	
	func draw_text_atlas(text : String, font : Font, fontSize : int) -> AtlasDrawInfo:
		for textAtlas : TextAtlas in textAtlases:
			var rect := textAtlas.draw_text(text, font, fontSize);
			if (rect.position.x < 0 || rect.position.y < 0):
				return null;
			if (rect.has_area()):
				return AtlasDrawInfo.new(textAtlas.get_uv(rect), textAtlas);
		_add_text_atlas();
		var newTextAtlas := textAtlases[textAtlases.size() - 1];
		var newRect := newTextAtlas.draw_text(text, font, fontSize);
		if (newRect.has_area()):
			return AtlasDrawInfo.new(newTextAtlas.get_uv(newRect), newTextAtlas);
		return null;
		
	class AtlasDrawInfo:
		var uv_rect : Rect2;
		var atlas : TextAtlas;
		func _init(uvRect : Rect2, _atlas : TextAtlas) -> void:
			uv_rect = uvRect;
			atlas = _atlas;
	
	func _get_atlas_mesh(atlas : TextAtlas) -> ImmediateMesh:
		for meshIndex : int in atlas.meshes.size():
			if (_is_usable_mesh(atlas.meshes[meshIndex])):
				return meshes[atlas.meshes[meshIndex]];
		_add_instance();
		var newIndex : int = mesh_instances.size() - 1;
		var material : ShaderMaterial = (mesh_instances[newIndex] as MeshInstance2D).material if (!is_3d) else (mesh_instances[newIndex] as MeshInstance3D).material_override;
		material.set_shader_parameter("textAtlas", atlas.viewport.get_texture());
		atlas.meshes.append(newIndex);
		return meshes[newIndex];

	func draw_text_2d(text : String, position : Vector2, hAlign : HorizontalAlignment, vAlign : VerticalAlignment, height : float) -> void:
		var drawInfo := draw_text_atlas(text, EditorImmediateGizmos.draw_font, EditorImmediateGizmos.draw_font_size);
		if (drawInfo == null): return;
		var mesh := _get_atlas_mesh(drawInfo.atlas);;
		if (mesh == null): return;
		
		var uv_tl := drawInfo.uv_rect.position;
		var uv_br := uv_tl + drawInfo.uv_rect.size;
		var uv_bl := Vector2(uv_tl.x, uv_br.y);
		var uv_tr := Vector2(uv_br.x, uv_tl.y);
		
		var v_bl := Vector2(0.0, 0.0);
		var v_tr := Vector2(drawInfo.uv_rect.size.x / drawInfo.uv_rect.size.y, -1.0) * height;
		var offset := position;	
		match (hAlign):
			HORIZONTAL_ALIGNMENT_CENTER:
				offset.x -= v_tr.x * 0.5;
			HORIZONTAL_ALIGNMENT_RIGHT:
				offset.x -= v_tr.x;
		match (vAlign):
			VERTICAL_ALIGNMENT_CENTER:
				offset.y -= v_tr.y * 0.5;
			VERTICAL_ALIGNMENT_TOP:
				offset.y -= v_tr.y;
		v_bl += offset;
		v_tr += offset;
		var v_tl := Vector2(v_bl.x, v_tr.y);
		var v_br := Vector2(v_tr.x, v_bl.y);
		
		v_bl = EditorImmediateGizmos.draw_2d_transform * v_bl;
		v_tr = EditorImmediateGizmos.draw_2d_transform * v_tr;
		v_tl = EditorImmediateGizmos.draw_2d_transform * v_tl;
		v_br = EditorImmediateGizmos.draw_2d_transform * v_br;
		
		mesh.surface_begin(Mesh.PRIMITIVE_TRIANGLES);
		mesh.surface_set_color(EditorImmediateGizmos.draw_color);
		#
		mesh.surface_set_uv(uv_bl);
		mesh.surface_add_vertex_2d(v_bl);
		mesh.surface_set_uv(uv_tl);
		mesh.surface_add_vertex_2d(v_tl);
		mesh.surface_set_uv(uv_br);
		mesh.surface_add_vertex_2d(v_br);
		#
		mesh.surface_set_uv(uv_tl);
		mesh.surface_add_vertex_2d(v_tl);
		mesh.surface_set_uv(uv_tr);
		mesh.surface_add_vertex_2d(v_tr);
		mesh.surface_set_uv(uv_br);
		mesh.surface_add_vertex_2d(v_br);
		#
		mesh.surface_end();

	func draw_text_3d(text : String, position : Vector3, hAlign : HorizontalAlignment, vAlign : VerticalAlignment, height : float) -> void:
		var drawInfo := draw_text_atlas(text, EditorImmediateGizmos.draw_font, EditorImmediateGizmos.draw_font_size);
		if (drawInfo == null): return;
		var mesh := _get_atlas_mesh(drawInfo.atlas);;
		if (mesh == null): return;
		
		var uv_tl := drawInfo.uv_rect.position;
		var uv_br := uv_tl + drawInfo.uv_rect.size;
		var uv_bl := Vector2(uv_tl.x, uv_br.y);
		var uv_tr := Vector2(uv_br.x, uv_tl.y);
		
		var v_bl := Vector3(0.0, 0.0, 0.0);
		var v_tr := Vector3(drawInfo.uv_rect.size.x / drawInfo.uv_rect.size.y, 1.0, 0.0) * height;
		var offset := position;	
		match (hAlign):
			HORIZONTAL_ALIGNMENT_CENTER:
				offset.x -= v_tr.x * 0.5;
			HORIZONTAL_ALIGNMENT_RIGHT:
				offset.x -= v_tr.x;
		match (vAlign):
			VERTICAL_ALIGNMENT_CENTER:
				offset.y -= v_tr.y * 0.5;
			VERTICAL_ALIGNMENT_TOP:
				offset.y -= v_tr.y;
		v_bl += offset;
		v_tr += offset;
		var v_tl := Vector3(v_bl.x, v_tr.y, position.z);
		var v_br := Vector3(v_tr.x, v_bl.y, position.z);
		
		v_bl = EditorImmediateGizmos.draw_3d_transform * v_bl;
		v_tr = EditorImmediateGizmos.draw_3d_transform * v_tr;
		v_tl = EditorImmediateGizmos.draw_3d_transform * v_tl;
		v_br = EditorImmediateGizmos.draw_3d_transform * v_br;
		
		mesh.surface_begin(Mesh.PRIMITIVE_TRIANGLES);
		mesh.surface_set_color(EditorImmediateGizmos.draw_color);
		#
		mesh.surface_set_uv(uv_bl);
		mesh.surface_add_vertex(v_bl);
		mesh.surface_set_uv(uv_tl);
		mesh.surface_add_vertex(v_tl);
		mesh.surface_set_uv(uv_br);
		mesh.surface_add_vertex(v_br);
		#
		mesh.surface_set_uv(uv_tl);
		mesh.surface_add_vertex(v_tl);
		mesh.surface_set_uv(uv_tr);
		mesh.surface_add_vertex(v_tr);
		mesh.surface_set_uv(uv_br);
		mesh.surface_add_vertex(v_br);
		#
		mesh.surface_set_uv(uv_br);
		mesh.surface_add_vertex(v_bl);
		mesh.surface_set_uv(uv_bl);
		mesh.surface_add_vertex(v_br);
		mesh.surface_set_uv(uv_tr);
		mesh.surface_add_vertex(v_tl);
		#
		mesh.surface_set_uv(uv_tr);
		mesh.surface_add_vertex(v_tl);
		mesh.surface_set_uv(uv_bl);
		mesh.surface_add_vertex(v_br);
		mesh.surface_set_uv(uv_tl);
		mesh.surface_add_vertex(v_tr);
		mesh.surface_end();

	func clear() -> void:
		super();
		for textAtlas : TextAtlas in textAtlases:
			textAtlas.clear();

	class TextAtlas:
		extends Node2D;
		
		var viewport : Viewport = null;
		var region : Rect2i;
		#
		var meshes : Array[int] = [];
		var bin_strings : Array[BinStrings] = [];
		var bin_xs : Array[int] = [ 0 ];
		var bin_ys : Array[int] = [ 0 ];
		
		class BinStrings:
			var rect : Rect2i;
			var text : String;
			var font : Font;
			var font_size : int;
			var max_width : int;
			
			func _init(_rect : Rect2i, _text : String, _font : Font, fontSize : int, maxWidth : int) -> void:
				rect = _rect;
				text = _text;
				font = _font;
				font_size = fontSize;
				max_width = maxWidth;
		
		func _init(_viewport : SubViewport) -> void:
			viewport = _viewport;
			region = Rect2i(Vector2i.ZERO, viewport.size);
			
		func draw_text(text : String, font : Font, fontSize : int) -> Rect2i:
			var maxWidth := mini(region.size.x, EditorImmediateGizmos.draw_font_max_width);
			var sizei := Vector2i(font.get_multiline_string_size(text, HORIZONTAL_ALIGNMENT_LEFT, maxWidth, fontSize).ceil());
			var ascent := font.get_ascent(fontSize);
			
			var xIndex = 0;
			var yIndex = 0;
			var rect : Rect2i = Rect2i(Vector2i.ZERO, sizei);
			if (!region.encloses(rect)): 
				return Rect2i(-Vector2i.ONE, Vector2.ZERO);
				
			var overlapping : bool = true;
			while (overlapping && yIndex < bin_ys.size()): 
				overlapping = false;
				for bin : BinStrings in bin_strings:
					if (rect.intersects(bin.rect)):
						overlapping = true;
						break;
				if (!overlapping):
					break;
				xIndex += 1;
				if (xIndex < bin_xs.size()):
					rect.position.x = bin_xs[xIndex];
					if ((rect.position.x + rect.size.x) <= (region.position.x + region.size.x)):
						continue;
				xIndex = 0;
				yIndex += 1;
				rect.position.x = bin_xs[xIndex];
				rect.position.y = bin_ys[yIndex];
			
			if (!region.encloses(rect)): 
				return Rect2i();

			for x in [ rect.position.x + rect.size.x ]:
				var index := bin_xs.bsearch(x);
				if (index < bin_xs.size() && bin_xs[index] == x):
					continue;
				bin_xs.insert(index, x);
			for y in [ rect.position.y + rect.size.y ]:
				var index := bin_ys.bsearch(y);
				if (index < bin_ys.size() && bin_ys[index] == y):
					continue;
				bin_ys.insert(index, y);
			bin_strings.append(BinStrings.new(rect, text, font, fontSize, maxWidth));
			queue_redraw();
			return rect;
		
		func _draw() -> void:
			for binString : BinStrings in bin_strings:
				var ascent := binString.font.get_ascent(binString.font_size);
				draw_multiline_string(binString.font, Vector2(binString.rect.position) + (Vector2.DOWN * ascent), binString.text, HORIZONTAL_ALIGNMENT_LEFT, binString.max_width, binString.font_size);
		
		func get_uv(rect : Rect2i) -> Rect2:
			return Rect2(
				Vector2(rect.position) / Vector2(region.size),
				Vector2(rect.size) / Vector2(region.size)
			);
		
		func clear() -> void:
			bin_xs = [0];
			bin_ys = [0];
			bin_strings.clear();

##########################################################################

enum RenderMode {
	Gizmos_Line_2D,
	Gizmos_Line_3D,
	Gizmos_Text_2D,
	Gizmos_Text_3D,
}

class RenderSelector:
	var process_block : Array[RenderBlock] = [ null, null ];
	var render_mode : RenderMode;
	
	func _init(renderMode : RenderMode) -> void:
		render_mode = renderMode;
		
	func _create_process_block() -> RenderBlock:
		match (render_mode):
			RenderMode.Gizmos_Line_2D, RenderMode.Gizmos_Line_3D: 
				return LineRenderBlock.new(render_mode == RenderMode.Gizmos_Line_3D);
			RenderMode.Gizmos_Text_2D, RenderMode.Gizmos_Text_3D: 
				return TextRenderBlock.new(render_mode == RenderMode.Gizmos_Text_3D);
			_: push_error("Unsupported ImmediateGizmos RenderMode");
		return null;
	
	func _get_block_index() -> int:
		return 1 if (Engine.is_in_physics_frame()) else 0;
		
	func get_render_block() -> RenderBlock:
		var index := _get_block_index();
		if (process_block[index] == null):
			process_block[index] = _create_process_block();
		return process_block[index];
	
	func clear() -> void:
		var index := _get_block_index();
		if (process_block[index] != null):
			process_block[index].clear();

static var render_selectors : Dictionary = {};
static func get_render_selector(renderMode : RenderMode) -> RenderSelector:
	if (render_selectors.has(renderMode)):
		return render_selectors.get(renderMode);
	var renderSelector : RenderSelector = RenderSelector.new(renderMode);
	render_selectors.set(renderMode, renderSelector);
	return renderSelector;

static func get_render_block(renderMode : RenderMode) -> RenderBlock:
	return get_render_selector(renderMode).get_render_block();

##########################################################################

static func get_scene_root() -> Node:
	if (Engine.is_editor_hint()):
		var editorInterface := Engine.get_singleton("EditorInterface");
		assert(editorInterface != null);
		return editorInterface.get_edited_scene_root().get_parent();

	assert(ProjectSettings.get_setting("application/run/main_loop_type") == "SceneTree", "To use ImmediateGizmos, the project main loop must be of type 'SceneTree'");
	return (Engine.get_main_loop() as SceneTree).root;
		
static func get_root() -> EditorImmediateGizmos:
	if (gizmo_root != null): 
		return gizmo_root;

	# Get root.
	var sceneRoot : Node = get_scene_root();

	var rootCounter = 1;
	var rootName := "ImmediateGizmos";
	var rootNode := sceneRoot.find_child(rootName, false, false);
	while (rootNode != null):
		if (rootNode.get("__id") == __expected_id):
			# Claim back root??
			gizmo_root = rootNode;
			return gizmo_root;
		
		# Ignore same named node.
		rootCounter += 1;
		rootName = "ImmediateGizmos%d" % rootCounter;
		rootNode = sceneRoot.find_child(rootName, false, false);
	
	# Create root.
	gizmo_root = EditorImmediateGizmos.new();
	gizmo_root.name = rootName;
	sceneRoot.add_child(gizmo_root);
	
	return gizmo_root;

##########################################################################

static var points_2d : Array[Vector2] = [];
static func draw_point_2d(point : Vector2) -> void:
	points_2d.append(point);

static func draw_line_2d(from : Vector2, to : Vector2) -> void:
	draw_point_2d(from);
	draw_point_2d(to);

static func draw_arc_2d(center : Vector2, startPoint : Vector2, radians : float) -> void:
	radians = clampf(radians, 0.0, TAU);
	if (radians <= 0.0):
		return;

	var detail := ceilf((radians / TAU) * 32.0);
	var increment = radians / (detail as float);

	for i : int in range(detail + 1):
		var pos = startPoint.rotated((i as float) * increment);
		draw_point_2d(center + pos);

static func end_draw_2d(color : Color) -> void:
	if (points_2d.size() > 0 && is_required_selection_met()): 
		var renderBlock := EditorImmediateGizmos.get_render_block(RenderMode.Gizmos_Line_2D) as LineRenderBlock;
		if (renderBlock != null):
			renderBlock.draw_line_2d(points_2d, color)
	points_2d.clear();

##########################################################################

static var points_3d : Array[Vector3] = [];
static func draw_point_3d(point : Vector3) -> void:
	points_3d.append(point);

static func draw_line_3d(from : Vector3, to : Vector3) -> void:
	draw_point_3d(from);
	draw_point_3d(to);

static func draw_arc_3d(center : Vector3, axis : Vector3, startPoint : Vector3, radians : float) -> void:
	radians = clampf(radians, 0.0, TAU);
	if (radians <= 0.0):
		return;

	var detail := ceilf((radians / TAU) * 32.0);
	var increment = radians / (detail as float);

	for i : int in range(detail + 1):
		var pos = startPoint.rotated(axis, (i as float) * increment);
		draw_point_3d(center + pos);

static func end_draw_3d(color : Color) -> void:
	if (points_3d.size() > 0 && is_required_selection_met()): 
		var renderBlock := EditorImmediateGizmos.get_render_block(RenderMode.Gizmos_Line_3D) as LineRenderBlock;
		if (renderBlock != null):
			renderBlock.draw_line_3d(points_3d, color)
	points_3d.clear();

##########################################################################

static func draw_text_2d(text : String, position : Vector2, hAlign : HorizontalAlignment = HORIZONTAL_ALIGNMENT_LEFT, vAlign : VerticalAlignment = VERTICAL_ALIGNMENT_BOTTOM, height : float = 0.25) -> void:
	var renderBlock := EditorImmediateGizmos.get_render_block(RenderMode.Gizmos_Text_2D) as TextRenderBlock;
	if (is_required_selection_met() && renderBlock != null):
		renderBlock.draw_text_2d(text, position, hAlign, vAlign, height);
		
static func draw_text_3d(text : String, position : Vector3, hAlign : HorizontalAlignment = HORIZONTAL_ALIGNMENT_LEFT, vAlign : VerticalAlignment = VERTICAL_ALIGNMENT_BOTTOM, height : float = 0.25) -> void:
	var renderBlock := EditorImmediateGizmos.get_render_block(RenderMode.Gizmos_Text_3D) as TextRenderBlock;
	if (is_required_selection_met() && renderBlock != null):
		renderBlock.draw_text_3d(text, position, hAlign, vAlign, height);
	
##########################################################################

func _ready() -> void:
	process_priority = target_process_priority;
	process_physics_priority = target_process_priority;
	set_process(true);
	set_physics_process(true);

func _process(_delta: float) -> void:
	for key : RenderMode in render_selectors:
		render_selectors.get(key).clear();
	reset();

func _physics_process(_delta: float) -> void:
	for key : RenderMode in render_selectors:
		render_selectors.get(key).clear();
	reset();

##########################################################################
