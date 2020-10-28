from tkinter import *
from tt_create import tt


root = Tk()
root['bg'] = '#aaaaaa'
root.title('Составитель расписания')
root.geometry('640x360+10+10')
b = Button(root, text='Составить расписание', command=tt, bg='#ee7777')
b.pack()


root.mainloop()
