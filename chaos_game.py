import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
from tkinter import filedialog
import math
import matplotlib.cm as cm
import numpy as np

def generate_polygon(n, radius=1, center=(0.5, 0.5)):
    cx, cy = center
    return [
        (
            cx + radius * math.cos(2 * math.pi * i / n),
            cy + radius * math.sin(2 * math.pi * i / n)
        )
        for i in range(n)
    ]

def run_chaos_game():

    # Parameter holen
    try:
        num_vertices = int(vertex_entry.get())
        iterations = int(iterations_entry.get())
        step = float(step_entry.get())
    except ValueError:
        return

    vertices = generate_polygon(num_vertices)

    x, y = random.random(), random.random()
    points_x, points_y = [], []

    for _ in range(iterations):
        vx, vy = random.choice(vertices)
        x = x + step * (vx - x)
        y = y + step * (vy - y)
        points_x.append(x)
        points_y.append(y)

    # Plot anzeigen
    ax.clear()
    ax.scatter(points_x, points_y, s=0.1, color='black')
    ax.set_title(f'Chaos Game with {num_vertices} vertices and step {step}')
    ax.axis('equal')
    ax.axis('off')
    canvas.draw()

import matplotlib.cm as cm
import numpy as np

def run_multiple_chaos_games():
    try:
        num_vertices = int(vertex_entry.get())
        iterations = int(iterations_entry.get())
    except ValueError:
        return

    step_values = [round(0.4 + i * 0.1, 1) for i in range(16)]

    global fig, canvas
    canvas.get_tk_widget().destroy()
    fig, axes = plt.subplots(nrows=4, ncols=4, figsize=(16, 16))
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()
    fig.subplots_adjust(hspace=0.4)

    norm = plt.Normalize(min(step_values), max(step_values))
    

    for idx, step in enumerate(step_values):
        row = idx // 4
        col = idx % 4
        ax = axes[row][col]

      

        vertices = generate_polygon(num_vertices)
        x, y = random.random(), random.random()
        points_x, points_y = [], []

        for _ in range(iterations):
            vx, vy = random.choice(vertices)
            x = x + step * (vx - x)
            y = y + step * (vy - y)
            points_x.append(x)
            points_y.append(y)

        ax.scatter(points_x, points_y, s=0.3, color=color)
        ax.set_title(f"Step = {step}", fontsize=8)
        ax.axis('equal')
        ax.axis('off')

    canvas.draw()




def save_plot():


    try:
        num_vertices = int(vertex_entry.get())
        step = float(step_entry.get())
    except ValueError:
        num_vertices = "?"
        step = "?"

    default_name = f"chaosgame_v{num_vertices}_s{step}_madebyjakobtea.png"

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
        initialfile=default_name 
    )

    if file_path:
        fig.savefig(file_path, bbox_inches='tight', dpi=300)
        print(f"Plot saved as {file_path}")

# GUI mit Tkinter
root = tk.Tk()
root.title("Interactive Chaos Game")

# Eingabefelder
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

ttk.Label(frame, text="corners (3+):").grid(row=0, column=0)
vertex_entry = ttk.Entry(frame)
vertex_entry.insert(0, "3")
vertex_entry.grid(row=0, column=1)

ttk.Label(frame, text="interations:").grid(row=1, column=0)
iterations_entry = ttk.Entry(frame)
iterations_entry.insert(0, "10000")
iterations_entry.grid(row=1, column=1)

ttk.Label(frame, text="Step factor (z. B. 0.5):").grid(row=2, column=0)
step_entry = ttk.Entry(frame)
step_entry.insert(0, "0.5")
step_entry.grid(row=2, column=1)

ttk.Button(frame, text="Start", command=run_chaos_game).grid(row=3, column=0, columnspan=2, pady=5)
ttk.Button(frame, text="Save as PNG", command=save_plot).grid(row=4, column=0, columnspan=2, pady=5)
ttk.Button(frame, text="Run multiple games", command=run_multiple_chaos_games).grid(row=5, column=0, columnspan=2, pady=5)


# Matplotlib-Canvas
fig, ax = plt.subplots(figsize=(5, 5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()
root.mainloop()
