from tkinter import *
import re


# this generates timetable, etc.
def imp():
    import tt_create


# this splits #rrggbb into integers
def colorsplit(c, a):
    res = '0x' + c[1 + a * 2:3 + a * 2]
    if res[-1] == 'x':
        res += '0'
    return int(res, 16)


# this converts strings to color
def stringtocolor(r, g, b):
    res = '#'
    if r:
        res += str(hex(int(r)))[2:]
    else:
        res += '00'
    if len(res) < 3:
        res = '#0' + res[-1]
    if g:
        res += str(hex(int(g)))[2:]
    else:
        res += '00'
    if len(res) < 5:
        res = res[:3] + '0' + res[-1]
    if b:
        res += str(hex(int(b)))[2:]
    else:
        res += '00'
    if len(res) < 7:
        res = res[:5] + '0' + res[-1]
    return res


# settings
def settings():
    global lengen, lenshow, bgcolor, btcolor, tcolor, lengenn, lenshown, bgcolorn, btcolorn, tcolorn

    # this updates settings from entries
    def settings_entry_upd(argument_that_is_not_used):
        global lengen, lenshow, bgcolor, btcolor, tcolor, lengenn, lenshown, bgcolorn, btcolorn, tcolorn
        st = bgr.get()
        if not st:
            pass
        elif not st.isdigit():
            bgr.delete(0, last=len(bgr.get()))
            bgr.insert(0, '0')
        elif int(st) > 255:
            bgr.delete(0, last=len(bgr.get()))
            bgr.insert(0, '255')
        elif int(st) < 0:
            bgr.delete(0, last=len(bgr.get()))
            bgr.insert(0, '0')
        st = bgg.get()
        if not st:
            pass
        elif not st.isdigit():
            bgg.delete(0, last=len(bgg.get()))
            bgg.insert(0, '0')
        elif int(st) > 255:
            bgg.delete(0, last=len(bgg.get()))
            bgg.insert(0, '255')
        elif int(st) < 0:
            bgg.delete(0, last=len(bgg.get()))
            bgg.insert(0, '0')
        st = bgb.get()
        if not st:
            pass
        elif not st.isdigit():
            bgb.delete(0, last=len(bgb.get()))
            bgb.insert(0, '0')
        elif int(st) > 255:
            bgb.delete(0, last=len(bgb.get()))
            bgb.insert(0, '255')
        elif int(st) < 0:
            bgb.delete(0, last=len(bgb.get()))
            bgb.insert(0, '0')
        st = btr.get()
        if not st:
            pass
        elif not st.isdigit():
            btr.delete(0, last=len(btr.get()))
            btr.insert(0, '0')
        elif int(st) > 255:
            btr.delete(0, last=len(btr.get()))
            btr.insert(0, '255')
        elif int(st) < 0:
            btr.delete(0, last=len(btr.get()))
            btr.insert(0, '0')
        st = btg.get()
        if not st:
            pass
        elif not st.isdigit():
            btg.delete(0, last=len(btg.get()))
            btg.insert(0, '0')
        elif int(st) > 255:
            btg.delete(0, last=len(btg.get()))
            btg.insert(0, '255')
        elif int(st) < 0:
            btg.delete(0, last=len(btg.get()))
            btg.insert(0, '0')
        st = btb.get()
        if not st:
            pass
        elif not st.isdigit():
            btb.delete(0, last=len(btb.get()))
            btb.insert(0, '0')
        elif int(st) > 255:
            btb.delete(0, last=len(btb.get()))
            btb.insert(0, '255')
        elif int(st) < 0:
            btb.delete(0, last=len(btb.get()))
            btb.insert(0, '0')
        st = tr.get()
        if not st:
            pass
        elif not st.isdigit():
            tr.delete(0, last=len(tr.get()))
            tr.insert(0, '0')
        elif int(st) > 255:
            tr.delete(0, last=len(tr.get()))
            tr.insert(0, '255')
        elif int(st) < 0:
            tr.delete(0, last=len(tr.get()))
            tr.insert(0, '0')
        st = tg.get()
        if not st:
            pass
        elif not st.isdigit():
            tg.delete(0, last=len(tg.get()))
            tg.insert(0, '0')
        elif int(st) > 255:
            tg.delete(0, last=len(tg.get()))
            tg.insert(0, '255')
        elif int(st) < 0:
            tg.delete(0, last=len(tg.get()))
            tg.insert(0, '0')
        st = tb.get()
        if not st:
            pass
        elif not st.isdigit():
            tb.delete(0, last=len(tb.get()))
            tb.insert(0, '0')
        elif int(st) > 255:
            tb.delete(0, last=len(tb.get()))
            tb.insert(0, '255')
        elif int(st) < 0:
            tb.delete(0, last=len(tb.get()))
            tb.insert(0, '0')
        bgcolorn = stringtocolor(bgr.get(), bgg.get(), bgb.get())
        btcolorn = stringtocolor(btr.get(), btg.get(), btb.get())
        tcolorn = stringtocolor(tr.get(), tg.get(), tb.get())
        st = bgr.get()
        if st:
            bgrs.set(int(st))
        else:
            bgrs.set(0)
        st = bgg.get()
        if st:
            bggs.set(int(st))
        else:
            bggs.set(0)
        st = bgb.get()
        if st:
            bgbs.set(int(st))
        else:
            bgbs.set(0)
        st = btr.get()
        if st:
            btrs.set(int(st))
        else:
            btrs.set(0)
        st = btg.get()
        if st:
            btgs.set(int(st))
        else:
            btgs.set(0)
        st = btb.get()
        if st:
            btbs.set(int(st))
        st = tr.get()
        if st:
            trs.set(int(st))
        else:
            trs.set(0)
        st = tg.get()
        if st:
            tgs.set(int(st))
        else:
            tgs.set(0)
        st = tb.get()
        if st:
            tbs.set(int(st))
        else:
            tbs.set(0)
        f['bg'] = bgcolorn
        le1['bg'] = bgcolorn
        le1['fg'] = tcolorn
        be['bg'] = btcolorn
        be['fg'] = tcolorn
        le['bg'] = bgcolorn
        le['fg'] = tcolorn
        c['bg'] = bgcolorn

    # this updates settings from scales
    def settings_scale_upd(argument_that_is_not_used):
        global lengen, lenshow, bgcolor, btcolor, tcolor, lengenn, lenshown, bgcolorn, btcolorn, tcolorn
        bgr.delete(0, last=len(bgr.get()))
        bgr.insert(0, str(bgrs.get()))
        bgg.delete(0, last=len(bgg.get()))
        bgg.insert(0, str(bggs.get()))
        bgb.delete(0, last=len(bgb.get()))
        bgb.insert(0, str(bgbs.get()))
        btr.delete(0, last=len(btr.get()))
        btr.insert(0, str(btrs.get()))
        btg.delete(0, last=len(btg.get()))
        btg.insert(0, str(btgs.get()))
        btb.delete(0, last=len(btb.get()))
        btb.insert(0, str(btbs.get()))
        tr.delete(0, last=len(tr.get()))
        tr.insert(0, str(trs.get()))
        tg.delete(0, last=len(tg.get()))
        tg.insert(0, str(tgs.get()))
        tb.delete(0, last=len(tb.get()))
        tb.insert(0, str(tbs.get()))
        settings_entry_upd(1)

    # this saves config
    def save():
        global lengen, lenshow, bgcolor, btcolor, tcolor, lengenn, lenshown, bgcolorn, btcolorn, tcolorn
        f = open('config.txt', 'w')
        print(str(lengenn), file=f)
        print(str(lenshown), file=f)
        print(str(bgcolorn), file=f)
        print(str(btcolorn), file=f)
        print(str(tcolorn), file=f)
        lengen = lengenn
        lenshow = lenshown
        bgcolor = bgcolorn
        btcolor = btcolorn
        tcolor = tcolorn
        root['bg'] = bgcolor
        b['bg'] = btcolor
        b['fg'] = tcolor
        sett['bg'] = btcolor
        sett['fg'] = tcolor
        hellp['bg'] = btcolor
        hellp['fg'] = tcolor
        f.close()

        s.destroy()

    # this sets default settings
    def reset():
        global lengen, lenshow, bgcolor, btcolor, tcolor, lengenn, lenshown, bgcolorn, btcolorn, tcolorn
        f = open('config_defaults.txt')
        conf = [i.strip() for i in f]
        lengenn = int(conf[0])
        lenshown = int(conf[1])
        bgcolorn = conf[2]
        btcolorn = conf[3]
        tcolorn = conf[4]
        f.close()
        bgr.delete(0, last=len(bgr.get()))
        bgr.insert(0, str(colorsplit(bgcolorn, 0)))
        bgg.delete(0, last=len(bgg.get()))
        bgg.insert(0, str(colorsplit(bgcolorn, 1)))
        bgb.delete(0, last=len(bgb.get()))
        bgb.insert(0, str(colorsplit(bgcolorn, 2)))
        btr.delete(0, last=len(btr.get()))
        btr.insert(0, str(colorsplit(btcolorn, 0)))
        btg.delete(0, last=len(btg.get()))
        btg.insert(0, str(colorsplit(btcolorn, 1)))
        btb.delete(0, last=len(btb.get()))
        btb.insert(0, str(colorsplit(btcolorn, 2)))
        tr.delete(0, last=len(tr.get()))
        tr.insert(0, str(colorsplit(tcolorn, 0)))
        tg.delete(0, last=len(tg.get()))
        tg.insert(0, str(colorsplit(tcolorn, 1)))
        tb.delete(0, last=len(tb.get()))
        tb.insert(0, str(colorsplit(tcolorn, 2)))
        lg.delete(0, last=len(lg.get()))
        lg.insert(0, str(lengen))
        ls.delete(0, last=len(ls.get()))
        ls.insert(0, str(lenshow))
        settings_entry_upd(1)
        numbers_entry_upd(1)

    # this updates numbers from entries
    def numbers_entry_upd(argument_that_is_not_used):
        global lengen, lenshow, bgcolor, btcolor, tcolor, lengenn, lenshown, bgcolorn, btcolorn, tcolorn
        st = lg.get()
        if not st:
            pass
        elif not st.isdigit():
            lg.delete(0, last=len(st))
            lg.insert(0, '1')
        elif int(st) < 1:
            lg.delete(0, last=len(st))
            lg.insert(0, '1')
        elif int(st) > 20:
            lg.delete(0, last=len(st))
            lg.insert(0, '20')
        st = ls.get()
        if not st:
            pass
        elif not st.isdigit():
            ls.delete(0, last=len(st))
            ls.insert(0, '1')
        elif int(st) < 1:
            ls.delete(0, last=len(st))
            ls.insert(0, '1')
        elif int(st) > 20:
            ls.delete(0, last=len(st))
            ls.insert(0, '20')
        st = lg.get()
        if st:
            lengenn = int(st)
            lgs.set(int(st))
        else:
            lengenn = 1
            lgs.set(1)
        st = ls.get()
        if st:
            lenshown = int(st)
            lss.set(int(st))
        else:
            lenshown = 1
            lss.set(1)

    # this updates numbers from scales
    def numbers_scales_upd(argument_that_is_not_used):
        global lengen, lenshow, bgcolor, btcolor, tcolor, lengenn, lenshown, bgcolorn, btcolorn, tcolorn
        lg.delete(0, last=len(lg.get()))
        lg.insert(0, lgs.get())
        ls.delete(0, last=len(ls.get()))
        ls.insert(0, lss.get())
        numbers_entry_upd(1)

    s = Toplevel()
    s['bg'] = bgcolor
    s.title('Настройки')
    s.geometry('600x350+30+30')
    bgcolorn = bgcolor
    btcolorn = btcolor
    tcolorn = tcolor
    lengenn = lengen
    lenshown = lenshow
    bgr = Entry(s)
    bgg = Entry(s)
    bgb = Entry(s)
    bgr.insert(0, str(colorsplit(bgcolorn, 0)))
    bgg.insert(0, str(colorsplit(bgcolorn, 1)))
    bgb.insert(0, str(colorsplit(bgcolorn, 2)))
    bgr.place(x=30, y=30, height=20, width=50)
    bgg.place(x=30, y=60, height=20, width=50)
    bgb.place(x=30, y=90, height=20, width=50)
    btr = Entry(s)
    btg = Entry(s)
    btb = Entry(s)
    btr.insert(0, str(colorsplit(btcolorn, 0)))
    btg.insert(0, str(colorsplit(btcolorn, 1)))
    btb.insert(0, str(colorsplit(btcolorn, 2)))
    btr.place(x=30, y=140, height=20, width=50)
    btg.place(x=30, y=170, height=20, width=50)
    btb.place(x=30, y=200, height=20, width=50)
    tr = Entry(s)
    tg = Entry(s)
    tb = Entry(s)
    tr.insert(0, str(colorsplit(tcolorn, 0)))
    tg.insert(0, str(colorsplit(tcolorn, 1)))
    tb.insert(0, str(colorsplit(tcolorn, 2)))
    tr.place(x=30, y=250, height=20, width=50)
    tg.place(x=30, y=280, height=20, width=50)
    tb.place(x=30, y=310, height=20, width=50)
    bgr.bind('<KeyRelease>', settings_entry_upd)
    bgg.bind('<KeyRelease>', settings_entry_upd)
    bgb.bind('<KeyRelease>', settings_entry_upd)
    btr.bind('<KeyRelease>', settings_entry_upd)
    btg.bind('<KeyRelease>', settings_entry_upd)
    btb.bind('<KeyRelease>', settings_entry_upd)
    tr.bind('<KeyRelease>', settings_entry_upd)
    tg.bind('<KeyRelease>', settings_entry_upd)
    tb.bind('<KeyRelease>', settings_entry_upd)
    bgrs = Scale(s, from_=0, to=255, orient=HORIZONTAL, bg=bgcolor, showvalue=0, highlightthickness=0,
                 command=settings_scale_upd)
    bggs = Scale(s, from_=0, to=255, orient=HORIZONTAL, bg=bgcolor, showvalue=0, highlightthickness=0,
                 command=settings_scale_upd)
    bgbs = Scale(s, from_=0, to=255, orient=HORIZONTAL, bg=bgcolor, showvalue=0, highlightthickness=0,
                 command=settings_scale_upd)
    bgrs.set(colorsplit(bgcolorn, 0))
    bggs.set(colorsplit(bgcolorn, 1))
    bgbs.set(colorsplit(bgcolorn, 2))
    bgrs.place(x=100, y=30)
    bggs.place(x=100, y=60)
    bgbs.place(x=100, y=90)
    btrs = Scale(s, from_=0, to=255, orient=HORIZONTAL, bg=bgcolor, showvalue=0, highlightthickness=0,
                 command=settings_scale_upd)
    btgs = Scale(s, from_=0, to=255, orient=HORIZONTAL, bg=bgcolor, showvalue=0, highlightthickness=0,
                 command=settings_scale_upd)
    btbs = Scale(s, from_=0, to=255, orient=HORIZONTAL, bg=bgcolor, showvalue=0, highlightthickness=0,
                 command=settings_scale_upd)
    btrs.set(colorsplit(btcolorn, 0))
    btgs.set(colorsplit(btcolorn, 1))
    btbs.set(colorsplit(btcolorn, 2))
    btrs.place(x=100, y=140)
    btgs.place(x=100, y=170)
    btbs.place(x=100, y=200)
    trs = Scale(s, from_=0, to=255, orient=HORIZONTAL, bg=bgcolor, showvalue=0, highlightthickness=0,
                command=settings_scale_upd)
    tgs = Scale(s, from_=0, to=255, orient=HORIZONTAL, bg=bgcolor, showvalue=0, highlightthickness=0,
                command=settings_scale_upd)
    tbs = Scale(s, from_=0, to=255, orient=HORIZONTAL, bg=bgcolor, showvalue=0, highlightthickness=0,
                command=settings_scale_upd)
    trs.set(colorsplit(tcolorn, 0))
    tgs.set(colorsplit(tcolorn, 1))
    tbs.set(colorsplit(tcolorn, 2))
    trs.place(x=100, y=250)
    tgs.place(x=100, y=280)
    tbs.place(x=100, y=310)
    lg = Entry(s)
    lg.insert(0, str(lengen))
    lg.place(x=300, y=170, width=50, height=20)
    ls = Entry(s)
    ls.insert(0, str(lengen))
    ls.place(x=300, y=230, width=50, height=20)
    lg.bind('<KeyRelease>', numbers_entry_upd)
    ls.bind('<KeyRelease>', numbers_entry_upd)
    lgs = Scale(s, from_=1, to=20, orient=HORIZONTAL, bg=bgcolor, showvalue=0, highlightthickness=0,
                command=numbers_scales_upd)
    lgs.set(lengen)
    lgs.place(x=370, y=170)
    lss = Scale(s, from_=1, to=20, orient=HORIZONTAL, bg=bgcolor, showvalue=0, highlightthickness=0,
                command=numbers_scales_upd)
    lss.set(lenshow)
    lss.place(x=370, y=230)
    a = Label(s, text='R:', bg=bgcolor, fg=tcolor)
    a.place(x=10, y=30)
    a = Label(s, text='R:', bg=bgcolor, fg=tcolor)
    a.place(x=10, y=140)
    a = Label(s, text='R:', bg=bgcolor, fg=tcolor)
    a.place(x=10, y=250)
    a = Label(s, text='G:', bg=bgcolor, fg=tcolor)
    a.place(x=10, y=60)
    a = Label(s, text='G:', bg=bgcolor, fg=tcolor)
    a.place(x=10, y=170)
    a = Label(s, text='G:', bg=bgcolor, fg=tcolor)
    a.place(x=10, y=280)
    a = Label(s, text='B:', bg=bgcolor, fg=tcolor)
    a.place(x=10, y=90)
    a = Label(s, text='B:', bg=bgcolor, fg=tcolor)
    a.place(x=10, y=200)
    a = Label(s, text='B:', bg=bgcolor, fg=tcolor)
    a.place(x=10, y=310)
    a = Label(s, text='Фон:', bg=bgcolor, fg=tcolor)
    a.place(x=30, y=10)
    a = Label(s, text='Кнопки:', bg=bgcolor, fg=tcolor)
    a.place(x=30, y=120)
    a = Label(s, text='Текст:', bg=bgcolor, fg=tcolor)
    a.place(x=30, y=230)
    a = Label(s, text='Качество генерации:', bg=bgcolor, fg=tcolor)
    a.place(x=300, y=150)
    a = Label(s, text='Количество генерируемых расписаний:', bg=bgcolor, fg=tcolor)
    a.place(x=300, y=210)
    a = Label(s, text='Результат применения настроек:', bg=bgcolor, fg=tcolor)
    a.place(x=300, y=10)
    f = Frame(s, bg=bgcolorn, highlightthickness=5)
    f.config(highlightbackground='#ffffff', highlightcolor='#ffffff')
    le1 = Label(f, bg=bgcolorn, fg=tcolor)
    le1.pack()
    be = Button(f, text='пример кнопки', bg=btcolorn, fg=tcolor)
    be.pack()
    le = Label(f, bg=bgcolorn, text='пример текста', fg=tcolor)
    le.pack()
    c = Canvas(f, bg=bgcolor, height=30, width=200, highlightthickness=0)
    c.pack()
    f.place(x=300, y=30)
    sav = Button(s, text='сохранить', bg=btcolorn, fg=tcolor, command=save)
    sav.place(x=500, y=300)
    default = Button(s, text='по умолчанию', bg=btcolorn, fg=tcolor, command=reset)
    default.place(x=400, y=300)
    s.mainloop()


