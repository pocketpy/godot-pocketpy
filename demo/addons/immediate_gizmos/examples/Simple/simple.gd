@tool
extends Node3D

############################################################################################
#
# This file is intented to be changed based on the users experimental needs!
#
# 	Any changes to the code below this block, such as variables or draw calls,
# should show their effects immediately in the editor as well as in-game. 
# 
############################################################################################

func _process(delta: float) -> void:
	# It's best to reset before use!
	ImmediateGizmos3D.reset();
	
	# Examples:
	example1();
	#example2();
	#example3();
	
func example1() -> void:
	ImmediateGizmos3D.line_cube(
		Vector3(0.0, 0.0, 0.0), 	# Position (center)
		1.0, 						# Radius
		Color.WHITE 				# Color?
	);

func example2() -> void:
	# Set color.
	#ImmediateGizmos3D.set_color(Color.BLUE);
	
	# Set position relative to this node (self).
	# Move and rotate the node in the editor to see this clearly!
	#ImmediateGizmos3D.set_transform(transform);
	
	# Only show if selected in the editor.
	#ImmediateGizmos3D.set_required_selection(self);
	
	# Draw!
	ImmediateGizmos3D.line_cube(Vector3.ZERO, 1.0);
	
func example3() -> void:
	ImmediateGizmos3D.draw_text(
		"Example Text!", 			# Text
		Vector3.ZERO,				# Position
		HORIZONTAL_ALIGNMENT_LEFT,	# Horizontal Text Alignment?
		VERTICAL_ALIGNMENT_BOTTOM,	# Veritcal Text Alignment?
		1.0							# Text height? (world space)
	);
