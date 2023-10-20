def Addstaff():
    def submitadd():
        tsid = tsidval.get()
        tsname = tsnameval.get()
        tsquali = tsqualival.get()
        tspost = tspostval.get()
        tsage = tsageval.get()
        tssal = tssalval.get()
        tsexp = tsexpval.get()
        tsphno = tsphnoval.get()
        tsemail = tsemailval.get()
        dname = dnameval.get()
        dno = dnoval.get()
        typ = staff_type.get()
        try:
            global con
            global mycursor
            con = mysql.connector.connect(
                host='localhost', user='root', password='root', database=' staff_management_system1')
            mycursor = con.cursor()
            strr = 'insert into teaching_staff1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,
                             (tsid, tsname, tsquali, tspost, tsage, tssal, tsexp, tsphno, tsemail, dname, dno, typ))
            con.commit()
            con = mysql.connector.connect(
                host='localhost', user='root', password='root', database=' staff_management_system1')
            mycursor = con.cursor()
            strr1 = 'select * from teaching_staff1 where dno=' + str(dno)
            mycursor.execute(strr1)
            datas1 = mycursor.fetchall()
            tcount = 0
            ntcount = 0
            for i in datas1:
                if i[11] == 'Teaching':
                    tcount += 1
                elif i[11] == 'Non-Teaching':
                    ntcount += 1
            print(tcount)
            strr1 = 'update department set no_of_teaching_staff=%s ,no_of_non_teaching_staff=%s where dno=%s '
            mycursor.execute(strr1, (tcount, ntcount, dno))
            con.commit()
            res = messagebox.askyesnocancel('Notifications', 'Id Name added successfully... and want to clean the form',
                                            parent=addroot)
            if (res == True):
                tsidval.set('')
                tsnameval.set('')
                tsqualival.set('')
                tspostval.set('')
                tsageval.set('')
                tssalval.set('')
                tsexpval.set('')
                tsphnoval.set('')
                tsemailval.set('')
                dnameval.set('')
                dnoval.set('')
        except:
            print("ho")

        con = mysql.connector.connect(
            host='localhost', user='root', password='root',database=' staff_management_system1')
        mycursor = con.cursor()
        strr = 'select * from teaching_staff1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        teaching_stafftable.delete(*teaching_stafftable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
            teaching_stafftable.insert('', END, values=vv)

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('560x660+220+50')
    addroot.config(bg='black')
    addroot.resizable(False, False)
    # -----------------------------add staff lables
    tsidlabel = Label(addroot, text='Enter TS_id: ', bg='gold2', font=('times', 15), relief=GROOVE,
                      borderwidth=3, width=15, anchor='w')
    tsidlabel.place(x=10, y=10)

    tsnamelabel = Label(addroot, text='Enter TS_name: ', bg='gold2', font=('times', 15), relief=GROOVE,
                        borderwidth=3, width=15, anchor='w')
    tsnamelabel.place(x=10, y=60)

    tsqualilabel = Label(addroot, text='Enter TS_qualification: ', bg='gold2', font=('times', 15), relief=GROOVE,
                         borderwidth=3, width=15, anchor='w')
    tsqualilabel.place(x=10, y=110)

    tspostlabel = Label(addroot, text='Enter TS_post: ', bg='gold2', font=('times', 15), relief=GROOVE,
                        borderwidth=3, width=15, anchor='w')
    tspostlabel.place(x=10, y=160)

    tsagelabel = Label(addroot, text='Enter TS_age: ', bg='gold2', font=('times', 15), relief=GROOVE,
                       borderwidth=3, width=15, anchor='w')
    tsagelabel.place(x=10, y=210)

    tssalarylabel = Label(addroot, text='Enter TS_salary: ', bg='gold2', font=('times', 15), relief=GROOVE,
                          borderwidth=3, width=15, anchor='w')
    tssalarylabel.place(x=10, y=260)

    tsexplabel = Label(addroot, text='Enter TS_experince: ', bg='gold2', font=('times', 15), relief=GROOVE,
                       borderwidth=3, width=15, anchor='w')
    tsexplabel.place(x=10, y=310)

    tsphnolabel = Label(addroot, text='Enter TS_phno: ', bg='gold2', font=('times', 15), relief=GROOVE,
                        borderwidth=3, width=15, anchor='w')
    tsphnolabel.place(x=10, y=360)

    tsemaillabel = Label(addroot, text='Enter TS_email: ', bg='gold2', font=('times', 15), relief=GROOVE,
                         borderwidth=3, width=15, anchor='w')
    tsemaillabel.place(x=10, y=410)

    dnamelabel = Label(addroot, text='Enter D_name: ', bg='gold2', font=('times', 15), relief=GROOVE,
                       borderwidth=3, width=15, anchor='w')
    dnamelabel.place(x=10, y=460)

    dnolabel = Label(addroot, text='Enter D_no: ', bg='gold2', font=('times', 15), relief=GROOVE,
                     borderwidth=3, width=15, anchor='w')
    dnolabel.place(x=10, y=510)

    stafftypelabel = Label(addroot, text='Enter Staff_type:', bg='gold2', font=('times', 15), relief=GROOVE,
                           borderwidth=3, width=15, anchor='w')
    stafftypelabel.place(x=10, y=560)

    # --------------------------------------------------------------------add staff entry
    tsidval = StringVar()
    tsnameval = StringVar()
    tsqualival = StringVar()
    tspostval = StringVar()
    tsageval = StringVar()
    tssalval = StringVar()
    tsexpval = StringVar()
    tsphnoval = StringVar()
    tsemailval = StringVar()
    dnameval = StringVar()
    dnoval = StringVar()
    staff_type = StringVar()

    tsidentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=tsidval)
    tsidentry.place(x=300, y=10)

    tsnameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=tsnameval)
    tsnameentry.place(x=300, y=60)

    tsqualidentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=tsqualival)
    tsqualidentry.place(x=300, y=110)

    tspostentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=tspostval)
    tspostentry.place(x=300, y=160)

    tsageentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=tsageval)
    tsageentry.place(x=300, y=210)

    tssalentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=tssalval)
    tssalentry.place(x=300, y=260)

    tsexpentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=tsexpval)
    tsexpentry.place(x=300, y=310)

    tsphnoentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=tsphnoval)
    tsphnoentry.place(x=300, y=360)

    tsemailentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=tsemailval)
    tsemailentry.place(x=300, y=410)

    dnameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=dnameval)
    dnameentry.place(x=300, y=460)

    dnoentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=dnoval)
    dnoentry.place(x=300, y=510)

    ty = ttk.Combobox(addroot, width=19, font=('roman', 15, 'bold'), textvariable=staff_type)
    ty['values'] = ('Teaching', 'Non-Teaching')
    ty.place(x=300, y=560)

    # -----------------------------------------------------------submit
    submitbutton = Button(addroot, text='SUBMIT', font=('roman', 17, 'bold'), bg='red', bd=5, width=20,
                          activebackground='blue', activeforeground='white', command=submitadd)
    submitbutton.place(x=150, y=610)
    addroot.mainloop()


