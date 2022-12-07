import tkinter as tk
from tkinter import ttk

class TkClass:
    def __init__(self, title, width, height):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{height}')
        self.root.resizable(True, True)
        self.center_window(width, height)

        self.label = tk.Label(self.root, text="Your Message").grid(row=0, column=0)

        self.text = tk.Text(self.root, width=30, height=10)
    
        self.check  = tk.Checkbutton(self.root, text="Show Messagebox").grid(row=2, column=0)
        
        self.button = tk.Button(self.root, text="Show Message", command=self.show_message).grid(row=5, column=5)
        
        self.root.mainloop()

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width/2 - width / 2)
        center_y = int(screen_height/2 - height / 2)
        self.root.geometry(f'{width}x{height}+{center_x}+{center_y}')

    def show_message(self):
        pass
        
        


TkClass("TkClass", 500, 500)