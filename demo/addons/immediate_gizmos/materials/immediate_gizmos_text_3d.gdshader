shader_type spatial;
render_mode unshaded;

uniform sampler2D textAtlas : filter_linear_mipmap;

void fragment() {
	vec4 color = texture(textAtlas, UV) * COLOR;
	if (color.a < 0.5) discard;
	ALBEDO = color.rgb;
}
