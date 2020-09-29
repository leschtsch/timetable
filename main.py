from tkinter import *
from tt_create import tt


def t():
    global table
    table = tt()


table = Toplevel()
root = Tk()
root.title('Составитель расписания')
x = root.winfo_screenwidth()
y = root.winfo_screenheight()
root.geometry(str(x//2)+'x'+str(y//2))
b = Button(root, text='Составить расписание', command=t())
b.pack()



root.mainloop()
