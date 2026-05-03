@tool
extends Node
class_name ImmediateGizmos2D

##########################################################################

static func set_color(color : Color): 
	EditorImmediateGizmos.draw_color = color;
static func set_transform(transform : Transform2D): 
	EditorImmediateGizmos.draw_2d_transform = transform;
static func set_required_selection(node : Node): 
	EditorImmediateGizmos.draw_required_selection = node;
static func set_font(font : Font): 
	EditorImmediateGizmos.draw_font = font;
static func set_font_size(fontSize : int): 
	EditorImmediateGizmos.draw_font_size = fontSize;
static func reset(): 
	EditorImmediateGizmos.reset();
	
##########################################################################

static func line(from : Vector2, to : Vector2, color : Color = EditorImmediateGizmos.gizmo_default_color) -> void:
	EditorImmediateGizmos.draw_line_2d(from, to);
	EditorImmediateGizmos.end_draw_2d(color);
	
static func line_strip(points : Array[Vector2], color : Color = EditorImmediateGizmos.gizmo_default_color) -> void:
	EditorImmediateGizmos.points_2d.append_array(points);
	EditorImmediateGizmos.end_draw_2d(color);
	
static func line_polygon(points : Array[Vector2], color : Color = EditorImmediateGizmos.gizmo_default_color) -> void:
	EditorImmediateGizmos.points_2d.append_array(points);
	if (points.size() <= 0): return;
	EditorImmediateGizmos.draw_point_2d(points[0])
	EditorImmediateGizmos.end_draw_2d(color);
	
static func line_arc(center : Vector2, startPoint : Vector2, radians : float, color : Color = EditorImmediateGizmos.gizmo_default_color) -> void:
	EditorImmediateGizmos.draw_arc_2d(center, startPoint, radians);
	EditorImmediateGizmos.end_draw_2d(color);

static func line_circle(center : Vector2, radius : float, color : Color = EditorImmediateGizmos.gizmo_default_color) -> void:
	EditorImmediateGizmos.draw_arc_2d(center, Vector2.UP * radius, TAU);
	EditorImmediateGizmos.end_draw_2d(color);
	
static func line_capsule(center : Vector2, radius : float, height : float, color : Color = EditorImmediateGizmos.gizmo_default_color) -> void:
	height -= radius * 2;
	if (height < 0):
		return line_circle(center, radius, color);
	
	var topCenter := center + Vector2(0.0, height * 0.5);
	var bottomCenter := center - Vector2(0.0, height * 0.5);
	
	var east := Vector2.RIGHT * radius;
	var west := Vector2.LEFT * radius;
	
	# Zero overlaps, super cool!
	EditorImmediateGizmos.draw_arc_2d(topCenter, east, PI);
	EditorImmediateGizmos.draw_arc_2d(bottomCenter, west, PI);
	EditorImmediateGizmos.draw_point_2d(topCenter + east);
	EditorImmediateGizmos.end_draw_2d(color);
	
static func line_rect(center : Vector2, size : Vector2, color : Color = EditorImmediateGizmos.gizmo_default_color) -> void:
	var tl := center + (Vector2(-1, -1) * size);
	var tr := center + (Vector2(1, -1) * size);
	var bl := center + (Vector2(-1, 1) * size);
	var br := center + (Vector2(1, 1) * size);
	
	# 3 Overlaps. Argh.
	EditorImmediateGizmos.draw_line_2d(tl, tr);
	EditorImmediateGizmos.draw_line_2d(br, bl);
	EditorImmediateGizmos.draw_point_2d(tl);
	EditorImmediateGizmos.end_draw_2d(color);
	
static func line_square(center : Vector2, size : float, color : Color = EditorImmediateGizmos.gizmo_default_color) -> void:
	line_rect(center, Vector2.ONE * size, color);

##########################################################################

static func draw_text(text : String, position : Vector2, hAlign : HorizontalAlignment = HORIZONTAL_ALIGNMENT_LEFT, vAlign : VerticalAlignment = VERTICAL_ALIGNMENT_BOTTOM, height : float = 0.25):
	EditorImmediateGizmos.draw_text_2d(text, position, hAlign, vAlign, height);

##########################################################################
