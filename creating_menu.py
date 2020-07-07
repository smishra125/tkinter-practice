from tkinter import *

screen = Tk()
screen.title("Event Management")
screen.geometry("600x500")
screen.wm_minsize(width=500, height=500)

def showname():
    l1.config(text="Shubham Mishra")

def showcity():
    l1.config(text="Hisar")

def mobile():
    l1.config(text="905478452")

l1 = Label(screen, font=('calibre', 14, 'bold'), fg='blue')
l1.place(x=50, y=100)

mainmenu = Menu(screen)
screen.config(menu=mainmenu)
mainmenu.add_command(label="Name", command=showname)
mainmenu.add_command(label="City", command=showcity)
mainmenu.add_command(label="Mobileno.", command=mobile)

screen.mainloop()
