from tkinter import *

screen = Tk()
screen.title("Event Management")
screen.geometry("600x100")
screen.wm_minsize(width=300, height=300)


def fun1(event):
    l1.config(text="x="+str(event.x)+" y="+str(event.y))


l1 = Label(screen, font=('calibre', 14, 'bold'), fg='blue', bg='lightblue')
l1.place(x=30, y=100)

## <Modifier-Modifier-Type detail>
screen.bind('<Shift-Control-Motion>', fun1) # by pressing shift+ctrl and move mouse to see the coordinates

screen.mainloop()
