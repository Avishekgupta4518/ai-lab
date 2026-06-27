# Artificial Intelligence Lab - Problem Solving by Searching

## Overview

This repository contains the implementation of four classical Artificial Intelligence search problems. These problems demonstrate how search algorithms and backtracking techniques can be used to solve different state-space search problems.

---

# Table of Contents

1. N-Queens Problem
2. Goat, Wolf and Cabbage Problem
3. Water Jug Problem
4. Robot Navigation Problem

---

# 1. N-Queens Problem

## Problem Statement

The objective is to place **N queens** on an **N × N chessboard** such that no two queens attack each other.

A queen can attack another queen if they are placed:

* In the same row
* In the same column
* On the same diagonal

The program uses **Backtracking Search** to find a valid arrangement.

---

## State Space

A partial arrangement of queens where the first **k rows** contain queens without attacking each other.

---

## Initial State

An empty chessboard.

---

## Goal State

All N queens are placed on the board safely.

---

## Search Technique

* Backtracking
* Depth-First Search (DFS)

---

## Algorithm

1. Start from the first row.
2. Try placing a queen in every column.
3. Check whether the position is safe.
4. If safe, place the queen.
5. Move to the next row.
6. If no valid position exists, backtrack.
7. Continue until all queens are placed.

---

## Output

* Displays one valid arrangement of queens.
* Prints "No Solution" if no solution exists.

---

# 2. Goat, Wolf and Cabbage Problem

## Problem Statement

A farmer must transport a goat, a wolf, and a cabbage across a river using a boat that can carry only the farmer and one additional item.

### Constraints

* The wolf cannot be left alone with the goat.
* The goat cannot be left alone with the cabbage.

---

## State Representation

Each state represents the location (West/East) of:

* Farmer
* Wolf
* Goat
* Cabbage

Example:

(Farmer, Wolf, Goat, Cabbage)

Each value is either:

* W = West
* E = East

---

## Initial State

```
(W, W, W, W)
```

---

## Goal State

```
(E, E, E, E)
```

---

## Valid Actions

The farmer can cross the river:

* Alone
* With the Wolf
* With the Goat
* With the Cabbage

Only safe states are considered.

---

## Search Technique

* Breadth-First Search (BFS)

---

## Output

The program prints the shortest sequence of moves needed to safely transport all items.

---

# 3. Water Jug Problem

## Problem Statement

Two water jugs are available:

* Jug A = 4 Liters
* Jug B = 3 Liters

Initially both jugs are empty.

The objective is to obtain exactly **2 liters of water in Jug A**.

---

## State Representation

Each state is represented as:

```
(Jug A, Jug B)
```

Example:

```
(4,1)
```

means

* Jug A contains 4 liters
* Jug B contains 1 liter

---

## Initial State

```
(0,0)
```

---

## Goal State

```
(2,x)
```

where Jug A contains exactly 2 liters.

---

## Valid Actions

* Fill Jug A
* Fill Jug B
* Empty Jug A
* Empty Jug B
* Pour A → B
* Pour B → A

---

## Search Technique

* Breadth-First Search (BFS)

---

## Output

The shortest sequence of states leading to the goal state is displayed.

---

# 4. Robot Navigation Problem

## Problem Statement

A robot must move through a **5 × 5 grid** from the start position to the goal while avoiding obstacles.

Grid:

```
S . . X .
. X . X .
. X . . .
. . X X .
. . . . G
```

Where:

* S = Start
* G = Goal
* X = Obstacle
* . = Free Cell

---

## State Representation

Each state is represented as:

```
(row, column)
```

---

## Initial State

```
(0,0)
```

---

## Goal State

```
(4,4)
```

---

## Valid Actions

The robot may move:

* Up
* Down
* Left
* Right

The robot cannot move:

* Outside the grid
* Into obstacles

---

## Search Technique

* Breadth-First Search (BFS)

---

## Output

The program displays:

* The shortest path
* Sequence of coordinates visited
* Goal reached successfully

---

# Requirements

* Python 3.x

No external libraries are required.

Only Python built-in modules are used:

* collections
* pprint
* queue (optional)

---

# Algorithms Used

| Problem                | Algorithm                  |
| ---------------------- | -------------------------- |
| N-Queens               | Backtracking (DFS)         |
| Goat, Wolf and Cabbage | Breadth-First Search (BFS) |
| Water Jug              | Breadth-First Search (BFS) |
| Robot Navigation       | Breadth-First Search (BFS) |

---

# Learning Outcomes

After completing this laboratory, students will understand:

* State-space representation
* Search problem formulation
* Breadth-First Search (BFS)
* Backtracking algorithm
* Path finding
* Constraint satisfaction problems
* Artificial Intelligence search techniques
* Problem-solving using graph search

---

# Author

**Name:** Avishek Kumar Gupta

**Department:** Computer Engineering

**Institute:** Purwanchal Campus, IOE

---

# License

This project is developed for educational and academic purposes.
