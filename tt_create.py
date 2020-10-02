from tkinter import *


# this is just key for list.sort()
def mysort(a):
    return a[-1]


# this reads list of teachers
def prior():
    global priority
    f = open('данные\\приоритеты.txt', encoding='utf-8')
    priority = [i.split() for i in f]
    priority.sort(key=mysort)
    priority = priority[::-1]
    for i in range(len(priority)):
        priority[i][-1] = float(priority[i][-1])
    f.close()


# this reads teachers' lessons
def create_pairs(a):
    lessons[a] = {}
    f = open('данные\\'+a+'.txt', encoding='utf-8')
    ft = ''.join([i for i in f])
    ft = ft.split('@')
    for i in ft:
        lessons[a][tuple(i.split('#')[0].split(),)] = i.split('#')[1]
    for i in lessons[a]:
        lessons[a][i] = lessons[a][i].split('\n')
        while lessons[a][i].count(''):
            lessons[a][i].pop(lessons[a][i].index(''))
            for z in range(len(lessons[a][i])):
                lessons[a][i][z] = lessons[a][i][z].split('\t')
    print(lessons)

    f.close()


# this unites previous two procedures
def read():
    global timetable, priority, c
    prior()
    f = open('данные\\приоритеты.txt', 'w', encoding='utf-8')
    for i in priority:
        print('\t'.join(map(str, i)), file=f)
    f.close()
    try:
        for i in priority:
            create_pairs(i[0])
    except FileNotFoundError:
        c.create_text(10, 10, text='не все файлы препов найдены', font='Arial50', fill='#f00000', anchor='nw')


# this creates window with timetable
def tt():
    timetable = Toplevel()
    timetable.title('Расписание')
    x = timetable.winfo_screenwidth()
    y = timetable.winfo_screenheight()
    timetable.geometry(str(x // 2) + 'x' + str(y // 2))
    c = Canvas(timetable, bg='#aaaaaa')
    c.pack(fill='both', expand=True)
    read()


lessons = {}
priority = []


if __name__ == '__main__':
    tt()
    print(lessons, priority, sep='\n')
