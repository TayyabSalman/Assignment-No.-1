import unittest
import code
#import yappi
from Tkinter import *
from Tkinter import Tk, Frame, BOTH
from PIL import Image, ImageTk
from PIL import ImageTk, Image
import os
import tkMessageBox
import tkFont
import MySQLdb
import getpass

db = MySQLdb.connect("localhost", "root", "", "assignment")
cursor = db.cursor()
# cursor.execute("create table question (qnum int (2),type varchar(10),ques varchar(80),op1 varchar(85),op2 varchar(85),op3 varchar(85),op4 varchar(85),corA varchar(85),qid int(5),"
#               "_cour varchar(45))")

status = 0
def NUMERIC():
    master = Tk()
    global e0, e1, e2, e3, e4, e5, e6, e7, e8, e9

    master.maxsize(700, 500)
    master.minsize(700, 500)
    master.geometry("500x500")
    Label(master, text="Enter Questions. Press submit to enter in \n database and SAVE to finalize it \n",font=(None, 15), pady=20, ).grid(row=0, columnspan=2)
    Label(master, text="Question Number: ", font="arial").grid(row=1, column=0,sticky=E)
    e0 = Entry(master,width=30)
    e0.grid(row=1, column=1,sticky=W)
    e1 = "NUMERIC"
    Label(master, text="Quiz Id: ", font="arial").grid(row=2, column=0,sticky=E)
    e2 = Entry(master, bg="white", width=30)
    e2.grid(row=2, column=1,sticky=W)
    Label(master, text="Course Name: ", font="arial").grid(row=3, column=0,sticky=E)
    e3 = Entry(master,  bg="white",width=30)
    e3.grid(row=3, column=1,sticky=W)
    Label(master, text="Question Statment: ", font="arial").grid(row=4, column=0,sticky=E)
    e4 = Entry(master, bg="white", width=30)
    e4.grid(row=4, column=1,sticky=W)
    Label(master, text="Correct Answer: ", font="arial").grid(row=5, column=0,sticky=E)
    e9 = Entry(master, bg="white", fg="black", width=30)
    e9.grid(row=5, column=1,sticky=W)
    Button(master, text="SAVE", command=stor_data, font="arial", bg="white").grid(row=6, column=0)
    Button(master, text="Submit", command=sub_data, font="arial", bg="green").grid(row=6, column=1)

    master.grid_columnconfigure(0, weight=1)
    master.grid_columnconfigure(1, weight=1)

    return true

def TF():
    master = Tk()
    global e0, e1, e2, e3, e4, e5, e6, e7, e8, e9
    master.maxsize(700, 500)
    master.minsize(700, 500)
    master.geometry("500x500")
    Label(master, text="Enter Questions. Press submit to enter in \n database and SAVE to finalize it \n",font=(None, 15), pady=20, ).grid(row=0, columnspan=2)
    Label(master, text="Question Number: ", font="arial").grid(row=1, column=0,sticky=E)
    e0 = Entry(master, bg="white",width=30)
    e0.grid(row=1, column=1,sticky=W)
    e1 = "T/F"
    Label(master, text="Quiz Id: ", font="arial").grid(row=2, column=0,sticky=E)
    e2 = Entry(master, bg="white",width=30)
    e2.grid(row=2, column=1,sticky=W)
    Label(master, text="Course Name: ", font="arial").grid(row=3, column=0,sticky=E)
    e3 = Entry(master, bg="white",width=30)
    e3.grid(row=3, column=1,sticky=W)
    Label(master, text="Question Statment: ", font="arial").grid(row=4, column=0,sticky=E)
    e4 = Entry(master, bg="white", width=30)
    e4.grid(row=4, column=1,sticky=W)
    Label(master, text="Option 1: ", font="arial").grid(row=5, column=0,sticky=E)
    e5 = Entry(master, bg="white", width=30)
    e5.grid(row=5, column=1,sticky=W)
    Label(master, text="Option 2: ", font="arial").grid(row=6, column=0,sticky=E)
    e6 = Entry(master, bg="white", width=30)
    e6.grid(row=6, column=1,sticky=W)
    Label(master, text="Correct Answer: ", font="arial").grid(row=7, column=0,sticky=E)
    e9 = Entry(master, bg="white", width=30)
    e9.grid(row=7, column=1,sticky=W)
    Button(master, text="SAVE", command=stor_data, font="arial", bg="white").grid(row=9, column=0)
    Button(master, text="Submit", command=sub_data, font="arial", bg="white").grid(row=9, column=1)

    master.grid_columnconfigure(0, weight=1)
    master.grid_columnconfigure(1, weight=1)