def Searchstaff():
    def submitsearch():
        t = tsidentry.get()
        d = dnoentry.get()
        typ = staff_type.get()
        print('search')
        global con, mycursor
        con = mysql.connector.connect(
            host='localhost', user='root', password='root', database=' staff_management_system1')
        mycursor = con.cursor()
        if typ == '' and t != '' and d != '':
            strr = 'select * from teaching_staff1 where tsid=%s and dno=%s '
            mycursor.execute(strr, (t, d))
        elif typ != '' and d != '' and t == '':
            strr = 'select * from teaching_staff1 where type=%s and dno=%s '
            mycursor.execute(strr, (typ, d))
        else:
            strr = 'select * from teaching_staff1 where dno='+ str(d)
            mycursor.execute(strr)

        datas = mycursor.fetchall()
        teaching_stafftable.delete(*teaching_stafftable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4],
                  i[5], i[6], i[7], i[8], i[9], i[10]]

            teaching_stafftable.insert('', END, values=vv)
        con.commit()

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('550x250+220+200')
    searchroot.config(bg='red')
    searchroot.resizable(False, False)
    # -----------------------------add staff lable
    tsidlabel = Label(searchroot, text='Enter TS_id: ', bg='gold2', font=('times', 20), relief=GROOVE,
                      borderwidth=3, width=17, anchor='w')
    tsidlabel.place(x=10, y=10)

    dnolabel = Label(searchroot, text='Enter D_no: ', bg='gold2', font=('times', 20), relief=GROOVE,
                     borderwidth=3, width=17, anchor='w')
    dnolabel.place(x=10, y=60)

    stafftypelabel = Label(searchroot, text='Enter Staff_type:', bg='gold2', font=('times', 20), relief=GROOVE,
                           borderwidth=3, width=17, anchor='w')
    stafftypelabel.place(x=10, y=110)
    # --------------------------------------------------------------------add staff entry
    tsidval = StringVar()

    dnoval = StringVar()
    staff_type = StringVar()

    tsidentry = Entry(searchroot, font=('roman', 17, 'bold'),
                      bd=5, textvariable=tsidval)
    tsidentry.place(x=300, y=10)

    dnoentry = Entry(searchroot, font=('roman', 17, 'bold'),
                     bd=5, textvariable=dnoval)
    dnoentry.place(x=300, y=60)

    ty = ttk.Combobox(searchroot, width=19, font=('roman', 17, 'bold'), textvariable=staff_type)
    ty['values'] = ('Teaching', 'Non-Teaching')
    ty.place(x=300, y=110)

    # -----------------------------------------------------------submit
    submitbutton = Button(searchroot, text='SUBMIT', font=('roman', 15, 'bold'), bg='blue', bd=5, width=25,
                          activebackground='blue', activeforeground='white', command=submitsearch)
    submitbutton.place(x=150, y=160)
    searchroot.mainloop()


