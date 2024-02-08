import tkinter
from tkinter import *
from tkinter import messagebox
import random
import mysql.connector as mysql



quesions=[" Which of the following is a Python tuple?",
          " Suppose t = (1, 2, 4, 3), which of the following is incorrect?",
          " What is the data type of (1)?",
          " If a=(1,2,3,4), a[1:-1] is",
          " What type of data is: a=[(1,1),(2,4),(3,9)]?",
          " Tuples are___",
          " Tuples can contain elements of ___ data type.",
          " In tuples values are enclosed in___",
          " Which of the following is not a function of tuple?",
          """ Write the output of the following. A=tuple(\"Python\")
                                                 print(A)""",
          """ Write the output of the following.  a=(23,34,65,20,5)
                                                   print(a[0]+a.index(5)).""",
          " Which of the following commands will create a list?",
          " What is the output when we execute list(\"hello\")?",
          " Suppose list1 is [2445,133,12454,123], what is max(list1)?",
          " To add a new element to a list we use which command?",
          " To insert 5 to the third position in list1, we use which command?",
          " Which of the following would give an error?",
          " Which of the following statements create a dictionary?",
          """ What will be the output of the following code? d = {\"john\":40,\"peter\":45}
                                                             \"john\" in d""",
          """ What will be the output of the following code? d = {\"john\":40, \"peter\":45}
                                                             d[\"john\"]""",
          """ Suppose d = {\"john\":40, \"peter\":45},
              to delete the entry for “john” what command do we use?""",
          " What is the maximum length of a Python identifier?",
          """ What will be the output of the following code?  s={1, 2, 3, 3, 2, 4, 5, 5}
                                                                print(s)""",
          " Which of the following is not a valid set operation in python?",
          " What will print(8**(1/2)) do in python",
          "What happens when ‘1’ == 1 is executed?",
          "An exception is ____",
          "What arithmetic operators cannot be used with strings in Python?",
          """If a function doesn’t have a return statement, which of the following does 
        the function return?"""
          "Who developed Python Programming Language?"
          ]

choice=[
        ["A. [1, 2, 3]","B. (1, 2, 3)","C. {1, 2, 3}","D. (4)"],
        ["A. print(t[3])","B. t[3] = 45","C. print(max(t))","D. print(len(t))"],
        ["A. Tuple","B. Integer","C. List","D. Both tuple and integer"],
        ["A. Error, tuple slicing doesn’t exist","B. [2,3]","C. (2,3,4)","D. (2,3)"],
        ["A. Array of tuples","B. Tuples of lists","C. List of tuples","D. Invalid type"],
        ["A. Immutable","B. Mutable","C. Mutable to some extent","D. none of above."],
        ["A. Some","B. None","C. Both.","D. Any"],
        ["A. Square brackets","B. Curly brackets","C. Parenthesis","D. None of the above"],
        ["A. update().","B. min().","C. Max().","D. Count()."],
        ["A. (python)","B. (\"Python\")","C. (\'P\', \'y\', \'t\', \'h\', \'o\', \'n\')","D. None of Above"],
        ["A. 27","B. 29","C. 28","D. 26"],
        ["A. list1 = list()","B. list1 = []","C. list1 = list([1, 2, 3])","D. all of the mentioned"],
        ["A. [‘h’, ‘e’, ‘l’, ‘l’, ‘o’]","B.  [‘hello’]","C. [‘llo’]","D. [‘olleh’]"],
        ["A. 2445","B. 133","C. 123","D. 12454"],
        ["A. list1.add(5)","B. list1.append(5)","C. list1.addLast(5)","D. list1.addEnd(5)"],
        ["A. list1.append(3, 5)","B. list1.add(3, 5)","C. list1.insert(2, 5)","D. list1.insert(3, 5)"],
        ["A. list1=[]","B. None of the mentioned","C. list1=[2,8,7]","D. list1=[]*3"],
        ["A. d = {}","B. d = {“john”:40, “peter”:45}","C. d = {40:”john”, 45:”peter”}","D. All of the above"],
        ["A. True","B. False","C. None","D. Error"],
        ["A. 40","B. 45","C. \"john\"","D. \"peter\""],
        ["A. d.delete(\"john\":40)","B. d.delete(\"john\")","C. del d[\"john\"]","D. del d(\"john\":40)"],
        ["A. 32","B. 16","C. 128","D. No Fixed Length is Specified"],
        ["A. {1,2,3,4,5,5}","B. {1,2,3,4,5}","C. none","D. {1,5}"],
        ["A. Union","B. Intersection","C. Difference","D. none of the above"],
        ["A. Square root","B. Cube root","C. Multiplication","D. Division"],
        ["A. we get a True","B. we get a False","C. an TypeError occurs","D. a ValueError occurs"],
        ["A. an object","B. a special function","C. a standard module","D. a module"],
        ["A. +","B. -","C. *","D. All of the mentioned"],
        ["A. zero","B. one","C. none","D. more than zero"],
        ["A. Wick van Rossum","B. Rasmus Lerdorf","C. Guido van Rossum","D. Niene Stom"]
    ]

