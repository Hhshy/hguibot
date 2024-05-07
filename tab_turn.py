# -*- coding: utf-8 -*-            
# @Author : Code_Hsy
# @Time : 2024-02-20 9:30

import tkinter as tk


class Page_1:  # 这是第一个页面
    def __init__(self, window):
        self.window = window
        self.window.title("p1")
        self.window.geometry("200x200")
        self.window.config(bg="#F9C03D")
        self.button = tk.Button(self.window, text="跳转", command=self.change)
        self.button.pack()

    def change(self):
        # pass  # 不知道怎么写，先占位
        self.button.destroy()
        root2 = tk.Tk()
        Page_2(root2)


class Page_2:  # 这是第二个页面
    def __init__(self, window):
        self.window = window
        self.window.title("p2")
        self.window.geometry("300x300")
        self.window.config(bg="#0F375A")
        self.button = tk.Button(self.window, text="返回", command=self.back)
        self.button.pack()

    def back(self):
        # pass  # 不知道怎么写，先占位
        self.button.destroy()
        Page_1(root)


root = tk.Tk()

p1 = Page_1(root)  # 这两个页单，可单独运行
# p2 = Page_2(root)
root.mainloop()