# this reads settings
def config():
    global lengen, lenshow, bgcolor, btcolor, tcolor
    try:
        f = open('config.txt')
        conf = [i.strip() for i in f]
        lengen = int(conf[0])
        lenshow = int(conf[1])
        bgcolor = conf[2]
        btcolor = conf[3]
        tcolor = conf[4]
        f.close()
        if not (re.search(r'#[1234567890abcdef]{6}', bgcolor) and re.search(r'#[1234567890abcdef]{6}',
                    btcolor) and re.search(r'#[1234567890abcdef]{6}', tcolor)):
            raise ValueError
    except ValueError:
        f = open('config_defaults.txt')
        conf = [i.strip() for i in f]
        lengen = int(conf[0])
        lenshow = int(conf[1])
        bgcolor = conf[2]
        btcolor = conf[3]
        tcolor = conf[4]
        f.close()
        f = open('config.txt', 'w')
        for i in conf:
            print(str(i), file=f)
        f.close()


# this shows help
def help_show():
    hell = Toplevel()
    hell['bg'] = bgcolor
    hell.title('Помощь')
    hell.geometry('640x360+50+50')
    t = Text(hell, bg=bgcolor, fg=tcolor, font='Arial 12', wrap=WORD)
    t.pack(fill='both', expand=True, side='left')
    f = open('help.txt', encoding='utf-8')
    st = ''
    for i in f:
        st += i
    t.insert(1.0, st)
    f.close()
    hell.mainloop()


lengen = 0
lenshow = 0
bgcolor = ''
btcolor = ''
tcolor = ''
config()
lengenn = lengen
lenshown = lenshow
bgcolorn = bgcolor
btcolorn = btcolor
tcolorn = tcolor
root = Tk()
root['bg'] = bgcolor
root.title('Составитель расписания')
root.geometry('640x360+10+10')
b = Button(root, text='Составить расписание', command=imp, bg=btcolor, fg=tcolor)
b.pack()
sett = Button(root, text='Настройки', command=settings, bg=btcolor, fg=tcolor)
sett.pack()
hellp = Button(root, text='Помощь', command=help_show, bg=btcolor, fg=tcolor)
hellp.pack()

root.mainloop()
