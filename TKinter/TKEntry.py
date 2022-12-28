## Basic get value from entry widget

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

frame = ttk.Frame(root)

frame.pack()

entry = ttk.Entry(frame, width=30)

entry.pack()

def get_value():
    print(entry.get())

btn = ttk.Button(frame, text="Get value", command=get_value).pack()

root.mainloop()



