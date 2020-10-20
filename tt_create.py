from tkinter import *


# this is just key for list.sort() for prior
def priority_sort(a):
    return a[-1]


# this reads list of teachers
def prior():
    global priority
    f = open('данные\\приоритеты.txt', encoding='utf-8')
    priority = [i.split() for i in f]
    priority.sort(key=priority_sort)
    priority = priority[::-1]
    for i in range(len(priority)):
        priority[i][-1] = float(priority[i][-1])
    f.close()


# this is just key for list.sort() for order
def order_sort(a):
    return priority[search(a[0][0])][2] + priority[search(a[1][0])][2]


# this creates order of pairs
def order():
    global row, after
    f = open('данные\\порядок.txt', encoding='utf-8')
    for i in f:
        a = i.split('\t')
        p1 = a[0].split()
        p2 = a[2].split()
        if a[1] == 'после':
            after.append([[p1[0], (p1[1], p1[2])], [p2[0], (p2[1], p2[2])]])
        elif a[1] == 'подряд':
            row.append([[p1[0], (p1[1], p1[2])], [p2[0], (p2[1], p2[2])]])
        else:
            c.create_text(10, 10, text='неизвестное слово:' + a[1], font='Arial50', fill='#f00000', anchor='nw')
    f.close()
    row.sort(key=order_sort)
    after.sort(key=order_sort)


# this reads teachers' lessons
def create_pairs(a):
    global lessons
    lessons[a] = {}
    f = open('данные\\' + a + '.txt', encoding='utf-8')
    ft = ''.join([i for i in f])
    ft = ft.split('@')
    for i in ft:
        ind = tuple(i.split('#')[0].split('\t'), )
        ind = (ind[0].strip('\n'), ind[1].strip('\n'))
        lessons[a][ind] = i.split('#')[1]
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
    order()


# this evaluates the timetable
def evaluate(ttl):
    summa = 0
    for i in ttl:
        for z in range(len(i)):
            for q in range(len(i[z])):
                if i[z][q]:
                    summa += priority[search(i[z][q][0])][2] * int(lessons[i[z][q][0]][i[z][q][1]][z][q])
    return int(summa)


# this searches teacher in priority
def search(name):
    global priority
    for i in range(len(priority)):
        if priority[i][0] == name:
            return i


# this is sort for orders
def order_index_sort(a, n1, n2):
    global lessons
    t1 = lessons[n1[0]][n1[1]]
    t2 = lessons[n2[0]][n2[1]]
    p1 = priority[search(n1[0])][2]
    p2 = priority[search(n2[0])][2]
    s1 = [[i] for i in a.copy()]
    s2 = []
    while len(s1) > 1:  # merge sort
        while len(s1) > 1:
            n = []
            while True:
                if int(t1[s1[0][0][0]][s1[0][0][1]]) * p1 + int(t2[s1[0][0][2]][s1[0][0][3]]) * p2 < int(
                        t1[s1[1][0][0]][s1[1][0][1]]) * p1 + int(t2[s1[1][0][2]][s1[1][0][3]]) * p2:
                    n.append(s1[0].pop(0))
                else:
                    n.append(s1[1].pop(0))
                if not len(s1[0]):
                    n.extend(s1[1])
                    break
                if not len(s1[1]):
                    n.extend(s1[0])
                    break
            s2.append(n)
            s1.pop(0)
            s1.pop(0)
        if len(s1):
            s2.append(s1[0])
        s1 = s2.copy()
        s2 = []
    return s1[0]


# this searches most wanted pair of lessons in a row
def row_search_max(a, ttbl):
    p1 = priority[search(a[0][0])][2]
    p2 = priority[search(a[1][0])][2]
    m = []
    for i in range(4):
        for z in range(6):
            if not (ttbl[int(a[0][1][1]) - 6][i][z] or ttbl[int(a[1][1][1]) - 6][i + 1][z]):
                m.append([i, z, i + 1, z])
    m = order_index_sort(m, a[0], a[1])
    if len(m) > lengen:
        m = m[-lengen:]
    return m


# this searches most wanted pair of lessons
def after_search_max(a, ttbl):
    m = []
    for i in range(len(lessons[a[0][0]][a[0][1]])):
        for z in range(len(lessons[a[0][0]][a[0][1]][i])):
            for q in range(len(lessons[a[1][0]][a[1][1]])):
                for r in range(len(lessons[a[1][0]][a[1][1]][q])):
                    if q * len(lessons[a[1][0]][a[1][1]][q]) + r > i * len(lessons[a[0][0]][a[0][1]][i]) + z:
                        if not (ttbl[int(a[0][1][1]) - 6][i][z] or ttbl[int(a[1][1][1]) - 6][q][r]):
                            m.append([i, z, q, r])
                    m = order_index_sort(m, a[0], a[1])
                    if len(m) > lengen:
                        m = m[-lengen:]
    return m


