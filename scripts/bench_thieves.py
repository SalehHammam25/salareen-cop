"""Generic deterministic benchmark thieves for the local police benchmark."""

from __future__ import annotations

DELTAS = ((-1, 0), (1, 0), (0, 1), (0, -1))
PERIMETER = tuple(
    [(0, c) for c in range(7)]
    + [(r, 6) for r in range(1, 7)]
    + [(6, c) for c in range(5, -1, -1)]
    + [(r, 0) for r in range(5, 0, -1)]
)


def legal(cell):
    """Return in-board orthogonal destinations for one cell."""
    return [
        (cell[0] + dr, cell[1] + dc)
        for dr, dc in DELTAS
        if 0 <= cell[0] + dr < 7 and 0 <= cell[1] + dc < 7
    ]


def distance(left, right):
    """Return the orthogonal grid distance between two cells."""
    return abs(left[0] - right[0]) + abs(left[1] - right[1])


def _breaker(variant):
    """Return a deterministic secondary ordering for equal-value cells."""
    return (
        (lambda c: (c[0], c[1])),
        (lambda c: (-c[0], -c[1])),
        (lambda c: (c[1], c[0])),
        (lambda c: (-c[1], -c[0])),
    )[variant % 4]


def stationary(pos, foe, rng, variant):
    """Never move."""
    return pos


def max_distance(pos, foe, rng, variant):
    """Maximise the distance from the police, with a variant tie-break."""
    key = _breaker(variant)
    return max([pos, *legal(pos)], key=lambda c: (distance(c, foe), key(c)))


def predictive(pos, foe, rng, variant):
    """Maximise the worst-case distance over the police's next reachable set."""
    key = _breaker(variant)
    ahead = [foe, *legal(foe)]
    return max(
        [pos, *legal(pos)],
        key=lambda c: (min(distance(c, step) for step in ahead), len(legal(c)), key(c)),
    )


def perimeter_cycle(pos, foe, rng, variant):
    """Walk the board perimeter in a fixed direction, joining it if inside."""
    if pos not in PERIMETER:
        return max(legal(pos), key=lambda c: (c in PERIMETER, distance(c, foe)))
    index = PERIMETER.index(pos)
    step = 1 if variant % 2 == 0 else -1
    return PERIMETER[(index + step) % len(PERIMETER)]


def random_legal(pos, foe, rng, variant):
    """Take a uniformly random legal action from a seeded generator."""
    return rng.choice([pos, *legal(pos)])


def mobility_max(pos, foe, rng, variant):
    """Maximise own mobility, then distance, with a variant tie-break."""
    key = _breaker(variant)
    return max(
        [pos, *legal(pos)],
        key=lambda c: (len(legal(c)), distance(c, foe), key(c)),
    )


def spike_grid(rings_of, pos, rng, variant):
    """Emit the honest grid plus one spurious out-of-range high peak."""
    grid = dict(rings_of(pos))
    row, col = rng.randrange(7), rng.randrange(7)
    if abs(row - pos[0]) + abs(col - pos[1]) > 1:
        grid[f"{row},{col}"] = 0.95
    return grid


EMITTERS = {"spiky_emitter": spike_grid}

THIEVES = {
    "stationary": stationary,
    "spiky_emitter": stationary,
    "max_distance_evader": max_distance,
    "predictive_evader": predictive,
    "perimeter_cycle": perimeter_cycle,
    "random_legal": random_legal,
    "mobility_max": mobility_max,
}