def MCQ():
    master = Tk()
    master.maxsize(700, 500)
    master.minsize(700, 500)
    master.geometry("500x500")
    master.title("Entering MCQ")
    global e0, e1, e2, e3, e4, e5, e6, e7, e8, e9
    Label(master, text="Enter Questions. Press submit to enter in \n database and SAVE to finalize it \n", font=(None, 15), pady=20, ).grid(row=0, columnspan=2)
    Label(master, text="Question Number: ", font="arial").grid(row=1, column=0,sticky=E)
    e0 = Entry(master, bg="white",fg="black", width=30)
    e0.grid(row=1, column=1,sticky=W)
    e1 = "MCQ"
    Label(master, text="Quiz Id: ", font="arial",).grid(row=2, column=0,sticky=E)
    e2 = Entry(master, bg="white",fg="black", width=30)
    e2.grid(row=2, column=1,sticky=W)
    Label(master, text="Course Name: ", font="arial").grid(row=3, column=0,sticky=E)
    e3 = Entry(master, bg="white",fg="black", width=30)
    e3.grid(row=3, column=1,sticky=W)
    Label(master, text="Question Statment: ", font="arial").grid(row=4, column=0,sticky=E)
    e4 = Entry(master, bg="white",fg="black", width=30)
    e4.grid(row=4, column=1,sticky=W)
    Label(master, text="Option 1: ", font="arial").grid(row=5, column=0,sticky=E)
    e5 = Entry(master, bg="white",fg="black", width=30)
    e5.grid(row=5, column=1,sticky=W)
    Label(master, text="Option 2: ", font="arial").grid(row=6, column=0,sticky=E)
    e6 = Entry(master, bg="white",fg="black", width=30)
    e6.grid(row=6, column=1,sticky=W)
    Label(master, text="Option 3: ", font="arial").grid(row=7, column=0,sticky=E)
    e7 = Entry(master, bg="white",fg="black", width=30)
    e7.grid(row=7, column=1,sticky=W)
    Label(master, text="Option 4: ", font="arial").grid(row=8, column=0,sticky=E)
    e8 = Entry(master, bg="white",fg="black", width=30)
    e8.grid(row=8, column=1,sticky=W)
    Label(master, text="Correct Answer: ", font="arial").grid(row=9, column=0,sticky=E)
    e9 = Entry(master, bg="white",fg="black", width=30)
    e9.grid(row=9, column=1,sticky=W)
    Button(master, text="SAVE", command=stor_data, font="arial", bg="white").grid(row=11, column=0)
    Button(master, text="Submit", command=sub_data, font="arial", bg="white").grid(row=11, column=1)

    master.grid_columnconfigure(0, weight=1)
    master.grid_columnconfigure(1, weight=1)


def sub_data():
    if (status):
        tkMessageBox.showinfo("Title", "Quiz Submitted Successfully !!")
    else:
        tkMessageBox.showinfo("Title", "Quiz Submission Failed!!")


def stor_data():
    global status
    quNum = int(e0.get())
    quType = e1
    quId = int(e2.get())
    # qId.append(quId)
    corName = e3.get()
    # corN.append(corName)n
    # print corN,qId
    quStat = e4.get()

    if quType == "MCQ":
        op1 = e5.get()
        op2 = e6.get()
        op3 = e7.get()
        op4 = e8.get()
        corA = e9.get()
        sql = "insert into question values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        status = cursor.execute(sql, (quNum, quType, quStat, op1, op2, op3, op4, corA, quId, corName))
    elif quType == "T/F":
        op1 = e5.get()
        op2 = e6.get()
        corA = e9.get()
        op3 = None
        op4 = None
        sql = "insert into question values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        status = cursor.execute(sql, (quNum, quType, quStat, op1, op2, op3, op4, corA, quId, corName))
    elif quType == "NUMERIC":
        op1 = None
        op2 = None
        op3 = None
        op4 = None
        corA = e9.get()
        sql = "insert into question values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        status = cursor.execute(sql, (quNum, quType, quStat, op1, op2, op3, op4, corA, quId, corName))