def Deletestaff():
    global con, mycursor
    con = mysql.connector.connect(
        host='localhost', user='root', password='root', database=' staff_management_system1')
    mycursor = con.cursor()
    cc = teaching_stafftable.focus()
    content = teaching_stafftable.item(cc)
    print(content)
    t = content['values'][0]
    d = content['values'][10]
    strr = 'delete from teaching_staff1 where tsid=%s and dno=%s'
    mycursor.execute(strr, (d))
    con.commit()
    strr1 = 'select * from teaching_staff1 where dno=' + str(d)
    mycursor.execute(strr1)
    datas1 = mycursor.fetchall()
    tcount = 0
    ntcount = 0
    for i in datas1:
        if i[11] == 'Teaching':
            tcount += 1
        elif i[11] == 'Non-Teaching':
            ntcount += 1
    strr2 = 'update department set no_of_teaching_staff=%s ,no_of_non_teaching_staff=%s where dno=%s '
    mycursor.execute(strr2, (tcount, ntcount, d))
    con.commit()
    messagebox.showinfo(
        'Notifications', 'Id {} deleted sucessfully...'.format(t))
    strr = 'select *from teaching_staff1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    teaching_stafftable.delete(*teaching_stafftable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4],
              i[5], i[6], i[7], i[8], i[9], i[10]]
        teaching_stafftable.insert('', END, values=vv)


