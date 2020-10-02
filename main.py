from tkinter import *
from tt_create import tt


root = Tk()
root['bg'] = '#aaaaaa'
root.title('Составитель расписания')
x = root.winfo_screenwidth()
y = root.winfo_screenheight()
root.geometry(str(x//2)+'x'+str(y//2))
b = Button(root, text='Составить расписание', command=tt, bg='#ee7777')
b.pack()


root.mainloop()
