from tkinter import *


def imp():
    import tt_create


root = Tk()
root['bg'] = '#aaaaaa'
root.title('Составитель расписания')
root.geometry('640x360+10+10')
b = Button(root, text='Составить расписание', command=imp, bg='#ee7777')
b.pack()


root.mainloop()
