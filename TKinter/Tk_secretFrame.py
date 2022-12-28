import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# freme for login - start
frame = ttk.Frame(root)

frame.pack()

luser = ttk.Label(frame, text="Username:").grid(row=0, column=0)
lpass = ttk.Label(frame, text="Password:").grid(row=1, column=0)

epass = ttk.Entry(frame, width=30)
euser = ttk.Entry(frame, width=30)
# freme for login - end

# secret frame - start

secter = ttk.Frame(root)
luser = ttk.Label(secter, text="Welcome to the secret frame!").grid(row=0, column=0)


# secret frame - end

def login():
    if euser.get() == "admin" and epass.get() == "admin":
        print("Access Granted")
        frame.pack_forget() # hide the login frame
        secter.pack() # show the secret frame
    else:
        print("Access Denied")

euser.grid(row=0, column=1, padx=2, pady=2)
epass.grid(row=1, column=1, padx=2, pady=2)

btn = ttk.Button(frame, text="Login", command=login).grid(row=2, column=1)




root.mainloop()