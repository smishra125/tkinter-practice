from tkinter import *

fields = ("Loan Amount", "Number of Installments", "Rate of Interest", "Installment")


def calculate_installments(entries):
    r = (float(entries[fields[2]].get())/100)/12
    p = float(entries[fields[0]].get())
    n = float(entries[fields[1]].get())
    i = p*r*(1+r)**n / ((1+r)**n - 1)
    i = (" %8.2f" % i).strip()
    entries[fields[3]].delete(0, END)
    entries[fields[3]].config(state=NORMAL)
    entries[fields[3]].insert(0, i)
    entries[fields[3]].config(state=DISABLED)
    cheer.config(text="Good luck")


def makeform(screen, fields):
    entries = {}
    for field in fields:
        row = Frame(screen)
        lab = Label(row, width=22, text=field+":", anchor="w")
        ent = Entry(row, fg="green", bg="yellow")
        # ent.insert(0,"0")
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT)
        entries[field] = ent
    # User should not enter the installment, so we disabled the last entry
    entries[field].config(state=DISABLED)
    return entries


def clear_field(entries):
    # entries[fields[0]].delete(0, END)
    # entries[fields[1]].delete(0, END)
    # entries[fields[2]].delete(0, END)
    entries[fields[3]].config(state=NORMAL)
    entries[fields[3]].delete(0, END)
    entries[fields[3]].config(state=DISABLED)
    cheer.config(text="")


if __name__ == '__main__':
    screen = Tk()
    screen.title("Loan Calculation")
    screen.geometry("300x300")
    screen.wm_minsize(width=400, height=600)
    screen.wm_maxsize(width=400, height=600)

    ents = makeform(screen, fields)
    b1 = Button(screen, text="Calculate Installments", command=(lambda e=ents : calculate_installments(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(screen, text="Clear", command=(lambda e=ents : clear_field(e)))
    b2.pack(side=LEFT, padx=5, pady=5)
    b3 = Button(screen, text="Exit", command=screen.quit)
    b3.pack(side=RIGHT, padx=5, pady=5)

    cheer = Label(screen, text="Exited??")
    cheer.pack(side=BOTTOM, fill=X, padx=5, pady=5)
    screen.mainloop()
