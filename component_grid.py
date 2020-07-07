from tkinter import *

screen = Tk()
screen.title("Component Management")
screen.wm_minsize(width=300, height=300)
l1 = Label(screen,text='One', bg='yellow')
l2 = Label(screen,text='Two', bg='Green')
l3 = Label(screen,text='Three', bg='blue')
l4 = Label(screen,text='Four', bg='Red')

# configure() is in taking width and height in character size not in pixel size.
l1.configure(width=20, height=5) # component width is changed not of column.
l1.grid(row=0,column=0)
l2.grid(row=0,column=1)
l3.grid(row=1,column=0)
l4.grid(row=1,column=1)

screen.mainloop()