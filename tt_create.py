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
    global lessons
    lessons[a] = {}
    f = open('данные\\' + a + '.txt', encoding='utf-8')
    ft = ''.join([i for i in f])
    ft = ft.split('@')
    for i in ft:
        lessons[a][tuple(i.split('#')[0].split('\t'), )] = i.split('#')[1]
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
    summa = 0
    for i in ttl[1]:
        for z in range(len(i)):
            for q in range(len(i[z])):
                if i[z][q]:
                    summa += priority[search(i[z][q][0])][2] * int(ttl[0][i[z][q][0]][i[z][q][1]][z][q])
    return int(summa)


# this searches teacher in priority
def search(name):
    global priority
    for i in range(len(priority)):
        if priority[i][0] == name:
            return i


# this searches maximum wanted lesson
def search_max(a):
    m = -10
    for i in a:
        for z in i:
            try:
                if int(z) > m:
                    m = int(z)
            except TypeError:
                pass
    return str(m)


# this is copy for ttable from addd
def tt_copy(ttable):
    r = [lessons_copy(ttable[0]), []]
    for i in range(len(ttable[1])):
        r[1].append([])
        for z in range(len(ttable[1][i])):
            r[1][i].append(ttable[1][i][z].copy())
    return r


# this is a part of generate
def addd(a, i, z):
    res = []
    m = search_max(a[0][i][z])
    flag = True
    while flag:
        if int(m) < -5:
            return []
        for q in range(len(a[0][i][z])):
            for x in range(len(a[0][i][z][q])):
                if (a[0][i][z][q][x] == m) and (not a[1][int(z[1]) - 6][q][x]):
                    if ((not a[1][0][q][x]) or (a[1][0][q][x][0] != i)) and (
                            (not a[1][1][q][x]) or (a[1][1][q][x][0] != i)) and (
                            (not a[1][2][q][x]) or (a[1][2][q][x][0] != i)) and (
                            (not a[1][3][q][x]) or (a[1][3][q][x][0] != i)) and (
                            (not a[1][4][q][x]) or (a[1][4][q][x][0] != i)) and (
                            (not a[1][5][q][x]) or (a[1][5][q][x][0] != i)):
                        a2 = tt_copy(a)
                        a2[1][int(z[1]) - 6][q][x] = [i, z]
                        res.append(a2)
                        flag = False
        m = str(int(m) - 1)
    if flag:
        return []
    return res


# this is list.copy() for lessons
def lessons_copy(lessons):
    r = {}
    for i in lessons:
        r[i] = {}
        for z in lessons[i]:
            r[i][z] = []
            for q in lessons[i][z]:
                r[i][z].append(q.copy())
    return r


# this uses normal generation
def generate():
    global lessons
    flag = False
    ttable = [[[[] for z in range(6)] for i in range(5)] for j in range(6)]
    lessons2 = lessons_copy(lessons)
    ttables = [[lessons_copy(lessons), ttable]]
    while lessons2:
        ttables2 = []
        i = list(lessons2.keys())[0]
        z = list(lessons2[i].keys())[0]
        for q in ttables:
            n = addd(q, i, z)
            if n:
                ttables2.extend(n)
                flag = True
        if not flag:
            return []
        ttables = ttables2
        lessons2[i].pop(z)
        if not lessons2[i]:
            lessons2.pop(i)
        ttables.sort(key=evaluate)
        while len(ttables) > 5:
            ttables.pop(0)
    return ttables


# this draws timetable
def draw(ttl, conven):
    global c, timetable
    x = timetable.winfo_screenwidth()
    w = (x - 200) // 6
    for i in range(len(ttl[1])):
        for z in range(len(ttl[1][i])):
            for q in range(len(ttl[1][i][z])):
                if not ttl[1][i][z][q]:
                    c.create_rectangle(30 + w * i, 60 + 30 * q + 50 * q * 5 + 50 * z, 30 + w * (i + 1),
                                       60 + 30 * q + 50 * q * 5 + 50 * (z + 1), fill='#dddddd')
                else:
                    color = priority[search(ttl[1][i][z][q][0])][1]
                    c.create_rectangle(30 + w * i, 60 + 30 * q + 50 * q * 5 + 50 * z, 30 + w * (i + 1),
                                       60 + 30 * q + 50 * q * 5 + 50 * (z + 1),
                                       fill=color)
                    center = ((60 + w * (2 * i + 1)) // 2, (100 * q * 5 + 50 * z + 120 + 60 * q + 50 * (z + 1)) // 2)
                    c.create_text(center[0], center[1], text=ttl[1][i][z][q][1][0] + '       ' + ttl[1][i][z][q][0],
                                  font='Arial 10')
                    c.create_text(200, 1750, text='удобство расписания: ' + str(conven), font='Arial15')


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
    ttbl = generate()
    if ttbl:
        ttbl = ttbl[0]
        convenience = evaluate(ttbl)
        draw(ttbl, convenience)
    else:
        c.create_text(10, 10, text='не удалось составить расписание')
        c.c


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
