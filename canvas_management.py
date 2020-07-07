from tkinter import *

screen = Tk()
screen.title("canvas Management")
screen.geometry("400x100")
screen.wm_minsize(width=300, height=300)

c1 = Canvas(screen, bg='gray')
c1.place(x=10, y=10, width=400, height=400)
c1.create_line(10,10,200,10, fill='yellow')
c1.create_rectangle(20,20,100,100, fill ='green', outline='red')
c1.create_oval(30,220,90,280, fill='navy', outline='white',width=2)
screen.mainloop()