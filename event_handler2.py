from tkinter import *

screen = Tk()
screen.title("Event Management")
screen.geometry("600x100")
screen.wm_minsize(width=300, height=300)

def setcolor():
    c = ['red', 'green', 'blue']
    # As v1.get() returns 1 by default that's why subtracted by 1.
    # v1.get() returns the value of the radio button
    e1.config(fg=c[v1.get()-1])
    if( v1.get()==1 ):
        e1.insert(0, "Tea it is")
        # e1.config(state=DISABLED)

    elif(v1.get() == 2):
        e1.insert(0, "Coffee it is")
        # e1.config(state=DISABLED)

    else:
        e1.insert(0, 'Cold Drink it is')
        # e1.config(state=DISABLED)


l1 = Label(screen, text='What do you like?', font=('calibre', 14, 'bold'), fg='gray', bg='lightblue')
l1.place(x=50, y=40)

v1 = IntVar()
v1.set(0)
rb1 = Radiobutton(screen, text='Tea', fg='Red', variable=v1, value=1, command=setcolor)
rb2 = Radiobutton(screen, text='Coffee', fg='green', variable=v1, value=2, command=setcolor)
rb3 = Radiobutton(screen, text='Cold Drink', fg='blue', variable=v1, value=3, command=setcolor)

rb1.place(x=50, y=80, width=80)
rb2.place(x=150, y=80, width=80)
rb3.place(x=250, y=80, width=100)

l2 = Label(screen, text='What is your priority', font=('calibre', 14, 'bold'), fg='gray', bg='lightblue')
l2.place(x=50, y=150)
e1 = Entry(screen, borderwidth=3, relief="solid")
e1.place(x=50, y=200)
screen.mainloop()
