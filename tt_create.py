from tkinter import *
import random
import time


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
    global lessons
    lessons[a] = {}
    f = open('данные\\' + a + '.txt', encoding='utf-8')
    ft = ''.join([i for i in f])
    ft = ft.split('@')
    for i in ft:
        lessons[a][tuple(i.split('#')[0].split(), )] = i.split('#')[1]
    for i in lessons[a]:
        lessons[a][i] = lessons[a][i].split('\n')
        while lessons[a][i].count(''):
            lessons[a][i].pop(lessons[a][i].index(''))
        for z in range(len(lessons[a][i])):
            lessons[a][i][z] = lessons[a][i][z].split('\t')
    f.close()


# this unites previous two procedures
def read():
    global timetable, priority, c, lessons
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


# this evaluates the timetable
def evaluate(ttl):
    summa  = 0
    for i in ttl:
        for z in range(len(i)):
            for q in range(len(i[z])):
                if i[z][q]:
                    summa += priority[search(i[z][q][0])][2]*int(lessons[i[z][q][0]][i[z][q][1]][z][q])
    return int(summa)


# this generates random timetable
def rangenerate():
    start = time.time()
    ttable = [[[[] for z in range(6)] for i in range(5)] for j in range(6)]
    for i in lessons:
        for z in lessons[i]:
            if ptt[int(z[1]) - 6]:
                index = ptt[int(z[1]) - 6][random.randint(0, len(ptt[int(z[1]) - 6])-1)]
                try:
                    while (ttable[0][int(index[0])][int(index[1])][0] == i)\
                            or (ttable[1][int(index[0])][int(index[1])][0] == i)\
                            or (ttable[2][int(index[0])][int(index[1])][0] == i)\
                            or (ttable[3][int(index[0])][int(index[1])][0] == i)\
                            or (ttable[4][int(index[0])][int(index[1])][0] == i)\
                            or (ttable[5][int(index[0])][int(index[1])][0] == i):
                        index = ptt[int(z[1]) - 6][random.randint(0, len(ptt[int(z[1]) - 6]) - 1)]
                        if time.time() - start > 3:
                            return []
                except IndexError:
                    pass
                ptt[int(z[1])-6].pop(ptt[int(z[1])-6].index(index))
                # index = ptt[int(z[1]) - 6].pop(random.randint(0, len(ptt[int(z[1]) - 6]) - 1))
                ttable[int(z[1]) - 6][int(index[0])][int(index[1])] = [i, z]
            else:
                c.create_text(10, 10, text='не удалось составить расписание')
                return []
    return ttable


# this searches teacher in priority
def search(name):
    global priority
    for i in range(len(priority)):
        if priority[i][0] == name:
            return i


# this draws timetable
def draw(ttl):
    global c, timetable, convenience
    x = timetable.winfo_screenwidth()
    w = (x - 200) // 6
    for i in range(len(ttl)):
        for z in range(len(ttl[i])):
            for q in range(len(ttl[i][z])):
                if not ttl[i][z][q]:
                    c.create_rectangle(30 + w * i, 60 + 30 * q + 50 * q * 5 + 50 * z, 30 + w * (i + 1),
                                       60 + 30 * q + 50 * q * 5 + 50 * (z + 1), fill='#dddddd')
                else:
                    color = priority[search(ttl[i][z][q][0])][1]
                    c.create_rectangle(30 + w * i, 60 + 30 * q + 50 * q * 5 + 50 * z, 30 + w * (i + 1),
                                       60 + 30 * q + 50 * q * 5 + 50 * (z + 1),
                                       fill=color)
                    center = ((60 + w * (2*i + 1))//2, (100 * q * 5 + 50 * z + 120 + 60 * q + 50 * (z + 1))//2)
                    c.create_text(center[0], center[1], text=ttl[i][z][q][1][0] + '       ' + ttl[i][z][q][0],
                                  font='Arial 10')
                    c.create_text(200, 1750, text='удобство расписания: ' + str(convenience), font='Arial15')


# this creates window with timetable
def tt():
    global timetable, c, convenience
    timetable = Toplevel()
    timetable.title('Расписание')
    x = timetable.winfo_screenwidth()
    y = timetable.winfo_screenheight()
    timetable.geometry(str(x - 120) + 'x' + str(y - 120) + '+30+30')
    frame = Frame(timetable, width=x - 120, height=y - 120)
    frame.pack()
    c = Canvas(frame, width=x - 140, height=10000, bg='#aaaaaa', scrollregion=(0, 0, 1000, 2000))
    s = Scrollbar(frame)
    c.config(yscrollcommand=s.set)
    s.config(command=c.yview)
    c.pack(side='left')
    s.pack(fill='y', expand=True)
    read()
    ttbl = rangenerate()
    convenience = evaluate(ttbl)
    if ttbl:
        draw(ttbl)


convenience = 0
lessons = {}
priority = []
ptt = []
for i in range(6):
    ptt.append([])
    for z in '0234':
        for j in '012345':
            ptt[i].append(z + j)
if __name__ == '__main__':
    tt()
    print(lessons)
