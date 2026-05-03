@tool
extends Node2D

############################################################################################

const grid_spacing : float = 400.0;
const grid_gap : float = 10.0;
const grid_title_height : float = 50.0;
const grid_max : int = 0;
var grid_pos := Vector2i.ZERO;

############################################################################################

var processTime : float = 0.0;
func _physics_process(delta: float) -> void:
	processTime += delta;
	reset_grid();
	ImmediateGizmos2D.reset();
	
	ImmediateGizmos2D.draw_text("This is the example scene for ImmediateGizmos!\n\nThis scene showcases the numerous rendering methods found in ImmediateGizmos2D with some simple examples!", Vector2.UP * grid_gap, HORIZONTAL_ALIGNMENT_LEFT, VERTICAL_ALIGNMENT_BOTTOM, 80.0);
	
	line_strips(processTime);
	arcs_circles_capsules();
	rects_squares();
	rotations(processTime);

############################################################################################
# Example stuffs!

func line_strips(time : float) -> void:
	next_grid("Lines");
	
	var points : Array[Vector2] = [];
	var pointCount := 10;
	for i : int in pointCount:
		points.append(Vector2(i, sin(time + i)));
		
	grid_label("ImmediateGizmos2D.line", Rect2(-2, -2, 4, 4));
	ImmediateGizmos2D.line(-Vector2.ONE, Vector2.ONE);
	grid_label("ImmediateGizmos2D.line_strip", Rect2(0, -2, pointCount - 1, 4));
	ImmediateGizmos2D.line_strip(points);
	grid_label("ImmediateGizmos2D.line_polygon", Rect2(0, -2, pointCount - 1, 4));
	ImmediateGizmos2D.line_polygon(points);

func arcs_circles_capsules() -> void:
	next_grid("Curves");
	
	grid_label("ImmediateGizmos2D.line_arc", Rect2(-2, -2, 4, 4));
	ImmediateGizmos2D.line_arc(Vector2.ZERO, Vector2.LEFT, TAU * 0.5, Color.RED);
	grid_label("ImmediateGizmos2D.line_circle", Rect2(-2, -2, 4, 4));
	ImmediateGizmos2D.line_circle(Vector2.ZERO, 1.0, Color.GREEN);
	grid_label("ImmediateGizmos2D.line_capsule", Rect2(-2, -2, 4, 4));
	ImmediateGizmos2D.line_capsule(Vector2.ZERO, 0.8, 3, Color.BLUE);
	
func rects_squares() -> void:
	next_grid("Rects");
	grid_label("ImmediateGizmos2D.line_rect", Rect2(-3, -3, 6, 6));
	ImmediateGizmos2D.line_rect(Vector2.ZERO, Vector2(1.0, 2.0), Color.MAGENTA);
	grid_label("ImmediateGizmos2D.line_square", Rect2(-3, -3, 6, 6));
	ImmediateGizmos2D.line_square(Vector2.ZERO, 1.0, Color.YELLOW);
	
func rotations(time : float) -> void:
	next_grid("Rotations");
	
	grid_label("arc", Rect2(-2, -2, 4, 4), time);
	ImmediateGizmos2D.line_arc(Vector2.ZERO, Vector2.LEFT, TAU * 0.75, Color.CYAN);
	grid_label("square", Rect2(-3, -3, 6, 6), -time);
	ImmediateGizmos2D.line_square(Vector2.ZERO, 1.0, Color.ORANGE);
	
############################################################################################

#region Grid showcase functions.

func next_grid(title : String) -> void:
	if (grid_pos.y > -grid_max):
		grid_pos.x += 1;
	grid_pos.y = -grid_max;
	
	ImmediateGizmos2D.set_transform(Transform2D.IDENTITY);
	ImmediateGizmos2D.set_color(Color.WHITE);
	var topLeft := Vector2((grid_pos.x + 0.5) * (grid_spacing + grid_gap), grid_title_height / 2);
	ImmediateGizmos2D.draw_text(title, topLeft, HORIZONTAL_ALIGNMENT_CENTER, VERTICAL_ALIGNMENT_CENTER, grid_title_height / 2);

func reset_grid() -> void:
	grid_pos.x = 0;
	grid_pos.y = -grid_max;

func grid_label(text : String, area : Rect2, rot : float = 0.0) -> void:
	var topLeft := (grid_pos as Vector2) * (grid_spacing + grid_gap);
	topLeft.y += grid_title_height;
	var center := topLeft + (Vector2.ONE * 0.5 * (grid_spacing + grid_gap));
	
	ImmediateGizmos2D.set_transform(Transform2D.IDENTITY);
	ImmediateGizmos2D.set_color(Color.WHITE);
	ImmediateGizmos2D.line_square(center, (grid_spacing + (grid_gap * 0.7)) / 2, Color.BLACK);
	ImmediateGizmos2D.draw_text(text, Vector2(center.x, topLeft.y), HORIZONTAL_ALIGNMENT_CENTER, VERTICAL_ALIGNMENT_TOP, 15);
	
	set_grid_transform(grid_pos, area, rot);
	grid_pos.y += 1;

func set_grid_transform(pos : Vector2i, area : Rect2, rot : float) -> void:
	var gridPos := (pos as Vector2) * (grid_spacing + grid_gap);
	gridPos += Vector2.ONE * 0.5 * grid_gap;
	gridPos.y += grid_title_height;
	var gridScale := (Vector2.ONE * grid_spacing) / area.size;
	gridPos -= area.position * gridScale;
	
	ImmediateGizmos2D.set_transform(Transform2D(rot, gridScale, 0, gridPos));

#endregion
