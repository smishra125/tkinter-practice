from tkinter import *

screen = Tk()
screen.title("Entry Management")
screen.geometry("800x600")
screen.wm_minsize(width=600, height=300)

e1 = Entry(screen)
e1.place(x=10, y=10)

# creating, placing, sizing, font, color, border
e2 = Entry(screen,font=('calibre', 16), fg='maroon', bg='orange')
e2.config(borderwidth=3, relief="solid")
e2.place(x=10, y=40)

# creating entry with default text and editable
e3 = Entry(screen)
e3.insert(0,'Enter your text')
e3.place(x=10,y=100)

# creating entry with default text and non editable
e4 = Entry(screen)
e4.insert(0,'shubham')
e4.insert(8,' ')
e4.insert(9,'Mishra')
e4.config(state=DISABLED)
e4.place(x=10,y=100)

# Check box setting
cb1 = Checkbutton(screen)
cb1.place(x=10,y=200)

# Creating bordered and captioned checkbox
cb2 = Checkbutton(screen,text='tick')
cb2.config(borderwidth=3, relief="solid")
cb2.place(x=10,y=200)

# Creating bordered and captioned checkbox
cb3 = Checkbutton(screen,text='Already selected')
cb3.select()
cb3.config(bg='gray')
cb3.place(x=10,y=250)
screen.mainloop()
