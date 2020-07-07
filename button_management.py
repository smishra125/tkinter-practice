from tkinter import *

screen = Tk()
screen.title("Button Management")
screen.geometry("800x600")
screen.wm_minsize(width=600, height=300)
b1 = Button(screen, text="Add")
b1.place(x=10, y=10, height=30, width=200)

b2 = Button(screen, text="Subtract")
b2.place(x=400, y=10, height=30, width=200)

# in this, height and width are in characters. height and width are in pixels only when used with place()
b3 = Button(screen, text="Multiply", height=3, width=10)
b3.place(x=10, y=100)

# font(font name, font size, style)
b4 = Button(screen, text="Divide", bg='yellow', fg='navy', font=('calibre', 16, 'bold'))
b4.place(x=400, y=100, height=30, width=200)

#set image, border width, border style
pic = PhotoImage(file='/home/shubham/Pictures/car.gif')
l1 = Label(screen, borderwidth=3, relief="solid", text="Show image", fg="red", image=pic,compound=CENTER)
l1.place(x=20, y=300, height=30, width=200)
screen.mainloop()