def Updatestaff():
    def submitupdate():
        tsid = tsidval.get()
        tsname = tsnameval.get()
        tsquali = tsqualival.get()
        tspost = tspostval.get()
        tsage = tsageval.get()
        tssal = tssalval.get()
        tsexp = tsexpval.get()
        tsphno = tsphnoval.get()
        tsemail = tsemailval.get()
        dname = dnameval.get()
        dno = dnoval.get()
        try:
            global con
            global mycursor
            con = mysql.connector.connect(
                host='localhost', user='root', password='root', database=' staff_management_system1')
            mycursor = con.cursor()
            strr = 'update teaching_staff1 set tsid=%s, tsname=%s, tsquali=%s, tspost=%s, tsage=%s, tssal=%s, tsexp=%s, tsphno=%s, tsemail=%s, dname=%s, dno=%s where tsid=%s and dno=%s'
            mycursor.execute(strr, (
            tsid, tsname, tsquali, tspost, tsage, tssal, tsexp, tsphno, tsemail, dname, dno, tsid, dno))
            con.commit()
            res = messagebox.askyesnocancel(
                'Notifications', 'Id Name updated successfully... and want to clean the form', parent=updateroot)
            if (res == True):
                tsidval.set('')
                tsnameval.set('')
                tsqualival.set('')
                tspostval.set('')
                tsageval.set('')
                tssalval.set('')
                tsexpval.set('')
                tsphnoval.set('')
                tsemailval.set('')
                dnameval.set('')
                dnoval.set('')
        except:
            print("ho")

        con = mysql.connector.connect(
            host='localhost', user='root', password='root', database=' staff_management_system1')
        mycursor = con.cursor()
        strr = 'select * from teaching_staff1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        teaching_stafftable.delete(*teaching_stafftable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4],
                  i[5], i[6], i[7], i[8], i[9], i[10]]

            teaching_stafftable.insert('', END, values=vv)


    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('570x670+200+160')
    updateroot.config(bg='green')
    updateroot.resizable(False, False)
    # -----------------------------add staff lables
    tsidlabel = Label(updateroot, text='Enter TS_id: ', bg='gold2', font=('times', 20), relief=GROOVE,
                      borderwidth=3, width=17, anchor='w')
    tsidlabel.place(x=10, y=10)

    tsnamelabel = Label(updateroot, text='Enter TS_name: ', bg='gold2', font=('times', 20), relief=GROOVE,
                        borderwidth=3, width=17, anchor='w')
    tsnamelabel.place(x=10, y=60)

    tsqualilabel = Label(updateroot, text='Enter TS_qualification: ', bg='gold2', font=('times', 20), relief=GROOVE,
                         borderwidth=3, width=17, anchor='w')
    tsqualilabel.place(x=10, y=110)

    tspostlabel = Label(updateroot, text='Enter TS_post: ', bg='gold2', font=('times', 20), relief=GROOVE,
                        borderwidth=3, width=17, anchor='w')
    tspostlabel.place(x=10, y=160)

    tsagelabel = Label(updateroot, text='Enter TS_age: ', bg='gold2', font=('times', 20), relief=GROOVE,
                       borderwidth=3, width=17, anchor='w')
    tsagelabel.place(x=10, y=210)

    tssalarylabel = Label(updateroot, text='Enter TS_salary: ', bg='gold2', font=('times', 20), relief=GROOVE,
                          borderwidth=3, width=17, anchor='w')
    tssalarylabel.place(x=10, y=260)

    tsexplabel = Label(updateroot, text='Enter TS_experince: ', bg='gold2', font=('times', 20), relief=GROOVE,
                       borderwidth=3, width=17, anchor='w')
    tsexplabel.place(x=10, y=310)

    tsphnolabel = Label(updateroot, text='Enter TS_phno: ', bg='gold2', font=('times', 20), relief=GROOVE,
                        borderwidth=3, width=17, anchor='w')
    tsphnolabel.place(x=10, y=360)

    tsemaillabel = Label(updateroot, text='Enter TS_email: ', bg='gold2', font=('times', 20), relief=GROOVE,
                         borderwidth=3, width=17, anchor='w')
    tsemaillabel.place(x=10, y=410)

    dnamelabel = Label(updateroot, text='Enter D_name: ', bg='gold2', font=('times', 20), relief=GROOVE,
                       borderwidth=3, width=17, anchor='w')
    dnamelabel.place(x=10, y=460)

    dnolabel = Label(updateroot, text='Enter D_no: ', bg='gold2', font=('times', 20), relief=GROOVE,
                     borderwidth=3, width=17, anchor='w')
    dnolabel.place(x=10, y=510)

    stafftypelabel = Label(updateroot, text='Enter Staff_type:', bg='gold2', font=('times', 20), relief=GROOVE,
                           borderwidth=3, width=17, anchor='w')
    stafftypelabel.place(x=10, y=560)
    # --------------------------------------------------------------------add staff entry
    tsidval = StringVar()
    tsnameval = StringVar()
    tsqualival = StringVar()
    tspostval = StringVar()
    tsageval = StringVar()
    tssalval = StringVar()
    tsexpval = StringVar()
    tsphnoval = StringVar()
    tsemailval = StringVar()
    dnameval = StringVar()
    dnoval = StringVar()
    staff_type = StringVar()
    tsidentry = Entry(updateroot, font=('roman', 17, 'bold'), bd=5, textvariable=tsidval)
    tsidentry.place(x=300, y=10)

    tsnameentry = Entry(updateroot, font=('roman', 17, 'bold'), bd=5, textvariable=tsnameval)
    tsnameentry.place(x=300, y=60)

    tsqualidentry = Entry(updateroot, font=('roman', 17, 'bold'), bd=5, textvariable=tsqualival)
    tsqualidentry.place(x=300, y=110)

    tspostentry = Entry(updateroot, font=('roman', 17, 'bold'), bd=5, textvariable=tspostval)
    tspostentry.place(x=300, y=160)

    tsageentry = Entry(updateroot, font=('roman', 17, 'bold'), bd=5, textvariable=tsageval)
    tsageentry.place(x=300, y=210)

    tssalentry = Entry(updateroot, font=('roman', 17, 'bold'), bd=5, textvariable=tssalval)
    tssalentry.place(x=300, y=260)

    tsexpentry = Entry(updateroot, font=('roman', 17, 'bold'), bd=5, textvariable=tsexpval)
    tsexpentry.place(x=300, y=310)

    tsphnoentry = Entry(updateroot, font=('roman', 17, 'bold'), bd=5, textvariable=tsphnoval)
    tsphnoentry.place(x=300, y=360)

    tsemailentry = Entry(updateroot, font=('roman', 17, 'bold'), bd=5, textvariable=tsemailval)
    tsemailentry.place(x=300, y=410)

    dnameentry = Entry(updateroot, font=('roman', 17, 'bold'), bd=5, textvariable=dnameval)
    dnameentry.place(x=300, y=460)

    dnoentry = Entry(updateroot, font=('roman', 17, 'bold'), bd=5, textvariable=dnoval)
    dnoentry.place(x=300, y=510)

    ty = ttk.Combobox(updateroot, width=19, font=('roman', 17, 'bold'), textvariable=staff_type)
    ty['values'] = ('Teaching', 'Non-Teaching')
    ty.place(x=300, y=560)
    # -----------------------------------------------------------submit
    submitbutton = Button(updateroot, text='SUBMIT', font=('roman', 15, 'bold'), bg='yellow', bd=5, width=25,
                          activebackground='blue', activeforeground='white', command=submitupdate)
    submitbutton.place(x=150, y=610)
    updateroot.mainloop()


