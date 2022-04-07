import os
import sys
from tkinter import *
import tkinter.ttk as ttk


#import для телеофна
# если вы это видите, git работает. просто тест. ничего подозрительного... пока что

root = Tk()
top_Frame = Frame(root, bg="#505050")
top_Frame.place(x=0, y=0, anchor="nw", width=320, height=20)
canvas = Canvas(root)

class Grip:
    ''' Makes a window dragable. '''
    def __init__ (self, parent, disable=None, releasecmd=None) :
        self.parent = parent
        self.root = parent.winfo_toplevel()

        self.disable = disable
        if type(disable) == 'str':
            self.disable = disable.lower()

        self.releaseCMD = releasecmd

        self.parent.bind('<Button-1>', self.relative_position)
        self.parent.bind('<ButtonRelease-1>', self.drag_unbind)

    def relative_position (self, event) :
        cx, cy = self.parent.winfo_pointerxy()
        geo = self.root.geometry().split("+")
        self.oriX, self.oriY = int(geo[1]), int(geo[2])
        self.relX = cx - self.oriX
        self.relY = cy - self.oriY

        self.parent.bind('<Motion>', self.drag_wid)

    def drag_wid (self, event) :
        cx, cy = self.parent.winfo_pointerxy()
        d = self.disable
        x = cx - self.relX
        y = cy - self.relY
        if d == 'x' :
            x = self.oriX
        elif d == 'y' :
            y = self.oriY
        self.root.geometry('+%i+%i' % (x, y))

    def drag_unbind (self, event) :
        self.parent.unbind('<Motion>')
        if self.releaseCMD is not None:
            self.releaseCMD()

def maildef():
    m = Toplevel(root)
    m.geometry('350x320')
    mcan = Canvas(m)
    grip4 = Grip(mcan)
    mcan.create_rectangle(0, 0, 350, 45,
                          fill="#49796b")
    mcan.create_rectangle(0, 45, 350, 320,
                          fill='#333333')
    mcan.pack(fill=BOTH, expand=1)
    m.resizable(False, False)
    m.overrideredirect(True)
    m.geometry('+500+200')

    mclose = Button(m, text='x', font=('Comfortaa', 11, 'bold'), command=lambda: m.destroy(), bg='#49796b',
                    borderwidth=0)
    mclose.place(x=325, y=2)

    adentry = Entry(m, width=30)
    adentry.insert(0, 'Адрес..')
    adentry.place(x=5, y=15)
    a = adentry.get()

    adentry1 = Button(m,text = 'Старт')

    adentry1.place(x=200, y=15)


    

    def mailproc(u):
        u = adentry.get()
        dmp1 = 'python email2phone/email2phonenumber.py scrape -e '
        dmp2 = str(u)



        m6 = dmp1 + dmp2

        scrollbar = Scrollbar(m)
        scrollbar.pack(side=RIGHT, fill=Y)

        mprocess = Listbox(m, yscrollcommand=scrollbar.set, width=100, height=100)
        mprocess.delete(0, END)
        doutput = os.popen(m6).readlines()
        for i in doutput:
            mprocess.insert(END, i)

        mprocess.place(x=0, y=45)
        scrollbar.config(command=mprocess.yview)

    mgo = Button(m, text='Старт', command=lambda: mailproc(a))
    mgo.place(x=200, y=13)


def ddosdef():
    d = Toplevel(root)
    d.geometry('200x120')
    dcan = Canvas(d)
    grip3 = Grip(dcan)
    dcan.create_rectangle(0, 0, 400, 45,
                            fill="#49796b")
    dcan.create_rectangle(0, 45, 400, 320,
                            fill='#333333')
    dcan.pack(fill=BOTH, expand=1)
    d.resizable(False,False)
    d.overrideredirect(True)
    d.geometry('+500+200')

    dtitle = Label(d,text = 'DDOS-атака', font = ('Comfortaa', 16, 'bold'), bg='#49796b')
    dtitle.place(x=5,y=2)

    dclose = Button(d, text='x', font=('Comfortaa', 11, 'bold'), command=lambda: d.destroy(), bg='#49796b',
                   borderwidth=0)
    dclose.place(x=175, y=2)

    adentry = Entry(d, width = 30)
    adentry.insert(0, 'IP-адрес..')
    adentry.place(x=5,y=50)


    #adentry1 = Entry(d,width = 15)
    #adentry1.insert(0, 'Порт..')   Упрощение работы юзера. дефолтный порт = 80.
    #adentry1.place(x= 200, y =15)


    def ddosproc():
        u = adentry.get()

        dp1 = 'python ddos/hammer.py -s '
        dp2 = str(u)

        dp6=dp1+dp2
        d7 = "start cmd /c " + dp6

        dscrollbar = Scrollbar(d)
        dscrollbar.pack(side=RIGHT, fill=Y)

        dprocess = Listbox(d, yscrollcommand=dscrollbar.set, width=100, height=100)
        dprocess.delete(0, END)
        #output = os.popen(dp6).readlines()
        #for i in output:   Старая реализация
        #    dprocess.insert(END, i)
        os.system(d7)
        dprocess.place(x=0, y=45)
        dscrollbar.config(command=dprocess.yview)

    dgo = Button(d, text='Старт', command=lambda: ddosproc())
    dgo.place(x=5, y=75)

