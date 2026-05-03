@tool
extends Node2D

const size : float = 320.0;

func _physics_process(delta: float) -> void:
	ImmediateGizmos2D.reset();
	ImmediateGizmos2D.set_required_selection(self);
	
	ImmediateGizmos2D.set_transform(transform);
	ImmediateGizmos2D.draw_text(
		"This has been selected!", 		# Text
		Vector2.UP * size, 				# Position
		HORIZONTAL_ALIGNMENT_CENTER, 	# Horizontal Alignment
		VERTICAL_ALIGNMENT_BOTTOM, 		# Vertical Alignment
		50 								# Size
	);
	
	var colors := [ Color.MEDIUM_PURPLE, Color.MEDIUM_BLUE, Color.MEDIUM_TURQUOISE ];
	for i : int in colors.size():
		ImmediateGizmos2D.set_transform(transform * Transform2D(deg_to_rad(i * 30), Vector2.ZERO));
		ImmediateGizmos2D.line_square(Vector2.ZERO, size * pow(0.8, i), colors[i]);
	
