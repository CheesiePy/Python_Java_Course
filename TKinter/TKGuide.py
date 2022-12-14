import tkinter as tk
from tkinter import ttk

"""
# Application Goal:
# 1. Create a GUI application that will allow the user to enter a name and a password
# 2. The application will then check if the user is in the database
# 3. If the user is in the database, the application will display a message "Welcome, <name>"
# 4. If the user is not in the database, the application will display a message "Access Denied"
"""


"""
The steps to create a GUI application with Tkinter:
    # 1. Create a root window - the main window of the application
    # 2. Create a frame - a container for other widgets
    # 3. Create a title for the root window
    # 4. set the size of the root window
    # 5. add nessasary widgets for the application
    # 6. call the root.mainloop() method to start the application
"""

"""
## when creating widgets:
 1. specify the parent widget (root/frame) as the first argument
 2. specify the widget's options as keyword arguments
 3. call any of the methods to configure or display the widget:
        - pack(), grid(), place()

# .pack() -  is used to pack the widgets in the window 
# .grid(row,col) -  is used to place the widgets in a table like structure in the window
# .place(x,y) -  is used to place the widgets in a specific location in the window
"""





# # root -  is the main window and its the start of any tkinter application 
root = tk.Tk()


# # add a frame
frame = ttk.Frame(root) # create a frame
frame.pack() # pack the frame into the root window

# # add a title
root.title("Login") # add a title to the root window


# # # set the size of the window (width x height)
root.geometry("300x200") # set the size of the root window (width x height)


# # # in this step we are only only adding the widgets to the window
# # # we will configure them later

# # # add a label -> username and password labels

ttk.Label(frame , text="username:").grid(row=0,column=0)

# # # add an entry -> username and password entries (use the grid method to align them next to their labels)

ttk.Entry(frame).grid(row=0,column=1, padx=2 ,pady=2)

# # # add a button -> login button and quit button

root.mainloop()




