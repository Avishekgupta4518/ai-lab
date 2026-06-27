import tkinter as tk
from tkinter import ttk

# Import everything from your algorithm file
from EightPuzzleProblem import *

current_path = []
current_step = 0

# Display Puzzle Board
def show_board(state):
    for i in range(3):
        for j in range(3):
            value = state[i][j]

            if value == 0:
                buttons[i][j]["text"] = ""
                buttons[i][j]["bg"] = "white"
            else:
                buttons[i][j]["text"] = str(value)
                buttons[i][j]["bg"] = "lightblue"

# Solve Puzzle
def solve():
    global current_path, current_step
    heuristic_name = combo.get()

    if heuristic_name == "Misplaced Tiles":
        heuristic = h1
    elif heuristic_name == "Manhattan Distance":
        heuristic = h2
    else:
        heuristic = h3

    found, parent, expanded = aStar(start, heuristic)

    if found:
        current_path = reconstruct(parent, goal)
        current_step = 0

        show_board(current_path[0])

        move_label.config(text="Moves : " + str(len(current_path)-1))
        expanded_label.config(text="Nodes Expanded : " + str(expanded))
        step_label.config(text="Step : 1 / " + str(len(current_path)))

    else:
        result_label.config(text="Goal Not Found")

# Next State

def next_step():
    global current_step

    if len(current_path) == 0:
        return

    if current_step < len(current_path)-1:
        current_step += 1
        show_board(current_path[current_step])

        step_label.config(
            text=f"Step : {current_step+1} / {len(current_path)}"
        )

# Previous State

def previous_step():
    global current_step

    if len(current_path) == 0:
        return

    if current_step > 0:
        current_step -= 1
        show_board(current_path[current_step])

        step_label.config(
            text=f"Step : {current_step+1} / {len(current_path)}"
        )

# GUI Window

root = tk.Tk()
root.title("A* 8 Puzzle Solver")
root.geometry("500x600")
root.configure(bg="white")


title = tk.Label(
    root,
    text="A* 8 Puzzle Solver",
    font=("Arial",20,"bold"),
    bg="white"
)

title.pack(pady=10)

# Puzzle Board

frame = tk.Frame(root,bg="white")
frame.pack()

buttons = []

for i in range(3):
    row=[]

    for j in range(3):

        btn = tk.Label(
            frame,
            text="",
            width=4,
            height=2,
            font=("Arial",24,"bold"),
            relief="solid",
            bg="white"
        )

        btn.grid(row=i,column=j,padx=5,pady=5)

        row.append(btn)

    buttons.append(row)


show_board(start)

# Heuristic Selection

combo = ttk.Combobox(
    root,
    values=[
        "Misplaced Tiles",
        "Manhattan Distance",
        "Combined"
    ],
    state="readonly",
    width=25
)

combo.current(0)
combo.pack(pady=20)

# Solve Button

solve_btn = tk.Button(
    root,
    text="Solve",
    font=("Arial",12,"bold"),
    command=solve,
    bg="green",
    fg="white",
    width=15
)

solve_btn.pack()

# Navigation Buttons

nav = tk.Frame(root,bg="white")
nav.pack(pady=20)

prev_btn = tk.Button(
    nav,
    text="Previous",
    command=previous_step,
    width=12,
    bg="orange"
)

prev_btn.grid(row=0,column=0,padx=10)

next_btn = tk.Button(
    nav,
    text="Next",
    command=next_step,
    width=12,
    bg="lightgreen"
)

next_btn.grid(row=0,column=1,padx=10)

# Information
step_label = tk.Label(
    root,
    text="Step : 0",
    font=("Arial",12),
    bg="white"
)

step_label.pack()

move_label = tk.Label(
    root,
    text="Moves : 0",
    font=("Arial",12),
    bg="white"
)

move_label.pack()

expanded_label = tk.Label(
    root,
    text="Nodes Expanded : 0",
    font=("Arial",12),
    bg="white"
)

expanded_label.pack()

result_label = tk.Label(
    root,
    text="",
    font=("Arial",12,"bold"),
    fg="red",
    bg="white"
)

result_label.pack(pady=10)

root.mainloop()