def phonedef():
    pre = Toplevel(root)
    pre.geometry('350x320')
    precan = Canvas(pre)
    grip2 = Grip(precan)
    precan.create_rectangle(0, 0, 350, 45,
                            fill="#49796b")
    precan.create_rectangle(0,45,350,320,
                            fill='#333333')
    precan.pack(fill=BOTH, expand=1)
    pre.resizable(False,False)
    pre.overrideredirect(True)
    pre.geometry('+500+200')


    close = Button(pre,text = 'x',font = ('Comfortaa', 11, 'bold'), command = lambda : pre.destroy(), bg='#49796b',borderwidth=0)
    close.place(x=325,y=1)

    entry = Entry(pre, width=30)
    entry.insert(0, 'Ввод...')
    entry.place(x=5,y=15)
    a = entry.get()

    def phoneproc(a):
        a = entry.get()
        p1 = 'python phoneinf/phoneinfoga.py -n '
        p2 = str(a)
        p3 = p1 + p2

        scrollbar = Scrollbar(pre)
        scrollbar.pack(side=RIGHT, fill=Y)

        process= Listbox(pre,yscrollcommand=scrollbar.set, width = 80, height = 100)
        process.delete(0,END)
        output  = os.popen(p3).readlines()
        for i in output:
            process.insert(END,i)



        process.place(x=0,y=45)
        scrollbar.config(command=process.yview())

    go = Button(pre,text = 'Старт', command = lambda : phoneproc(a))
    go.place(x=200,y=13)

style = ttk.Style(root)
root.tk.call('source', 'src1/azure.tcl')
style.theme_use('azure')
style.configure("Accentbutton", foreground='white')
style.configure("Togglebutton", foreground='white')

canvas.create_rectangle(0, 0, 250, 45,
             fill="#49796b")
canvas.create_rectangle(0,45,250,320,
             fill='#333333')
canvas.pack(fill=BOTH, expand=1)

root.title('Nebula by Lap.')
root.geometry('250x320')
root.geometry('+200+200')
root.resizable(False,False)
#root.wm_attributes('-toolwindow', 1)
root.overrideredirect(True)
grip = Grip(canvas)
closebtn = Button(canvas,text = 'x',font = ('Comfortaa', 11, 'bold'), command = lambda : root.destroy(), bg='#49796b', borderwidth=0)
closebtn.place(x=225,y=2)

title = Label(canvas,text = 'Nebula', font = ('Comfortaa', 16, 'bold'), bg='#49796b')
title.place(x=5,y=2)

ver = Label(canvas,text = ' v. 0.1.1', font=('Comic 14 bold italic'), bg='#49796b', fg='#91aea6').place(x=90,y=10)

cred= Label(text = 'от Лэпа с любовью.', font = ('Comic 8 italic'))
cred.place(x=5,y=300)

phoneimg = PhotoImage(file = 'src2/phone.png')
ddosimg = PhotoImage(file = 'src2/ddos.png')
mailimg = PhotoImage(file = 'src2/mail.png')


phoneprob = Button(canvas,image=phoneimg,borderwidth=0, command = lambda : phonedef()).place(x=0,y=50)
ddosprob = Button(canvas,image = ddosimg, borderwidth=0, command = lambda : ddosdef()).place(x=0,y=100)
mailprob = Button(canvas,image= mailimg, borderwidth = 0, command = lambda :maildef()).place(x=0,y=150)

root.attributes('-topmost', True)



root.mainloop()