from tkinter import *

screen = Tk()
screen.title("Event Management")
screen.geometry("600x100")
screen.wm_minsize(width=300, height=300)


def sum():
    a = int(e1.get())  # e1.get() return string
    b = int(e2.get())
    s = a+b
    l3.config(text="Sum of %d and %d is %d" % (a, b, s))


l1 = Label(screen, text='First Number', font=('calibre', 14, 'bold'), fg='orange', bg='lightblue')
l1.place(x=30, y=100)

l2 = Label(screen, text='Second Number', font=('calibre', 14, 'bold'), fg='orange', bg='lightblue')
l2.place(x=30, y=150)

e1 = Entry(screen, borderwidth=3, relief="solid")
e2 = Entry(screen, borderwidth=3, relief="solid")
e1.place(x=250, y=100)
e2.place(x=250, y=150)

b1 = Button(screen, text='Sum', command=sum)
b1.place(x=150, y=200)

l3 = Label(screen, text='Result will be shown here', font=('calibre', 14, 'bold'), fg='green', bg='white')
l3.place(x=50, y=250)

screen.mainloop()