answer=[1,1,1,3,2,0,3,2,0,2,0,3,0,3,1,2,1,0,0,2,3,1,3,0,1,0,2,2,2]

user_ans=[]


indexes=[]
def gen():
   
    while(len(indexes)<10):
        x=random.randint(0,29)


        if x in indexes:
            continue
        else:
            indexes.append(x)
       


def showresult(score):
    l1.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()

    global label,label1,label11,btn
    label=Label(win,text= "Your Score is ",font="Verdana 24 bold",bg="#9de9fa",fg="black",justify="center")
    label.place(x=500,y=250)
    label1=Label(win,text=score,font="Verdana 24 bold",bg="#9de9fa",fg="black",justify="center")
    label1.place(x=750,y=250)
    
    if score!=10:
        label11=Label(win,text="/10",font="Verdana 24 bold",bg="#9de9fa",fg="black",justify="center")
        label11.place(x=775,y=250)
    else:
        label11=Label(win,text="/10",font="Verdana 24 bold",bg="#9de9fa",fg="black",justify="center")
        label11.place(x=800,y=250)


    btn1=Button(text="Quit",font="bold 18",bg="black",fg="cyan",command=win.destroy)
    btn1.place(x=630,y=400)
     
    
def calc():
    global indexes,user_ans,answer
    x=0
    score=0
    for i in indexes:
        if user_ans[x]==answer[i]:
            score=score+1
        x+=1
    showresult(score)
    

ques=1

def select():
    global i,user_ans,l1,r1,r2,r3,r4,ques
    x=i.get()
    user_ans.append(x)
    i.set(-1)
    
    if ques < 10:
        l1.config(text=quesions[indexes[ques]])
        r1['text']=choice[indexes[ques]][0]
        r2['text']=choice[indexes[ques]][1]
        r3['text']=choice[indexes[ques]][2]
        r4['text']=choice[indexes[ques]][3]
        ques +=1
    else:
        calc()

def start():
    global l1,r1,r2,r3,r4
    
    
    l1=Label(win,text=quesions[indexes[0]],font=("cambria",25,"bold"),bg="#9de9fa",fg="black")
    l1.place(x=130,y=150)
    
    global i
    i=IntVar()
    i.set(-1)
    r1=Radiobutton(win,text=choice[indexes[0]][0],value=0,variable=i,font="Verdana 16 bold",bg="#9de9fa",fg="black",command=select)
    r1.place(x=150,y=250)   
   
    r2=Radiobutton(win,text=choice[indexes[0]][1],value=1,variable=i,font="Verdana 16 bold",bg="#9de9fa",fg="black",command=select)
    r2.place(x=150,y=300)
   
    r3=Radiobutton(win,text=choice[indexes[0]][2],value=2,variable=i,font="Verdana 16 bold",bg="#9de9fa",fg="black",command=select)
    r3.place(x=150,y=350)

    r4=Radiobutton(win,text=choice[indexes[0]][3],value=3,variable=i,font="Verdana 16 bold",bg="#9de9fa",fg="black",command=select)
    r4.place(x=150,y=400)    

   
def remove():
    global l,b
    l.destroy()
    b.destroy()
    gen()
    start()
    


def welcome():
    global l,b
    l=Label(win,text="Welcome To The Quiz on Python",bg="#9de9fa",fg="black",font=("cambria",30,"bold"))
    l.place(x=350,y=250)
    

    b=Button(win,text="Start Quiz",font="bold 14",bg="black",fg="cyan",command=remove)
    b.place(x=550,y=400)


