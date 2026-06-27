# Artificial Intelligence Lab 2 - Problem Solving using Informed Search (A* Search for 8-Puzzle)

## Overview

This project implements the **A* (A-Star) Search Algorithm** to solve the **8-Puzzle Problem**, a classical Artificial Intelligence search problem. The implementation compares the performance of three heuristic functions:

* **h₁(n): Misplaced Tiles**
* **h₂(n): Manhattan Distance**
* **h₃(n): Combined Heuristic (h₁ + h₂)**

The project demonstrates how heuristic functions influence the efficiency of informed search algorithms by comparing the number of moves and nodes expanded for each heuristic.

---

# Table of Contents

1. Introduction
2. Problem Statement
3. Problem Formulation
4. Heuristics
5. A* Search Algorithm
6. Sample Output
7. Performance Comparison
8. Learning Outcomes

---

# Introduction

The **8-Puzzle Problem** consists of a **3 × 3 board** containing eight numbered tiles and one blank space (represented by **0**). The objective is to rearrange the tiles from an initial configuration to a predefined goal configuration by sliding one tile at a time into the blank space.

Since every move has an equal cost, the **A*** search algorithm is used to efficiently find the shortest solution path using heuristic functions.

---

# Problem Statement

Given an initial arrangement of tiles, find the shortest sequence of moves required to reach the goal state.

### Initial State

```text
5 8 2
1 0 3
4 7 6
```

### Goal State

```text
1 2 3
4 5 6
7 8 0
```

---

# Problem Formulation

## State Space

All possible configurations of eight numbered tiles and one blank space.

---

## Initial State

The given starting arrangement of the puzzle.

---

## Goal State

The desired arrangement where all numbered tiles are in their correct positions.

---

## Successor Function

Generate new states by moving the blank tile in one of the following directions:

* Up
* Down
* Left
* Right

Only valid moves inside the puzzle boundaries are allowed.

---

## Path Cost

Each move has a cost of **1**.

---

## Goal Test

The algorithm terminates when the current state matches the goal configuration.

---

# A* Search Algorithm

A* is an informed search algorithm that evaluates nodes using:

[
f(n)=g(n)+h(n)
]

Where:

* **g(n)** = Actual cost from the start state to the current state.
* **h(n)** = Estimated cost from the current state to the goal.
* **f(n)** = Total estimated cost.

The node with the smallest **f(n)** value is expanded first.

---

# Heuristic Functions

## 1. Misplaced Tiles (h₁)

Counts the number of tiles that are not in their correct goal position.

### Formula

```text
h₁(n) = Number of misplaced tiles
```

### Advantages

* Very simple
* Easy to implement
* Guarantees an optimal solution

### Disadvantages

* Provides limited information
* Usually expands more nodes

---

## 2. Manhattan Distance (h₂)

Calculates the total horizontal and vertical distance each tile is away from its goal position.

### Formula

```text
h₂(n) = Σ |current_row − goal_row| + |current_column − goal_column|
```

### Advantages

* More informative than Misplaced Tiles
* Expands fewer nodes
* Faster search

### Disadvantages

* Slightly more computational work per node

---

## 3. Combined Heuristic (h₃)

The combined heuristic is calculated as:

```text
h₃(n) = h₁(n) + h₂(n)
```

This heuristic attempts to make the search more informed by combining both heuristic values.

### Advantages

* Provides stronger guidance during search
* May reduce node expansion

### Note

The combined heuristic is useful for comparison purposes but may not always satisfy the admissibility property required for guaranteed optimal A* solutions.

---

# Algorithm Workflow

1. Start from the initial state.
2. Compute the heuristic value.
3. Insert the state into the priority queue.
4. Expand the state with the smallest **f(n)**.
5. Generate all valid neighboring states.
6. Compute their costs.
7. Repeat until the goal state is reached.
8. Reconstruct and display the solution path.

---

# Program Output

For each heuristic, the program displays:

* Solution path
* Total number of moves
* Number of expanded nodes

Example:

```text
Using h1 : Misplaced Tiles

(5, 8, 2)
(1, 0, 3)
(4, 7, 6)

↓

...

Goal Reached

Moves = 10

Nodes Expanded = 98
```

---

# Performance Comparison

The program compares three heuristic functions.

| Heuristic | Description        | Expected Performance               |
| --------- | ------------------ | ---------------------------------- |
| h₁        | Misplaced Tiles    | Expands more nodes                 |
| h₂        | Manhattan Distance | Expands fewer nodes                |
| h₃        | Combined Heuristic | Usually provides stronger guidance |

The comparison includes:

* Solution path
* Number of moves
* Nodes expanded
* Search efficiency

---

# Features

* Implementation of A* Search Algorithm
* Misplaced Tiles Heuristic
* Manhattan Distance Heuristic
* Combined Heuristic
* Automatic path reconstruction
* Performance comparison
* Interactive GUI using Tkinter
* Step-by-step puzzle visualization
* Displays moves and expanded nodes

---

# Learning Outcomes

After completing this laboratory, students will understand:

* Informed Search Algorithms
* A* Search Algorithm
* Priority Queue implementation
* Heuristic Functions
* Misplaced Tiles Heuristic
* Manhattan Distance Heuristic
* State-space search
* Path reconstruction
* Performance evaluation of search algorithms
* GUI development using Tkinter

---

# Future Improvements

Possible enhancements include:

* Solvability checking before search
* Animated tile movement
* Additional heuristic functions
* Greedy Best-First Search implementation
* Uniform Cost Search comparison
* Random puzzle generation
* User-defined puzzle input

---

# Author

**Name:** Avishek Kumar Gupta

**Lab:** Lab 2 – Problem Solving using Informed Search

**Department:** Computer Engineering

**Institute:** Purwanchal Campus, IOE

---

# License

This project is developed for educational and academic purposes only.
