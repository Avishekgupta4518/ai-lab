from heapq import heappush, heappop

start = (
    (5, 8, 2),
    (1, 0, 3),
    (4, 7, 6)
    )

goal = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
    )

# Heuristic 1 : Misplaced Tiles
def h1(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count = count + 1
    return count

# Heuristic 2: Manhattan Distance
def h2(state):
    distance = 0

    for i in range(3):
        for j in range(3):
            value = state[i][j]

            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3

                distance += abs(i - goal_x) + abs(j - goal_y)

    return distance

# Combined Heuristic
def h3(state):
    return h1(state) + h2(state)

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i,j
            
def get_neighbours(state):
    x,y = find_blank(state)
    moves = [(-1,0),(0,-1),(1,0),(0,1)]
    neighbours = []
    for dx, dy in moves:
        nx = x + dx
        ny = y + dy
        if 0 <=nx < 3 and 0 <= ny < 3:
            board = [list(row) for row in state]
            board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
            neighbours.append(tuple(map(tuple, board)))
    return neighbours

def display(state):
    for row in state:
        print(row)
    print()
    
def aStar(start, heuristic):
    pq = []
    heappush(pq, (heuristic(start), 0, start))
    parent = {start: None}
    g_cost = {start: 0}
    expanded = 0
    while pq:
        f, g, current = heappop(pq)
        expanded = expanded + 1
        if current == goal:
            return True, parent, expanded 
        
        for neighbour in get_neighbours(current):
            new_g = g + 1
            if neighbour not in g_cost or new_g < g_cost[neighbour]:
                g_cost[neighbour] = new_g
                f_cost = new_g + heuristic(neighbour)
                heappush(
                    pq, (f_cost, new_g, neighbour)
                )
                parent[neighbour] = current
    return False, parent, expanded

def reconstruct(parent, current):
    path = []
    while current is not None:
        path.append(current)
        current = parent[current]
    return path[::-1]

# Run all heuristics
heuristics = [
    ("h1 : Misplaced Tiles", h1),
    ("h2 : Manhattan Distance", h2),
    ("h3 : Combined Heuristic", h3)
]

for name, heuristic in heuristics:
    print(name)
    goalFound, parent, expanded = aStar(start, heuristic)

    if goalFound:
        path = reconstruct(parent, goal)

        for state in path:
            display(state)

        print("Moves =", len(path) - 1)
        print("Nodes Expanded =", expanded)

    else:
        print("Goal state is not found.")