## create a basic login form if the user enters the correct username and password
## the application will display a message "Access Granted"

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

frame = ttk.Frame(root)

frame.pack()

luser = ttk.Label(frame, text="Username:").grid(row=0, column=0)
lpass = ttk.Label(frame, text="Password:").grid(row=1, column=0)

epass = ttk.Entry(frame, width=30, show="*")
euser = ttk.Entry(frame, width=30)

def login():
    if euser.get() == "admin" and epass.get() == "admin":
        print("Access Granted")
    else:
        print("Access Denied")

euser.grid(row=0, column=1, padx=2, pady=2)
epass.grid(row=1, column=1, padx=2, pady=2)

btn = ttk.Button(frame, text="Login", command=login).grid(row=2, column=1)

root.mainloop()