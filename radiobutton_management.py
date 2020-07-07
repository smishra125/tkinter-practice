from tkinter import *

screen = Tk()
screen.title("Radio Button Management")
screen.geometry("800x600")
screen.wm_minsize(width=300, height=300)

#creating and placing a set of radio button
v = IntVar()
rb1 = Radiobutton(screen, text='male', variable=v, value=1)
rb2 = Radiobutton(screen, text='female', variable=v, value=2)
rb1.place(x=50, y=10)
rb2.place(x=50, y=30)

v1 = IntVar()
v1.set(1)
rb3 = Radiobutton(screen, text='Tea', variable=v1, value=1)
rb4 = Radiobutton(screen, text='Coffee', variable=v1, value=2)
rb3.place(x=200, y=10)
rb4.place(x=200, y=30)

# instead of radio button in circular holes , we want to make them in other style
v2 = IntVar()
# v2.set(1)
rb5 = Radiobutton(screen, text='India', variable=v2, indicator=0, value=1)
rb6 = Radiobutton(screen, text='USA', variable=v2, indicator=0, value=2)
rb5.config(bg='lightgreen')
rb6.config(bg='lightgreen')
rb5.place(x=350, y=10)
rb6.place(x=350, y=30)
screen.mainloop()
