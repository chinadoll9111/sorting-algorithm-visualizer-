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
