from tkinter import *
from tkinter.messagebox import *

screen = Tk()
screen.title("Event Management")
screen.geometry("600x100")
screen.wm_minsize(width=500, height=500)

# To show some information, it returns ok
# showinfo("Information", "This is a message box")

# To show error message, it returns ok
showerror("Error", "You must be python programmer")

# To show warning messages, it returns ok
# showwarning("Warning", "This is for coders only")

# to ask true or false in place of yes or no
# askyesno("Question", "Do you like this project?")

# to ask for a retry
# askretrycancel("Retry","You have entered invalid input")

screen.mainloop()