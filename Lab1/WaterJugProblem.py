from collections import deque

CAPACITY_A = 4
CAPACITY_B = 3


def get_next_states(state):
    a, b = state
    states = []

    # Fill operations
    states.append((CAPACITY_A, b))
    states.append((a, CAPACITY_B))

    # Empty operations
    states.append((0, b))
    states.append((a, 0))

    # Pour A -> B
    transfer = min(a, CAPACITY_B - b)
    states.append((a - transfer, b + transfer))

    # Pour B -> A
    transfer = min(b, CAPACITY_A - a)
    states.append((a + transfer, b - transfer))

    return states


def bfs():
    start = (0, 0)

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state[0] == 2:
            return path

        if state in visited:
            continue

        visited.add(state)

        for next_state in get_next_states(state):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))

    return None


solution = bfs()

print("Shortest Path:")

for step in solution:
    print(step)