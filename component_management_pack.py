from tkinter import *

screen = Tk()
screen.title("Component Management")
screen.wm_minsize(width=300, height=300)
l1 = Label(screen,text='One', bg='yellow')
l2 = Label(screen,text='Two', bg='Green')
l3 = Label(screen,text='Three', bg='blue')
l4 = Label(screen,text='Four', bg='Red')

# # These pack() have side
# l1.pack(side=RIGHT)
# l2.pack(side=LEFT)
# l3.pack(side=TOP)
# l4.pack(side=BOTTOM)

# # These pack() have fill
# l1.pack(fill=X)
# l2.pack(fill=X)
# l3.pack(fill=X)
# l4.pack(fill=X)

# These pack() have padding
l1.pack(padx=10,pady=20)

# This l2 label has internal padding. i in ipadx stands for internal padding
l2.pack(ipadx=10,ipady=20)
l3.pack(fill=X)
l4.pack(fill=X)

screen.mainloop()