def open_window():

    def check():
        name=Entry.get(e1)
        sec=Entry.get(e2)
        regno=Entry.get(e3)
        unm=Entry.get(e4)
        password=Entry.get(e5)
        cpass=Entry.get(e6)
        
    
        if(name!="" and regno!="" and sec!="" and unm!="" and password!="" and cpass!=""):
            if(password!=cpass):
                messagebox.showinfo("Error!!!!!","Password Doesn't Match!!")
        
            else:
                con = mysql.connect(host="localhost",user="root",password="raghavarora09",database="t20")
                cursor = con.cursor()
                cursor.execute("insert into quiz values('"+name+"','"+regno+"','"+sec+"','"+unm+"','"+password+"','"+cpass+"')")
                cursor.execute("commit")
                
                messagebox.showinfo("SignUp Status","SignUp Successful!!!!")
               
                con.close()
                x = rem0()
            
        else:
            messagebox.showinfo("Error!!!!","Please Fill All the fields")

        
      
    global l,l1,l2,l3,l4,l5,l6,b1,b2
    l=Label(win,text="SIGN UP!!",fg="black",font="Verdana 24 bold",bg="#9de9fa")
    l.place(x=600,y=100)
    
    
    l1=Label(win,text="Name:",fg="black",font="Verdana 16 bold",bg="#9de9fa")
    l1.place(x=500,y=200)
    e1=Entry(win,bg="#9de9fa",width=25,bd=3)
    e1.place(x=750,y=200)
        
    l2=Label(win,text="Registration No:",fg="black",font="Verdana 16 bold",bg="#9de9fa")
    l2.place(x=500,y=250)
    e2=Entry(win,bg="#9de9fa",width=25,bd=3)
    e2.place(x=750,y=250)

    l3=Label(win,text="Section:",fg="black",font="Verdana 16 bold",bg="#9de9fa")
    l3.place(x=500,y=300)
    e3=Entry(win,bg="#9de9fa",width=25,bd=3)
    e3.place(x=750,y=300)
        
   
    l4=Label(win,text="Enter Username:",fg="black",font="Verdana 16 bold",bg="#9de9fa")
    l4.place(x=500,y=350)
    e4=Entry(win,bg="#9de9fa",width=25,bd=3)
    e4.place(x=750,y=350)
    
        
    l5=Label(win,text="Enter Password:",fg="black",font="Verdana 16 bold",bg="#9de9fa")
    l5.place(x=500,y=400)
    e5=Entry(win,bg="#9de9fa",width=25,bd=3)
    e5.place(x=750,y=400)
        
    l6=Label(win,text="Confirm Password:",fg="black",font="Verdana 16 bold",bg="#9de9fa")
    l6.place(x=500,y=450)
    e6=Entry(win,bg="#9de9fa",width=25,bd=3)
    e6.place(x=750,y=450)

    b1=Button(win,text="Submit",fg="black",font="Verdana 13 bold",bg="#9de9fa",command=check)
    b1.place(x=650,y=500)
    

  

def rem1():
    global l1,l2,l0,e1,e2,b1,b2,fm
    fm.destroy()
    l1.destroy()
    l2.destroy()
    l0.destroy()
    e1.destroy()
    e2.destroy()
    b1.destroy()
    b2.destroy()            
    open_window()


def rem():
    global l1,l2,l0,e1,e2,b1,b2,fm
    fm.destroy()
    l1.destroy()
    l2.destroy()
    l0.destroy()
    e1.destroy()
    e2.destroy()
    b1.destroy()
    b2.destroy()
    welcome()
    
def rem0():
    global l,l2,l3,l4,l5,l6
    global e1,e2,e3,e4
    global e5,e6,b1
    l.destroy()
    l1.destroy()
    l2.destroy()
    l3.destroy()
    l4.destroy()
    l5.destroy()
    l6.destroy()
    e1.destroy()
    e2.destroy()
    e3.destroy()
    e4.destroy()
    e5.destroy()
    e6.destroy()
    b1.destroy()
    login()



con=mysql.connect(
    host="######",
    user="#####",
    password="#####",
    database="####"
    )

cursor=con.cursor()

def user_login(uname,passw):
    try:
        cursor.execute("select * from quiz where name='"+uname+"' and password='"+passw+"'")
        return (cursor.fetchone())
    except:
        return False
    
    
    
def msg():
    uname=Entry.get(e1)
    passw=Entry.get(e2)

    if(uname=="" or passw==""):
        messagebox.showinfo("Alert","Fill all details......")
    else:
        res = user_login(uname,passw)
        if res:
            messagebox.showinfo("Message","Login Successfully....")
            x = rem()
        else:
            messagebox.showinfo("Alert","Login Failed.......")



    
win=tkinter.Tk()
win.title("Let's Play Quiz")
win.configure(bg="#9de9fa")
win.geometry("1350x700+0+0")


def login():
    global l1,l2,l0,e1,e2,b1,b2,fm
    l0=Label(win,text="Login!!",bg="#9de9fa",fg="black",font="Verdana 30 bold")
    l0.place(x=625,y=125)

    fm=Frame(win,bd=4,relief=RIDGE,bg="#9de9fa")
    fm.place(x=450,y=200,width=475,height=300)

    

    l1=Label(fm,text="Username:",bg="#9de9fa",fg="black",font="Verdana 16 bold",padx=20)
    l1.grid(row=1,column=0,padx=20,pady=40)
    e1=Entry(fm,font="Verdana 12 ",bd=2,bg="#9de9fa")
    e1.grid(row=1,column=1,padx=20)

    l2=Label(fm,text="Password:",bg="#9de9fa",fg="black",font="Verdana 16 bold")
    l2.grid(row=2,column=0,padx=20,pady=40)
    e2=Entry(fm,font="Verdana 12 ",bd=2,bg="#9de9fa",show='*')
    e2.grid(row=2,column=1,padx=20)


    b1=Button(fm,text="Login",font="Verdana 13 bold",bg="black",fg="cyan",command=msg)
    b1.grid(row=3,column=0,padx=50)

    b2=Button(fm,text="Sign Up",font="Verdana 13 bold",bg="black",fg="cyan",command=rem1)
    b2.grid(row=3,column=1)

login()
win.mainloop()
