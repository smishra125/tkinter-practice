from tkinter import *

screen = Tk()
screen.title("Frame Management")
screen.geometry("500x500")
screen.wm_minsize(width=300, height=300)

f1 = Frame(screen, borderwidth=3, relief="solid")
f1.place(x=10, y=10, width=400, height=200)
l1 = Label(screen, text="Choose your color", font = ("calibre", 14, "bold"))
l1.place(x=20, y=20)
v = IntVar()
rb1 = Radiobutton(f1, text="RED", variable=v, value=1)
rb2 = Radiobutton(f1, text="Blue", variable=v, value=2)
rb3 = Radiobutton(f1, text="Green", variable=v, value=3)
rb1.place(x=50, y=60)
rb2.place(x=120, y=60)
rb3.place(x=190, y=60)

f2 = Frame(screen, borderwidth=3, relief="solid")
f2.place(x=10, y=250, width=400, height=200)
screen.mainloop()
