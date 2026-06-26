from collections import deque

def is_valid(state):
    F, W, G, C = state

    # Wolf eats Goat
    if W == G and F != W:
        return False

    # Goat eats Cabbage
    if G == C and F != G:
        return False

    return True


def get_successors(state):
    F, W, G, C = state
    successors = []

    # Farmer moves alone
    new_state = (1 - F, W, G, C)
    if is_valid(new_state):
        successors.append((new_state, "Farmer crosses alone"))

    # Farmer moves with Wolf
    if F == W:
        new_state = (1 - F, 1 - W, G, C)
        if is_valid(new_state):
            successors.append((new_state, "Farmer takes Wolf"))

    # Farmer moves with Goat
    if F == G:
        new_state = (1 - F, W, 1 - G, C)
        if is_valid(new_state):
            successors.append((new_state, "Farmer takes Goat"))

    # Farmer moves with Cabbage
    if F == C:
        new_state = (1 - F, W, G, 1 - C)
        if is_valid(new_state):
            successors.append((new_state, "Farmer takes Cabbage"))

    return successors


def bfs():
    start = (0, 0, 0, 0)
    goal = (1, 1, 1, 1)

    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [(state, "Goal Reached")]

        if state in visited:
            continue

        visited.add(state)

        for next_state, action in get_successors(state):
            if next_state not in visited:
                queue.append(
                    (next_state, path + [(state, action)])
                )

    return None


def display_state(state):
    names = ["Farmer", "Wolf", "Goat", "Cabbage"]

    west = []
    east = []

    for i in range(4):
        if state[i] == 0:
            west.append(names[i])
        else:
            east.append(names[i])

    print(f"West Bank: {west}")
    print(f"East Bank: {east}")


solution = bfs()

print("\nSolution Steps:\n")

for step_no, (state, action) in enumerate(solution, start=1):
    print(f"Step {step_no}")
    print(f"Action: {action}")
    print(f"State : {state}")

    display_state(state)
    print("-" * 40)