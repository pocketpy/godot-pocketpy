#include "CubePhysics.hpp"
#include <cassert>

namespace cube_physics {

static const Vector2i DIR_9[9] = {
	Vector2i(-1, -1), Vector2i(0, -1), Vector2i(1, -1),
	Vector2i(-1, 0), Vector2i(0, 0), Vector2i(1, 0),
	Vector2i(-1, 1), Vector2i(0, 1), Vector2i(1, 1)
};

Body *BroadPhaseIter::next(AABB *p_overlap) {
	while (true) {
		if (candidate) {
			if (candidate->layer & layer_mask) {
				if(aabb.intersects(candidate->aabb, p_overlap)) {
					Body *retval = candidate;
					candidate = candidate->next;
					return retval;
				}
			}
			candidate = candidate->next;
		} else {
			chunk_index++;
			if (chunk_index >= 9) {
				return nullptr;
			}
			Vector2i chunk_pos = base_chunk_pos + DIR_9[chunk_index];
			Body **p_candidates = space->chunks.getptr(chunk_pos);
			candidate = p_candidates ? *p_candidates : nullptr;
		}
	}
}

void Space::step(float delta) {
	HashMap<CollisionPair, AABB, CollisionPair::Hasher> cached_pairs;

	// find collision pairs
	for (Body *a : moving_bodies) {
		assert(!a->is_static);
		assert(a->is_moving());

		BroadPhaseIter iter(this, a->aabb, layer_masks[a->layer]);
		AABB overlap;
		while (Body *b = iter.next(&overlap)) {
			CollisionPair pair(a, b);
			if (!cached_pairs.has(pair)) {
				cached_pairs.insert(pair, overlap);
			}
		}
	}

	// resolve collisions
	for (const auto &[pair, overlap] : cached_pairs) {
		if (pair.is_trigger())
			continue;

		float a_inv_mass = pair.a->inv_mass();
		float b_inv_mass = pair.b->inv_mass();
		float penetration;
		Vector3 n = overlap.find_min_size_axis(&penetration);

		// penetration resolution
		Vector3 correction = n * penetration;
		pair.a->instant_velocity += correction * a_inv_mass;
		if (!pair.b->is_static) {
			pair.b->instant_velocity -= correction * b_inv_mass;
			moving_bodies.insert(pair.b);
		}

		// impulse-based collision resolution
		Vector3 v_rel = pair.a->velocity - pair.b->velocity;
		float v_rel_n = v_rel.dot(n);
		if (v_rel_n < 0) {
			// resolve collision
			float e = 0.5f; // restitution
			float j = -(1 + e) * v_rel_n / (a_inv_mass + b_inv_mass);
			pair.a->velocity += j * n * a_inv_mass;
			if (!pair.b->is_static) {
				pair.b->velocity -= j * n * b_inv_mass;
				moving_bodies.insert(pair.b);
			}
		} else {
			// resting contact, do nothing
		}
	}

	// move bodies by its velocity
	for (Body *body : moving_bodies) {
		// body->velocity += this->gravity * delta;
		Vector3 total_vel = body->velocity + body->instant_velocity;
		body->instant_velocity.zero();
		body->aabb.move(total_vel * delta);
	}

	// trigger user callbacks
	// NOTE: must do it here because user may create/destroy bodies
	for (const auto &[pair, overlap] : cached_pairs) {
		if (pair.is_trigger()) {
		} else {
		}
	}
}

} // namespace cube_physics