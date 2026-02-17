# main.py
import tkinter as tk
from tkinter import ttk
import random
from algorithms import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort
from renderer import Renderer

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithm Visualizer")
        self.root.configure(bg="#1e1e1e")  # dark background
        self.array = []
        self.bar_width = 15
        self.renderer = None

        # Top Frame for Controls
        self.top_frame = tk.Frame(root, bg="#1e1e1e")
        self.top_frame.pack(side=tk.TOP, pady=10)

        tk.Label(self.top_frame, text="Sorting Algorithm Visualizer", font=("Helvetica", 16, "bold"),
                 fg="white", bg="#1e1e1e").grid(row=0, column=0, columnspan=4, pady=10)

        # Dropdown
        self.algorithm_var = tk.StringVar(value="Bubble Sort")
        algorithms = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort"]
        tk.Label(self.top_frame, text="Algorithm:", fg="white", bg="#1e1e1e").grid(row=1, column=0, padx=5)
        self.dropdown = ttk.Combobox(self.top_frame, values=algorithms, textvariable=self.algorithm_var, width=15)
        self.dropdown.grid(row=1, column=1, padx=5)

        # Generate Array Button
        self.generate_btn = tk.Button(self.top_frame, text="Generate Array", bg="#007acc", fg="white",
                                      command=self.generate_array, width=12)
        self.generate_btn.grid(row=1, column=2, padx=5)

        # Start Button
        self.start_btn = tk.Button(self.top_frame, text="Start Sorting", bg="#28a745", fg="white",
                                   command=self.start_sort, width=12)
        self.start_btn.grid(row=1, column=3, padx=5)

        # Speed Slider
        self.speed_frame = tk.Frame(root, bg="#1e1e1e")
        self.speed_frame.pack(side=tk.TOP, pady=10)
        tk.Label(self.speed_frame, text="Speed:", fg="white", bg="#1e1e1e").pack(side=tk.LEFT)
        self.speed_slider = tk.Scale(self.speed_frame, from_=0.03, to=0.50, resolution=0.01,
                                     orient=tk.HORIZONTAL, bg="#1e1e1e", fg="white", length=400)
        self.speed_slider.set(0.05)
        self.speed_slider.pack(side=tk.LEFT, padx=5)

        # Canvas for visualization
        self.canvas_frame = tk.Frame(root, bg="#1e1e1e")
        self.canvas_frame.pack(pady=10)
        self.canvas = tk.Canvas(self.canvas_frame, width=800, height=400, bg="#252526")
        self.canvas.pack()

    def generate_array(self):
        self.array = [random.randint(1, 50) for _ in range(10)]
        num_bars = len(self.array)
        self.bar_width = 60  # make each bar wider
        self.padding = (800 - num_bars * self.bar_width) // 2  # center bars on canvas
        self.renderer = Renderer(self.canvas, self.array, self.bar_width, self.speed_slider.get(), self.padding)


    def start_sort(self):
        if not self.renderer:
            return
        self.renderer.set_speed(self.speed_slider.get())
        algorithm = self.algorithm_var.get()
        if algorithm == "Bubble Sort":
            gen = bubble_sort(self.array)
        elif algorithm == "Selection Sort":
            gen = selection_sort(self.array)
        elif algorithm == "Insertion Sort":
            gen = insertion_sort(self.array)
        elif algorithm == "Merge Sort":
            gen = merge_sort(self.array)
        elif algorithm == "Quick Sort":
            gen = quick_sort(self.array)
        else:
            return

        for step in gen:
            self.renderer.render_step(step)

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()
from controller import Controller
from renderer import Renderer


def main():
    controller = Controller()
    renderer = Renderer(controller)
    renderer.run()


if __name__ == "__main__":
    main()
