from tkinter import *

screen = Tk()
screen.title("Creating sub menu")
screen.geometry("500x500")
screen.wm_minsize(width=300, height=300)


def showcity(city):
    l1.config(text=city)

def showcolor(color):
    l1.config(fg=color)


l1 = Label(screen, font=('calibre', 14, 'bold'))
l1.place(x=50, y=80)

mainmenu = Menu(screen)
screen.config(menu=mainmenu)

cityname = Menu(mainmenu)
colormenu = Menu(mainmenu)

cityname.add_command(label="Hisar", command=(lambda c="Hisar" : showcity(c)))
cityname.add_command(label="Rohtak", command=(lambda c="Rohtak" : showcity(c)))
cityname.add_command(label="Gurgaon", command=(lambda c="Gurgaon" : showcity(c)))

colormenu.add_command(label="orange", command=(lambda c="orange" : showcolor(c)))
colormenu.add_command(label="Green", command=(lambda c="green" : showcolor(c)))
colormenu.add_command(label="Red", command=(lambda c="Blue" : showcolor(c)))

mainmenu.add_cascade(label='city', menu=cityname)
mainmenu.add_cascade(label='color', menu=colormenu)

screen.mainloop()
