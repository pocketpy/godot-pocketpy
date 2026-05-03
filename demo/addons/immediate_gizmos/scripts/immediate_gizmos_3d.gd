@tool
extends Node
class_name ImmediateGizmos3D

##########################################################################

static func set_color(color : Color): 
	EditorImmediateGizmos.draw_color = color;
static func set_transform(transform : Transform3D): 
	EditorImmediateGizmos.draw_3d_transform = transform;
static func set_required_selection(node : Node): 
	EditorImmediateGizmos.draw_required_selection = node;
static func set_font(font : Font): 
	EditorImmediateGizmos.draw_font = font;
static func set_font_size(fontSize : int): 
	EditorImmediateGizmos.draw_font_size = fontSize;
static func reset(): 
	EditorImmediateGizmos.reset();
	
##########################################################################

static func line(from : Vector3, to : Vector3, color : Color = EditorImmediateGizmos.gizmo_default_color) -> void:
	EditorImmediateGizmos.draw_line_3d(from, to);
	EditorImmediateGizmos.end_draw_3d(color);
	
static func line_strip(points : Array[Vector3], color : Color = EditorImmediateGizmos.gizmo_default_color) -> void:
	EditorImmediateGizmos.points_3d.append_array(points);
	EditorImmediateGizmos.end_draw_3d(color);
	
static func line_polygon(points : Array[Vector3], color : Color = EditorImmediateGizmos.gizmo_default_color) -> void:
	EditorImmediateGizmos.points_3d.append_array(points);
	if (points.size() <= 0): return;
	EditorImmediateGizmos.draw_point_3d(points[0])
	EditorImmediateGizmos.end_draw_3d(color);
	
static func line_arc(center : Vector3, axis : Vector3, startPoint : Vector3, radians : float, color : Color = EditorImmediateGizmos.gizmo_default_color) -> void:
	EditorImmediateGizmos.draw_arc_3d(center, axis, startPoint, radians);
	EditorImmediateGizmos.end_draw_3d(color);

static func line_circle(center : Vector3, axis : Vector3, radius : float, color : Color = EditorImmediateGizmos.gizmo_default_color) -> void:
	var against := Vector3.RIGHT if axis.is_equal_approx(Vector3.UP) else Vector3.UP;
	var startDirection := axis.cross(against).normalized();
	EditorImmediateGizmos.draw_arc_3d(center, axis, startDirection * radius, TAU);
	EditorImmediateGizmos.end_draw_3d(color);

static func line_sphere(center : Vector3, radius : float, color : Color = EditorImmediateGizmos.gizmo_default_color) -> void:
	EditorImmediateGizmos.draw_arc_3d(center, Vector3.RIGHT, Vector3.UP * radius, TAU);
	EditorImmediateGizmos.draw_arc_3d(center, Vector3.FORWARD, Vector3.UP * radius, TAU * 0.25);
	EditorImmediateGizmos.draw_arc_3d(center, Vector3.UP, Vector3.RIGHT * radius, TAU);
	EditorImmediateGizmos.draw_arc_3d(center, Vector3.FORWARD, Vector3.RIGHT * radius, TAU * 0.75);
	EditorImmediateGizmos.end_draw_3d(color);
	
static func line_capsule(center : Vector3, radius : float, height : float, color : Color = EditorImmediateGizmos.gizmo_default_color) -> void:
	height -= radius * 2;
	if (height < 0):
		return line_sphere(center, radius, color);
	
	var topCenter := center + Vector3(0.0, height * 0.5, 0.0);
	var bottomCenter := center - Vector3(0.0, height * 0.5, 0.0);
	
	var north := Vector3.FORWARD * radius;
	var east := Vector3.RIGHT * radius;
	var south := Vector3.BACK * radius;
	var west := Vector3.LEFT * radius;
	
	# Zero overlaps, super cool!
	EditorImmediateGizmos.draw_arc_3d(topCenter, Vector3.RIGHT, north, PI);
	EditorImmediateGizmos.draw_arc_3d(bottomCenter, Vector3.RIGHT, south, PI);
	EditorImmediateGizmos.draw_arc_3d(topCenter, Vector3.UP, north, TAU * 0.25);
	EditorImmediateGizmos.draw_arc_3d(topCenter, Vector3.FORWARD, west, PI);
	EditorImmediateGizmos.draw_arc_3d(bottomCenter, Vector3.FORWARD, east, PI);
	EditorImmediateGizmos.draw_arc_3d(bottomCenter, Vector3.UP, west, TAU);
	EditorImmediateGizmos.draw_arc_3d(topCenter, Vector3.UP, west, TAU * 0.75);
	EditorImmediateGizmos.end_draw_3d(color);
	
static func line_cuboid(center : Vector3, radius : Vector3, color : Color = EditorImmediateGizmos.gizmo_default_color) -> void:
	var tlb := center + (Vector3(1, 1, -1) * radius);
	var tlf := center + (Vector3(1, 1, 1) * radius);
	var trb := center + (Vector3(-1, 1, -1) * radius);
	var trf := center + (Vector3(-1, 1, 1) * radius);
	var blb := center + (Vector3(1, -1, -1) * radius);
	var blf := center + (Vector3(1, -1, 1) * radius);
	var brb := center + (Vector3(-1, -1, -1) * radius);
	var brf := center + (Vector3(-1, -1, 1) * radius);
	
	# 3 Overlaps. Argh.
	EditorImmediateGizmos.draw_line_3d(tlb, tlf);
	EditorImmediateGizmos.draw_line_3d(blf, blb);
	EditorImmediateGizmos.draw_line_3d(tlb, trb);
	EditorImmediateGizmos.draw_point_3d(trf);
	EditorImmediateGizmos.draw_point_3d(tlf);
	EditorImmediateGizmos.draw_line_3d(trf, brf);
	EditorImmediateGizmos.draw_point_3d(blf);
	EditorImmediateGizmos.draw_line_3d(brf, brb);
	EditorImmediateGizmos.draw_point_3d(blb);
	EditorImmediateGizmos.draw_line_3d(brb, trb);
	EditorImmediateGizmos.end_draw_3d(color);
	
static func line_cube(center : Vector3, radius : float, color : Color = EditorImmediateGizmos.gizmo_default_color) -> void:
	line_cuboid(center, Vector3.ONE * radius, color);

##########################################################################

static func draw_text(text : String, position : Vector3, hAlign : HorizontalAlignment = HORIZONTAL_ALIGNMENT_LEFT, vAlign : VerticalAlignment = VERTICAL_ALIGNMENT_BOTTOM, height : float = 0.25):
	EditorImmediateGizmos.draw_text_3d(text, position, hAlign, vAlign, height);

##########################################################################
