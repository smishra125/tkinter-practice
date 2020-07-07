from tkinter import *

screen = Tk()
screen.title("Component Management")
screen.wm_minsize(width=300, height=300)
l1 = Label(screen,text='One', bg='yellow')
l2 = Label(screen,text='Two', bg='Green')
l3 = Label(screen,text='Three', bg='blue')
l4 = Label(screen,text='Four', bg='Red')

# We use place function to display the component. width and height are the pixel.
# From place function we can decide the component place and size also.
l1.place(x=10, y=10, width=80, height=30) # width and height is in pixel
l2.place(x=10, y=100)
l3.place(x=200, y=10)
l4.place(x=200, y=100)

screen.mainloop()