def add(x,y):
    return x+y


def make_quiz():
    master = Tk()
    master.maxsize(700, 500)
    master.minsize(700, 500)
    master.geometry("500x500")
    master.title("Choice of Questions")
    Label(master, text="What sort of Questions will you include in your Quiz? ", font="arial", pady=20).grid(row=0, columnspan=2)
    Button(master, text="1. MCQ", command=MCQ, font="arial",bg="white").grid(row=1, column=0)
    Button(master, text="2. T/F", command=TF, font="arial", bg="white").grid(row=2, column=0)
    Button(master, text="3. NUMERIC", command=NUMERIC, font="arial",bg="white").grid(row=3, column=0)
    master.grid_columnconfigure(0, weight=1)

def atmt_quiz():
    root = Tk()
    root.minsize(700, 500)
    root.maxsize(700, 500)
    global q0, q1
    Label(root, text="Please enter Course Name and it's ID \n", font=(None, 15)).grid(row=0, columnspan=2)

    Label(root, text="Quiz ID: ", font="arial", pady=6).grid(row=1, column=0, sticky=E)
    q0 = Entry(root, bg="white", width=30)
    q0.grid(row=1, column=1, sticky=W)
    Label(root, text="Course Name: ", font="arial", pady=6).grid(row=2, column=0, sticky=E)
    q1 = Entry(root, bg="white", width=30)
    q1.grid(row=2, column=1, sticky=W)

  #  Button(master, text="Log-in", command=lambda: _log(master), font="arial", bg="white").grid(row=4, pady=20,columnspan=2)
    Button(root, text="Submit", command=lambda: fet_quiz(root, q0.get(), q1.get()), font="arial", bg="white").grid(row=4, pady=20,columnspan=2)


    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

def add_marks(x1):
    s1 = "insert into student values (%s,%s,%s,%s)"
    status=cursor.execute(s1,(globalName,1,1,x1))


def chk(i, j):
    print i, j


# def mar():
#   print
def fet_quiz(test1, q0, q1):
    marks = 0
    master = Tk()
    master.maxsize(700, 500)
    master.minsize(700, 500)
    master.geometry("500x500")
    id = int(q0)
    cn = str(q1).upper()


    try:
        sql = "select * from question where qid=%s and _cour=%s"
        cursor.execute(sql, (id, cn))
        results = cursor.fetchall()
        x = [0, 0]
        answer = [0, 0]

        def nex():
            if x[0] > 0:
                print x[1]
                if answer[0].get() == answer[1]:
                    x[1] += 1
                    print x[1]
            if x[0] > (len(results) - 1):
                master.destroy()
                tkMessageBox.showinfo("Title", ("Quiz is finished. No more attempts are available. Marks Obtained: %s" % x[1]))
                typ = str(x[1])
                add_marks(typ)
                return
            y = Label(master, text="Question: %s " % results[x[0]][2], justify=LEFT, anchor=W,font=("arial", 12))
            y.pack()
            z = Label(master, text="1) %s" % results[x[0]][3])
            z.pack()
            a = Label(master, text="2) %s" % results[x[0]][4])
            a.pack()
            b = Label(master, text="3) %s" % results[x[0]][5])
            b.pack()
            c = Label(master, text="4) %s" % results[x[0]][6])
            c.pack()
            var = StringVar()
            ans = Entry(master, textvariable=var)
            ans.pack()
            answer[0] = ans
            answer[1] = results[x[0]][7]
            # print type(int(ans.get()))f
            # if (ans.get()==results[x[0]][7]):
            #   x[1]+=1
            # print var.get()
            # sub=Button(master,text="Submit",command=sequence(nex,mar))
            sub = Button(master, text="Submit", command=nex, bg="white", font="arial")
            sub.pack()
            # chk(results[x[0][7]],var.get())

            x[0] += 1


        nex()
        # scrollbar.config(command=listbox.yview)
        # marks=112
        # tkMessageBox.showinfo("Title",marks)

        # while(x<len(results)):
    except:
        print "Cannot locate data"

