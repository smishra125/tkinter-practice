from tkinter import *

screen = Tk()
screen.title("Event Management")
screen.geometry("600x100")
screen.wm_minsize(width=300, height=300)


def msg1():
    l1.config(text='Sr. Engineer is selected')


def msg2():
    l1.config(text='Jr. Engineer is selected')


l1 = Label(screen, text='Job Profile', font=('calibre', 14, 'bold'), fg='gray', bg='lightblue')
l1.place(x=200, y=30)

b1 = Button(screen, text='Senior Engineer', command=msg1)
b2 = Button(screen, text='Junior Engineer', command=msg2)
b1.config(borderwidth=3, relief="solid")
b2.config(borderwidth=3, relief="solid")

b1.place(x=80, y=200, width=200, height=40)
b2.place(x=380, y=200, width=200, height=40)

screen.mainloop()
