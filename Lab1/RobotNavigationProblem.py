from collections import deque

grid = [
    ['S', '.', '.', 'X', '.'],
    ['.', 'X', '.', 'X', '.'],
    ['.', 'X', '.', '.', '.'],
    ['.', '.', 'X', 'X', '.'],
    ['.', '.', '.', '.', 'G']
]

ROWS = len(grid)
COLS = len(grid[0])

start = (0, 0)
goal = (4, 4)

directions = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1)    # Right
]


def is_valid(r, c):
    return (
        0 <= r < ROWS and
        0 <= c < COLS and
        grid[r][c] != 'X'
    )


def bfs():
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        r, c = current

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            next_cell = (nr, nc)

            if is_valid(nr, nc) and next_cell not in visited:
                queue.append((next_cell, path + [next_cell]))

    return None


path = bfs()

if path:
    print("Shortest Path:")

    for cell in path:
        print(cell)

else:
    print("No path found")