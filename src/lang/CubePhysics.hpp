#include "godot_cpp/templates/hash_map.hpp"
#include "godot_cpp/templates/hash_set.hpp"
#include "godot_cpp/templates/vector.hpp"

namespace cube_physics {

using namespace godot;

struct Space;

const float MIN_PENETRATION_DEPTH = 0.001f;

struct AABB {
	Vector3 vmin;
	Vector3 vmax;

	AABB() :
			vmin(Vector3(0, 0, 0)), vmax(Vector3(0, 0, 0)) {}
	AABB(Vector3 vmin, Vector3 vmax) :
			vmin(vmin), vmax(vmax) {}

	Vector3 position() const { return vmin; }
	Vector3 size() const { return vmax - vmin; }

	void move(Vector3 delta) {
		vmin += delta;
		vmax += delta;
	}

	bool intersects(const AABB &other, AABB *p_overlap) const {
		AABB overlap(
				Vector3(std::max(vmin.x, other.vmin.x), std::max(vmin.y, other.vmin.y), std::max(vmin.z, other.vmin.z)),
				Vector3(std::min(vmax.x, other.vmax.x), std::min(vmax.y, other.vmax.y), std::min(vmax.z, other.vmax.z)));

		Vector3 overlap_size = overlap.size();
		if (overlap_size.x <= MIN_PENETRATION_DEPTH)
			return false;
		if (overlap_size.y <= MIN_PENETRATION_DEPTH)
			return false;
		if (overlap_size.z <= MIN_PENETRATION_DEPTH)
			return false;

		if (p_overlap)
			*p_overlap = overlap;
		return true;
	}

	Vector3 find_min_size_axis(float *p_min_size) const {
		Vector3 overlap_size = size();
		if (overlap_size.x < overlap_size.y && overlap_size.x < overlap_size.z) {
			*p_min_size = overlap_size.x;
			return Vector3(1, 0, 0);
		} else if (overlap_size.y < overlap_size.z) {
			*p_min_size = overlap_size.y;
			return Vector3(0, 1, 0);
		} else {
			*p_min_size = overlap_size.z;
			return Vector3(0, 0, 1);
		}
	}
};

struct Body {
	Body *prev;
	Body *next;
	void *ctx;

	AABB aabb;
	Vector3 velocity;
	Vector3 instant_velocity;

	uint32_t layer;

	bool is_static;
	bool is_trigger;

	float mass;

	float inv_mass() const {
		return is_static ? 0 : 1 / mass;
	}

	Vector3 position() const { return aabb.position(); }

	void zero_velocity() {
		velocity = Vector3(0, 0, 0);
	}

	bool is_moving() const {
		return velocity != Vector3(0, 0, 0);
	}
};

struct Space {
	float chunk_size;
	Vector3 gravity;
	uint32_t layer_masks[32];

	HashMap<Vector2i, Body *> chunks;

	HashSet<Body *> moving_bodies;

	Space(float chunk_size) :
			chunk_size(chunk_size) {}

	void add_body(Body *body) {
		Vector2i chunk_pos = to_chunk(body->position());
		if (chunks.has(chunk_pos)) {
			Body *head = chunks[chunk_pos];
			body->prev = nullptr;
			body->next = head;
			head->prev = body;
			chunks[chunk_pos] = body;
		} else {
			body->prev = nullptr;
			body->next = nullptr;
			chunks[chunk_pos] = body;
		}
	}

	Vector2i to_chunk(Vector3 position) const {
		return Vector2i(
				static_cast<int>(floor(position.x / chunk_size)),
				static_cast<int>(floor(position.z / chunk_size)));
	}

	void point_cast(Vector3 point);
	void ray_cast(Vector3 from, Vector3 to, float max_distance);
	void circle_cast(Vector3 center, float radius);
	void sphere_cast(Vector3 center, float radius);
	void cube_cast(AABB cube);

	void step(float delta);
};

struct BroadPhaseIter {
	Space *space;
	AABB aabb;
	uint32_t layer_mask;

	Vector2i base_chunk_pos;
	int chunk_index;
	Body *candidate;

	BroadPhaseIter(Space *space, const AABB &aabb, uint32_t layer_mask) {
		this->space = space;
		this->aabb = aabb;
		this->layer_mask = layer_mask;
		this->base_chunk_pos = space->to_chunk(aabb.position());
		this->chunk_index = -1;
		this->candidate = nullptr;
	}

	Body *next(AABB *p_overlap);
};

struct CollisionPair {
	Body *a; // non-static
	Body *b;

	CollisionPair(Body *a, Body *b) :
			a(a), b(b) {}

	bool operator==(const CollisionPair &other) const {
		return (a == other.a && b == other.b) || (a == other.b && b == other.a);
	}

	bool operator!=(const CollisionPair &other) const {
		return !(*this == other);
	}

	bool is_trigger() const {
		return a->is_trigger || b->is_trigger;
	}

	struct Hasher {
		size_t operator()(const CollisionPair &pair) const {
			return std::hash<Body *>()(pair.a) ^ std::hash<Body *>()(pair.b);
		}
	};
};

} // namespace cube_physics