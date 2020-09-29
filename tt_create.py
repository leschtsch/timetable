import os
from tkinter import *


def tt():
    timetable = Toplevel()
    timetable.title('Расписание')
    x = timetable.winfo_screenwidth()
    y = timetable.winfo_screenheight()
    timetable.geometry(str(x // 2) + 'x' + str(y // 2))
    return timetable

if __name__ == '__main__':
    tt()
