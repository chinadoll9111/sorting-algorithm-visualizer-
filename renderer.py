# renderer.py
import time
import tkinter as tk

class Renderer:
    def __init__(self, canvas, array, bar_width, speed=0.05, padding=0):
        self.canvas = canvas
        self.array = array
        self.bar_width = bar_width
        self.speed = speed
        self.padding = padding
        self.bars = []
        self.create_bars()  # make sure this is inside __init__

    def set_speed(self, speed):
        self.speed = speed

    def create_bars(self):
        self.canvas.delete("all")
        self.bars = []
        for i, val in enumerate(self.array):
            x0 = self.padding + i * self.bar_width
            y0 = 400 - val * 7  # scale height for visibility
            x1 = self.padding + (i+1) * self.bar_width
            y1 = 400

            # Draw bar
            bar = self.canvas.create_rectangle(x0, y0, x1, y1, fill="#007acc", outline="#1e1e1e")
            self.bars.append(bar)

            # Draw number label above bar
            self.canvas.create_text(x0 + self.bar_width/2, y0 - 10, text=str(val),
                                    fill="white", font=("Helvetica", 12, "bold"))
        self.canvas.update_idletasks()

    def render_step(self, step):
        op, i, j = step
        if op == "compare":
            self.canvas.itemconfig(self.bars[i], fill="orange")
            self.canvas.itemconfig(self.bars[j], fill="orange")
        elif op == "swap" or op == "overwrite":
            self.create_bars()
        elif op == "sorted":
            for bar in self.bars:
                self.canvas.itemconfig(bar, fill="#28a745")  # green
        self.canvas.update_idletasks()
        time.sleep(max(0.01, self.speed))
import tkinter as tk
import random


class Renderer:
    def __init__(self, controller):
        self.controller = controller

        self.root = tk.Tk()
        self.root.title("Sorting Visualizer")

        self.width = 1000
        self.height = 500

        self.array = []
        self.generator = None
        self.running = False
        self.paused = False

        # ---------------- CONTROL FRAME ----------------
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)

        # Algorithm Dropdown
        self.algorithm_var = tk.StringVar()
        self.algorithm_var.set("Bubble Sort")

        dropdown = tk.OptionMenu(
            control_frame,
            self.algorithm_var,
            "Bubble Sort",
            "Selection Sort",
            "Insertion Sort",
            "Merge Sort",
            "Quick Sort",
            command=self.update_complexity
        )
        dropdown.pack(side=tk.LEFT, padx=10)

        # Start Button
        tk.Button(control_frame, text="Start", command=self.start_sort).pack(side=tk.LEFT, padx=5)

        # Pause Button
        self.pause_button = tk.Button(control_frame, text="Pause", command=self.toggle_pause)
        self.pause_button.pack(side=tk.LEFT, padx=5)

        # Generate Button
        tk.Button(control_frame, text="Generate New Array", command=self.generate_array).pack(side=tk.LEFT, padx=5)

        # Speed Slider
        self.speed_scale = tk.Scale(
            control_frame,
            from_=1,
            to=200,
            orient=tk.HORIZONTAL,
            label="Speed (ms)"
        )
        self.speed_scale.set(30)
        self.speed_scale.pack(side=tk.LEFT, padx=10)

        # Time Complexity Label
        self.complexity_label = tk.Label(self.root, text="")
        self.complexity_label.pack()

        # Canvas
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="white")
        self.canvas.pack()

        # Colors
        self.default_color = "steelblue"
        self.compare_color = "orange"
        self.swap_color = "red"
        self.overwrite_color = "green"

        self.generate_array()
        self.update_complexity(self.algorithm_var.get())

    # ---------------- ARRAY GENERATION ----------------

    def generate_array(self):
        self.array = [random.randint(10, 400) for _ in range(60)]
        self.running = False
        self.draw_array()

    # ---------------- DRAWING ----------------

    def draw_array(self, highlight_indices=None, color=None):
        self.canvas.delete("all")

        if highlight_indices is None:
            highlight_indices = []

        bar_width = self.width / len(self.array)
        max_value = max(self.array)

        for i, value in enumerate(self.array):
            x0 = i * bar_width
            y0 = self.height - (value / max_value) * (self.height - 20)
            x1 = (i + 1) * bar_width
            y1 = self.height

            bar_color = self.default_color

            if i in highlight_indices:
                bar_color = color

            self.canvas.create_rectangle(x0, y0, x1, y1, fill=bar_color, outline="")

        self.root.update_idletasks()

    # ---------------- SORT CONTROL ----------------

    def start_sort(self):
        if self.running:
            return

        self.controller.set_algorithm(self.algorithm_var.get())
        self.generator = self.controller.algorithm(self.array)

        self.running = True
        self.paused = False
        self.animate()

    def animate(self):
        if not self.running or self.paused:
            return

        try:
            action = next(self.generator)
            self.handle_action(action)

            delay = self.speed_scale.get()
            self.root.after(delay, self.animate)

        except StopIteration:
            self.running = False

    def toggle_pause(self):
        if not self.running:
            return

        self.paused = not self.paused

        if not self.paused:
            self.animate()

    # ---------------- HANDLE ACTION ----------------

    def handle_action(self, action):
        action_type, i, j = action

        if action_type == "compare":
            self.draw_array([i, j], self.compare_color)

        elif action_type == "swap":
            self.draw_array([i, j], self.swap_color)

        elif action_type == "overwrite":
            self.draw_array([i], self.overwrite_color)

        elif action_type == "sorted":
            self.draw_array()

    # ---------------- COMPLEXITY INFO ----------------

    def update_complexity(self, algorithm_name):
        complexities = {
            "Bubble Sort": "Time: O(n²) | Space: O(1)",
            "Selection Sort": "Time: O(n²) | Space: O(1)",
            "Insertion Sort": "Time: O(n²) | Space: O(1)",
            "Merge Sort": "Time: O(n log n) | Space: O(n)",
            "Quick Sort": "Time: O(n log n) avg | O(n²) worst | Space: O(log n)"
        }

        self.complexity_label.config(text=complexities[algorithm_name])

    # ---------------- RUN ----------------

    def run(self):
        self.root.mainloop()