# this is copy for ttable from addd
def tt_copy(ttable):
    r = []
    for i in range(len(ttable)):
        r.append([])
        for z in range(len(ttable[i])):
            r[i].append(ttable[i][z].copy())
    return r


# this is a part of generate
def addd(a, i, z):
    global lessons
    res = []
    m = '5'
    flag = 0
    full = False
    for ii in a:
        if full:
            break
        for zz in ii:
            if full:
                break
            for q in zz:
                if full:
                    break
                if not q:
                    full = True
                if full:
                    break
    if full:
        while flag < lengen:
            if int(m) < -5:
                return []
            for q in range(len(lessons[i][z])):
                for x in range(len(lessons[i][z][q])):
                    if (lessons[i][z][q][x] == m) and (not a[int(z[1]) - 6][q][x]):
                        if ((not a[0][q][x]) or (a[0][q][x][0] != i)) and (
                                (not a[1][q][x]) or (a[1][q][x][0] != i)) and (
                                (not a[2][q][x]) or (a[2][q][x][0] != i)) and (
                                (not a[3][q][x]) or (a[3][q][x][0] != i)) and (
                                (not a[4][q][x]) or (a[4][q][x][0] != i)) and (
                                (not a[5][q][x]) or (a[5][q][x][0] != i)):
                            a2 = tt_copy(a)
                            a2[int(z[1]) - 6][q][x] = [i, z]
                            res.append(a2)
                            flag += 1
            m = str(int(m) - 1)
    if flag == 0:
        return []
    return res


# this is addd for pair of lessons
def addd_2(a, option, ttbl):
    if option == 'row':
        m = row_search_max(a, ttbl)
    elif option == 'after':
        m = after_search_max(a, ttbl)
    if not m:
        return []
    res = []
    for i in m:
        ttbln = tt_copy(ttbl)
        ttbln[int(a[0][1][1]) - 6][i[0]][i[1]] = a[0]
        ttbln[int(a[1][1][1]) - 6][i[2]][i[3]] = a[1]
        res.append(ttbln)
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
    global lessons, row, after
    ttable = [[[[] for z in range(6)] for i in range(5)] for j in range(6)]
    lessons2 = lessons_copy(lessons)
    ttables = [ttable]

    while row:   # this inserts row
        ttables2 = []
        for i in ttables:
            n = addd_2(row[0], 'row', i)
            if n:
                ttables2.extend(n)
            else:
                return []
        lessons2[row[0][0][0]].pop(row[0][0][1])
        if not lessons2[row[0][0][0]]:
            lessons2.pop(row[0][0][0])
        lessons2[row[0][1][0]].pop(row[0][1][1])
        if not lessons2[row[0][1][0]]:
            lessons2.pop(row[0][1][0])
        row.pop(0)
        ttables = ttables2
        ttables.sort(key=evaluate)
        if len(ttables) > lengen:
            ttables = ttables[-lengen:]

    while after:  # this inserts after
        ttables2 = []
        for i in ttables:
            n = addd_2(after[0], 'after', i)
            if n:
                ttables2.extend(n)
            else:
                return []
        lessons2[after[0][0][0]].pop(after[0][0][1])
        if not lessons2[after[0][0][0]]:
            lessons2.pop(after[0][0][0])
        lessons2[after[0][1][0]].pop(after[0][1][1])
        if not lessons2[after[0][1][0]]:
            lessons2.pop(after[0][1][0])
        after.pop(0)
        ttables = ttables2
        ttables.sort(key=evaluate)
        if len(ttables) > lengen:
            ttables = ttables[-lengen:]

    while lessons2:  # this inserts others
        ttables2 = []
        i = list(lessons2.keys())[0]
        z = list(lessons2[i].keys())[0]
        for q in ttables:
            n = addd(q, i, z)
            if n:
                ttables2.extend(n)
            else:
                return []
        ttables = ttables2
        lessons2[i].pop(z)
        if not lessons2[i]:
            lessons2.pop(i)
        ttables.sort(key=evaluate)
        if len(ttables) > lengen:
            ttables = ttables[-lengen:]

    return ttables


# this draws timetable
def draw(ttl, conven):
    global c, timetable
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
                    center = ((60 + w * (2 * i + 1)) // 2, (100 * q * 5 + 50 * z + 120 + 60 * q + 50 * (z + 1)) // 2)
                    tx = ttl[i][z][q][1][0] + '       ' + ttl[i][z][q][0]
                    tx.strip('\n')
                    c.create_text(center[0], center[1], text=tx, font='Arial 10')
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
        print(ttbl)
        convenience = evaluate(ttbl)
        draw(ttbl, convenience)
    else:
        c.create_text(75, 10, text='не удалось составить расписание')


convenience = 0
lessons = {}
after = []
row = []
priority = []
lengen = 5
if __name__ == '__main__':
    tt()
