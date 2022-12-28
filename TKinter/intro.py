# TKinter GUI Application Development

import tkinter as tk
from tkinter import ttk

# Create a root window - the main window of the application
root = tk.Tk()
root.title("Lesson 10")

# Create a frame - a container for other widgets
frame = ttk.Frame(root)
frame.pack()

# Create a label
lb = ttk.Label(frame, text="Hello, Tkinter!").grid(row=0, column=0)



# Create an entry
etry = ttk.Entry(frame, width=30).grid(row=1, column=1)

# Create a combobox
cb = ttk.Combobox(frame, textvariable="Choose code type: ",values=["Python", "C#", "Java", "C++", "C"]).grid(row=1, column=0)

# Create a checkbox
chb = ttk.Checkbutton(frame, text="Check me!").grid(row=2, column=0)
chb2 = ttk.Checkbutton(frame, text="Check me 2!").grid(row=2, column=1)
chb3 = ttk.Checkbutton(frame, text="Check me 3!").grid(row=2, column=2)

def show_off():
    ttk.Label(frame, text="May Lindenberg").grid(row=0, column=1)




# Create a button
btn = ttk.Button(frame, text="Quit", command=quit).grid(row=5, column=5)
btn = ttk.Button(frame, text="Showoff", command=show_off).grid(row=5, column=4)


btn = ttk.Button(frame, text="Get value", command=get_value).grid(row=5, column=3)

root.mainloop()