def next(ref):

    print "sasa"
    cur = db.cursor()
    # Use all the SQL you like
    cur.execute("SELECT * FROM test")
    string = cur.fetchall()
    global globalName
    globalName=r0.get()
    print globalName
    #print "HELLOOOOOOOOOOO" , r0.get() ,"HELLOOOOOOOOOOO"

    for row in string:
        if(r0.get()==row[1]):
            if(r1.get()==row[2]):
                global var
                var=0
                ref.destroy()
                slct_quiz()
    else:
        tkMessageBox.showerror("Sorry", "Sorry")



    mainloop()



def stud_authen():
    master = Tk()
    global r0,r1
    master.maxsize(700, 500)
    master.minsize(700, 500)
    master.geometry("500x500")
    master.title("Welcome to Quiz Application")
    Label(master, text="Enter Username and Password \n",font=(None, 20),pady=20,).grid(row=0, columnspan=2)

    Label(master, text="Enter User Name: ", font="arial",pady=6).grid(row=2, column=0,sticky=E)
    r0 = Entry(master, bg="white", width=30)
    r0.grid(row=2, column=1,sticky=W)
    Label(master, text="Enter Password: ",font="arial",pady=6).grid(row=3, column=0,sticky=E)
    r1 = Entry(master, bg="white", show="*", width=30)
    r1.grid(row=3, column=1,sticky=W)

   # Button(master, text="Submit", command=sub_data, font="arial", bg="green").grid(row=6, column=1)


    Label(master, text="Note: Please enter valid Information \n", font=("perpetua", 10),pady=10, ).grid(row=8, columnspan=2)

    master.grid_columnconfigure(0, weight=1)
    master.grid_columnconfigure(1, weight=1)
    Button(master, text="Log-in", command=lambda: next(master), font="arial", bg="white").grid(row=4,pady=20, columnspan=2)


def slct_quiz():
    master = Tk()

    master.maxsize(700, 500)
    master.minsize(700, 500)
    master.geometry("500x500")
    master.title("Quiz Choices")
    op = Label(text="Available Quizzes are given below.\n", font=("arial", 20))
    op.pack()

    op2 = Label(text="Enter the ID of Quiz and Course name of that quiz in READY tab \n", font=("perpetua", 13))
    op2.pack()


    try:
        cursor.execute("select distinct qid,_cour from question")
        res = cursor.fetchall()
        for row in res:
            opt = Label(master, text="%s is the ID of '%s' " % row)
            opt.pack()
    except:
        print "Cannot locate data"


    atmt_quiz()

    mainloop()


def _log(ref):
    val1 = str(r0.get())
    val2 = str(r1.get())
    roll = (val1.upper())
    ref.destroy()
    if (roll == "INSTRUCTOR") and (val2 == '12345'):
        make_quiz()
    elif (roll == "STUDENT") and (val2 == '12345'):
        stud_authen()
    else:
        exit()
#        tkMessageBox.showerror("Sorry", "Sorry")

 #       _log(ref)



yappi.start()
if __name__ == '__main__':
    # _log()
    # make_quiz()
    # slct_quiz()
    # atmt_quiz()
    master = Tk()
    master.maxsize(700, 500)
    master.minsize(700, 500)
    master.geometry("500x500")
    master.title("Welcome to Quiz Application")
    Label(master, text="Welcome to Quiz Application \n",font=(None, 20),pady=20,).grid(row=0, columnspan=2)

    Label(master, text="Login as Student or Instructor? \n Type Student or Instructor \n", font="arial", pady=20).grid(row=1, columnspan=2)
    Label(master, text="Enter Roll: ", font="arial",pady=6).grid(row=2, column=0,sticky=E)
    r0 = Entry(master, bg="white", width=30)
    r0.grid(row=2, column=1,sticky=W)
    Label(master, text="Enter Key: ",font="arial",pady=6).grid(row=3, column=0,sticky=E)
    r1 = Entry(master, bg="white", show="*", width=30)
    r1.grid(row=3, column=1,sticky=W)
    Button(master, text="Log-in", command=lambda: _log(master), font="arial", bg="white").grid(row=4,pady=20, columnspan=2)

    Label(master, text="Note: Invalid Input will result in closing of application \n", font=("perpetua", 10), pady=10, ).grid(row=8, columnspan=2)
    master.grid_columnconfigure(0, weight=1)
    master.grid_columnconfigure(1, weight=1)

    mainloop()
    yappi.get_func_stats().print_all()

    yappi.get_thread_stats().print_all()


    ########
