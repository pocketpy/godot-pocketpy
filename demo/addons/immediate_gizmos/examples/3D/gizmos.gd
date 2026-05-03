@tool
extends Node3D

############################################################################################

const grid_spacing : float = 2.0;
const grid_gap : float = 0.1;
const grid_title_height : float = 0.5;
const grid_max : int = 4;
var grid_pos := Vector3i.ZERO;

############################################################################################

var processTime : float = 0.0;
func _physics_process(delta: float) -> void:
	processTime += delta;
	reset_grid();
	ImmediateGizmos3D.reset();
	
	ImmediateGizmos3D.draw_text("This is the example scene for ImmediateGizmos!\n\nThis scene showcases the numerous rendering methods found in ImmediateGizmos3D with some simple examples!", (Vector3.UP * (grid_spacing + grid_gap) * grid_max) + (Vector3.UP * (grid_gap + grid_title_height)), HORIZONTAL_ALIGNMENT_LEFT, VERTICAL_ALIGNMENT_BOTTOM, 0.8);
	
	line_strips(processTime);
	arcs_circles_spheres_capsules();
	cuboids_cubes();
	rotations(processTime);

############################################################################################
# Example stuffs!

func line_strips(time : float) -> void:
	next_grid("Lines");
	
	var points : Array[Vector3] = [];
	var pointCount := 10;
	for i : int in pointCount:
		points.append(Vector3(i, sin(time + i), cos(time + i)));
		
	grid_label("ImmediateGizmos3D.line", AABB(Vector3(-2, -2, -2), Vector3(4, 4, 4)));
	ImmediateGizmos3D.line(-Vector3.ONE, Vector3.ONE);
	grid_label("ImmediateGizmos3D.line_strip", AABB(Vector3(0, -2, -2), Vector3(pointCount - 1, 4, 4)));
	ImmediateGizmos3D.line_strip(points);
	grid_label("ImmediateGizmos3D.line_polygon", AABB(Vector3(0, -2, -2), Vector3(pointCount - 1, 4, 4)));
	ImmediateGizmos3D.line_polygon(points);
	
func arcs_circles_spheres_capsules():
	next_grid("Curves");
	
	grid_label("ImmediateGizmos3D.line_arc", AABB(Vector3.ONE * -2, Vector3.ONE * 4));
	ImmediateGizmos3D.line_arc(Vector3.ZERO, Vector3.FORWARD, Vector3.LEFT, TAU * 0.5, Color.RED);
	grid_label("ImmediateGizmos3D.line_circle", AABB(Vector3.ONE * -2, Vector3.ONE * 4));
	ImmediateGizmos3D.line_circle(Vector3.ZERO, Vector3.FORWARD, 1.0, Color.GREEN);
	grid_label("ImmediateGizmos3D.line_sphere", AABB(Vector3.ONE * -2, Vector3.ONE * 4));
	ImmediateGizmos3D.line_sphere(Vector3.ZERO, 1.0, Color.YELLOW);
	grid_label("ImmediateGizmos3D.line_capsule", AABB(Vector3.ONE * -2, Vector3.ONE * 4));
	ImmediateGizmos3D.line_capsule(Vector3.ZERO, 0.8, 3, Color.BLUE);
	
func cuboids_cubes():
	next_grid("Cuboids");

	grid_label("ImmediateGizmos3D.line_cuboid", AABB(Vector3.ONE * -3, Vector3.ONE * 6));
	ImmediateGizmos3D.line_cuboid(Vector3.ZERO, Vector3(1.0, 2.0, 1.0), Color.MAGENTA);
	grid_label("ImmediateGizmos3D.line_cube", AABB(Vector3.ONE * -3, Vector3.ONE * 6));
	ImmediateGizmos3D.line_cube(Vector3.ZERO, 1.0, Color.YELLOW);

func rotations(time : float) -> void:
	next_grid("Rotations");
	
	var rot := Vector3(time * 0.771, time * 0.345, time * 0.125);
	grid_label("arc", AABB(Vector3.ONE * -2, Vector3.ONE * 4), Basis.from_euler(Vector3(rot.x, rot.y, rot.z)));
	ImmediateGizmos3D.line_arc(Vector3.ZERO, Vector3.FORWARD, Vector3.LEFT, TAU * 0.5, Color.CYAN);
	grid_label("square", AABB(Vector3.ONE * -3, Vector3.ONE * 6), Basis.from_euler(Vector3(rot.y, rot.z, rot.x)));
	ImmediateGizmos3D.line_cube(Vector3.ZERO, 1.0, Color.ORANGE);
	grid_label("capsule", AABB(Vector3.ONE * -2, Vector3.ONE * 4), Basis.from_euler(Vector3(rot.z, rot.x, rot.y)));
	ImmediateGizmos3D.line_capsule(Vector3.ZERO, 0.8, 3, Color.RED);
	
############################################################################################

#region Grid showcase functions.

func next_grid(title : String) -> void:
	if (grid_pos.y > -grid_max):
		grid_pos.x += 1;
	grid_pos.y = -grid_max;
	
	ImmediateGizmos3D.set_transform(Transform2D.IDENTITY);
	ImmediateGizmos3D.set_color(Color.WHITE);
	var gridPos := (((grid_pos as Vector3) * Vector3(1.0, -1.0, 1.0)) + Vector3(0.5, 0.0, 0.5)) * (grid_spacing + grid_gap);
	ImmediateGizmos3D.draw_text(title, gridPos, HORIZONTAL_ALIGNMENT_CENTER, VERTICAL_ALIGNMENT_BOTTOM, grid_title_height / 2);

func reset_grid() -> void:
	grid_pos.x = 0;
	grid_pos.y = -grid_max;

func grid_label(text : String, area : AABB, rot : Basis = Basis.IDENTITY) -> void:
	var top := ((grid_pos as Vector3) * Vector3(1.0, -1.0, 1.0)) * (grid_spacing + grid_gap);
	var gridPos := (((grid_pos as Vector3) * Vector3(1.0, -1.0, 1.0)) + Vector3(0, -1, 0)) * (grid_spacing + grid_gap);
	var center := gridPos + (Vector3.ONE * 0.5 * (grid_spacing + grid_gap));
	
	ImmediateGizmos3D.set_transform(Transform3D.IDENTITY);
	ImmediateGizmos3D.set_color(Color.WHITE);
	ImmediateGizmos3D.line_cube(center, (grid_spacing + (grid_gap * 0.7)) / 2, Color.BLACK);
	ImmediateGizmos3D.draw_text(text, Vector3(center.x, top.y, center.z * 2), HORIZONTAL_ALIGNMENT_CENTER, VERTICAL_ALIGNMENT_TOP, 0.1);

	set_grid_transform(grid_pos, area, rot);
	grid_pos.y += 1;

func set_grid_transform(pos : Vector3i, area : AABB, rot : Basis) -> void:
	var gridPos := (((pos as Vector3) * Vector3(1.0, -1.0, 1.0)) + Vector3(0, -1, 0)) * (grid_spacing + grid_gap);
	gridPos += Vector3.ONE * 0.5 * grid_gap;
	var gridScale := (Vector3.ONE * grid_spacing) / area.size;
	gridPos -= area.position * gridScale;
	
	var gridTransform := Transform3D(rot, Vector3.ZERO);
	gridTransform = gridTransform.scaled(gridScale);
	gridTransform = gridTransform.translated(gridPos);
	ImmediateGizmos3D.set_transform(gridTransform);
	

#endregion
