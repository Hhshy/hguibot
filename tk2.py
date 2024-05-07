# -*- coding: utf-8 -*-            
# @Author : Code_Hsy
# @Time : 2024-02-19 11:29

import tkinter as tk


class TimerDemo:
    def __init__(self, root):
        self.root = root
        self.counter = 0
        self.timer_running = False
        self.timer_label = tk.Label(root, text="0")
        self.timer_label.pack()
        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack()
        self.pause_button = tk.Button(root, text="Pause", command=self.pause_timer)
        self.pause_button.pack()

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def pause_timer(self):
        self.timer_running = False

    def update_timer(self):
        if self.timer_running:
            self.counter += 1
            self.timer_label.config(text=str(self.counter))
            self.root.after(1000, self.update_timer)


root = tk.Tk()
demo = TimerDemo(root)
root.mainloop()