def Showstaff():
    global con, cursor
    con = mysql.connector.connect(
        host='localhost', user='root', password='root', database=' staff_management_system1')
    mycursor = con.cursor()
    print('Staff Show')
    strr = 'select * from teaching_staff1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    teaching_stafftable.delete(*teaching_stafftable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]

        teaching_stafftable.insert('', END, values=vv)


def Exitstaff():
    res = messagebox.askyesnocancel('Notification', 'Do you want to exit?')
    if (res == True):
        root.destroy()


######################################################################CONNECTION OF DATABASE
def Connectdb():
    global con, mycursor
    host = 'localhost'
    user = 'root'
    password = 'root'
    try:
        con = mysql.connector.connect(host=host, user=user, password=password)
        mycursor = con.cursor()
    except:
        messagebox.showerror('notifications', 'Data is incorrect please try again')
        return
    try:
        strr = 'create database staff_management_system1'
        mycursor.execute(strr)
        strr = 'use staff_management_system1'
        mycursor.execute(strr)
        strr = 'create table teaching_staff1(tsid varchar(20),tsname varchar(20),tsquali varchar(40),tspost varchar(30),tsage varchar(10),tssal varchar(10),tsexp varchar(40),tsphno varchar(15),tsemail varchar(30),dname varchar(30),dno varchar(15),type varchar(45))'
        mycursor.execute(strr)
        strr = 'create table department(dno varchar(15) ,dname varchar(45),no_of_teaching_staff varchar(10),no_of_non_teaching_staff varchar(10),college_id varchar(10))'
        mycursor.execute(strr)
        strr = 'create table college(clgid varchar(15) ,clgname varchar(45),clgphno varchar(10),clgwebsite varchar(10))'
        mycursor.execute(strr)

        messagebox.showinfo('Notification', 'Database created and now you are connected to the database..........',
                            parent=root)

    except:
        strr = 'use staff_management_system1'
        mycursor.execute(strr)


def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%y")
    clock.config(text='Date :' + date_string + "\n" + 'Time :' + time_string)
    clock.after(200, tick)


#########################################################################INTRO SLIDER
import random

colors = ['red', 'green', 'blue', 'yellow', 'pink', 'red2', 'gold2']


def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2, IntroLabelColorTick)


def IntroLabelTick():
    global count, text
    if (count >= len(ss)):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text + ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(200, IntroLabelTick)


######################################################################
from tkinter import *
from tkinter import Toplevel, messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import mysql.connector
import time

root = Tk()
root.title('COLLEGE STAFF MANAGEMENT SYSTEM')
root.config(bg='gold2')
root.geometry('1174x700+200+50')
root.resizable(False, False)

########################################################################## FRAMES
# -------------------------------------------Dataentry Frame Intro

DataEntryFrame = Frame(root, bg='gold2', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=10, y=80, width=500, height=600)

frontlabel = Label(DataEntryFrame, text='-----------------Welcome----------------', width=25,
                   font=('arial', 23, 'italic bold'),
                   bg='gold2')
frontlabel.pack(side=TOP, expand=True)

Addbtn = Button(DataEntryFrame, text='1. Add Staff', width=20, font=('chiller', 20, 'bold'), bd=6, bg='skyblue',
                activebackground='blue', relief=RIDGE, activeforeground='white', command=Addstaff)
Addbtn.pack(side=TOP, expand=True)

Searchbtn = Button(DataEntryFrame, text='2. Search Staff', width=20, font=('chiller', 20, 'bold'), bd=6, bg='skyblue',
                   activebackground='blue', relief=RIDGE, activeforeground='white', command=Searchstaff)
Searchbtn.pack(side=TOP, expand=True)

Deletebtn = Button(DataEntryFrame, text='3. Delete Staff', width=20, font=('chiller', 20, 'bold'), bd=6, bg='skyblue',
                   activebackground='blue', relief=RIDGE, activeforeground='white', command=Deletestaff)
Deletebtn.pack(side=TOP, expand=True)

Updatebtn = Button(DataEntryFrame, text='4. Update Staff', width=20, font=('chiller', 20, 'bold'), bd=6, bg='skyblue',
                   activebackground='blue', relief=RIDGE, activeforeground='white', command=Updatestaff)
Updatebtn.pack(side=TOP, expand=True)

Showbtn = Button(DataEntryFrame, text='5. Show Staff', width=20, font=('chiller', 20, 'bold'), bd=6, bg='skyblue',
                 activebackground='blue', relief=RIDGE, activeforeground='white', command=Showstaff)
Showbtn.pack(side=TOP, expand=True)

Exitbtn = Button(DataEntryFrame, text='6. Exit', width=20, font=('chiller', 20, 'bold'), bd=6, bg='skyblue',
                 activebackground='blue', relief=RIDGE, activeforeground='white', command=Exitstaff)
Exitbtn.pack(side=TOP, expand=True)

ShowDataFrame = Frame(root, bg='gold2', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=550, y=80, width=620, height=600)

# -------------------------------------------------------Show data Frame
style = ttk.Style()
style.configure('Treeview.Heading', font=('chiller', 15, 'bold'), foreground='blue')
style.configure('Treeview', font=('times', 15, 'bold'), foreground='black', background='cyan')
scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)
teaching_stafftable = Treeview(ShowDataFrame, column=('tsid', 'tsname', 'tsquali', 'tspost', 'tsage', 'tssal',
                                                      'tsexp', 'tsphno', 'tsemail', 'dname', 'dno'),
                               yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=teaching_stafftable.xview)
scroll_y.config(command=teaching_stafftable.yview)
teaching_stafftable.heading('tsid', text='tsid')
teaching_stafftable.heading('tsname', text='tsname')
teaching_stafftable.heading('tsquali', text='tsquali')
teaching_stafftable.heading('tspost', text='tspost')
teaching_stafftable.heading('tsage', text='tsage')
teaching_stafftable.heading('tssal', text='tssal')
teaching_stafftable.heading('tsexp', text='tsexp')
teaching_stafftable.heading('tsphno', text='tsphno')
teaching_stafftable.heading('tsemail', text='tsemail')
teaching_stafftable.heading('dname', text='dname')
teaching_stafftable.heading('dno', text='dno')
teaching_stafftable['show'] = 'headings'
teaching_stafftable.column('tsid', width=100)
teaching_stafftable.column('tsname', width=200)
teaching_stafftable.column('tsquali', width=200)
teaching_stafftable.column('tspost', width=200)
teaching_stafftable.column('tsage', width=100)
teaching_stafftable.column('tssal', width=200)
teaching_stafftable.column('tsexp', width=300)
teaching_stafftable.column('tsphno', width=200)
teaching_stafftable.column('tsemail', width=300)
teaching_stafftable.column('dname', width=300)
teaching_stafftable.column('dno', width=100)
teaching_stafftable.pack(fill=BOTH, expand=1)

########################################################################### SLIDER
ss = 'WELCOME TO COLLEGE STAFF MANAGEMENT SYSTEM'
count = 0
text = ''
######################################################
SliderLabel = Label(root, text=ss, relief=RIDGE, borderwidth=4, font=('chiller', 30, 'bold'), width=25, bg='cyan')
SliderLabel.place(x=260, y=0)
IntroLabelTick()
IntroLabelColorTick()

############################################################################## CLOCK
clock = Label(root, font=('times', 14, 'bold'), relief=RIDGE, borderwidth=4, bg='lawn green')
clock.place(x=0, y=0)
tick()

################################################################################CONNECT DATABASE BUTTON
connectbutton = Button(root, text='Connect to Database', width=16, font=('chiller', 17, 'italic bold'), relief=RIDGE,
                       borderwidth=4, bg='green2', activebackground='blue', activeforeground='white', command=Connectdb)
connectbutton.place(x=930, y=0)

root.mainloop()
