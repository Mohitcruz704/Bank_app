from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import sqlite3


t=Tk()
t.geometry('600x400')
t.resizable(0,0)

f55=None




#--------------------REGISTRATION---------------------------
#Registration Screen
def regis():
    f3=Frame(bg="#091e42")
    f3.place(x=0,y=0,width=600, height=400)

    r1=StringVar()
    r2=StringVar()
    r3=StringVar()
    
    un=Label(text="User Name",bg="#091e42",fg="white", font=("",12))
    un.place(x=200,y=50)
    e1=Entry(f3, font=("",11), textvariable=r1)
    e1.place(x=300,y=50, width=130)

    up=Label(text="Password",bg="#091e42",fg="white", font=("",12))
    up.place(x=200,y=100)
    e2=Entry(f3, font=("",11),show='*', textvariable=r2)
    e2.place(x=300,y=100, width=130)

    uc=Label(text="Contact No.",bg="#091e42",fg="white", font=("",12))
    uc.place(x=200,y=150)
    e3=Entry(f3, font=("",11), textvariable=r3)
    e3.place(x=300,y=150, width=130)
#_----------------------------------EXCEPTION IS OCCURIG WHICH IS WHEN CLICK O REGIS BUTTON WITH FILILING F=DATA IT SHOWS SAME MESSAGE
    def regis1():
        db=sqlite3.connect("Bank.db")
        cr=db.cursor()
        if( r1.get()!="" and r2.get()!="" and r3.get()!=""):
            cr.execute("Insert into regis values('"+r1.get()+"','"+r2.get()+"','"+r3.get()+"')")
            db.commit()
            db.close()
            messagebox.showinfo('Title',"User Registered")
            r1.set("")
            r2.set("")
            r3.set("")
            # set is used to set the entry box empty.
        else:
            messagebox.showinfo('Title','invalid input')
        

    b1=Button(f3,text="Regis",command=regis1 )
    b1.place(x=260,y=210,width=100,height=40)

    b2=Button(f3,text="Home",command=home)
    b2.place(x=15,y=340,width=100,height=40)

    b3=Button(f3,text="Login",command=login )
    b3.place(x=480,y=340,width=100,height=40)




    
#----------------------------------------LOGIN---------------------------------------------  
#Login Screen

def login():
    f2=Frame(bg="#091e42")
    f2.place(x=0,y=0,width=600, height=400)

    g1= StringVar()
    g2= StringVar()

    
    un=Label(f2,text="User Name",bg="#091e42",fg="white", font=("",12))
    un.place(x=200,y=50)
    e1=Entry(f2, font=("",11),textvariable=g1)
    e1.place(x=300,y=50, width=130)

    up=Label(f2,text="Password",bg="#091e42",fg="white", font=("",12))
    up.place(x=200,y=100)
    e2=Entry(f2, font=("",11),show='*', textvariable=g2)
    e2.place(x=300,y=100, width=130)

    def login1():
        db=sqlite3.connect("Bank.db")
        c=db.cursor()
        if(g1.get()=="" and g2.get()==""):
            messagebox.showinfo('Tilte',"Invalid Input..")
        else:
            r=c.execute("select * from regis where UNAME='"+g1.get()+"' AND UPASS='"+g2.get()+"'")
            for r1 in r:
                mymenu()
                #messagebox.showinfo('Title','Welcome')
                break
            else:
                messagebox.showinfo('Title','Invalid User name and password')
            
            

            db.commit()
            db.close()
            g1.set("")
            g2.set("")

        
    b1=Button(f2,text="LogIn",command=login1 )
    b1.place(x=260,y=160,width=100,height=40)

    b2=Button(f2,text="Home",command=home)
    b2.place(x=15,y=340,width=100,height=40)

    b3=Button(f2,text="Regis", command=regis)
    b3.place(x=480,y=340,width=100,height=40)




#---------------------MENU OPTIONS--------------------------------  
# Menu Options/ Screens
def mymenu():
    n=ttk.Notebook()
    n.place(x=0,y=0 ,width=600,height=400)
    def demo(a):
        if(n.index("current")==5):
            home()
    n.bind("<<NotebookTabChanged>>",demo)
    createAccount(n)
    showallAccount(n)
    searchAccount(n)
    updateAccountInfo(n)
    deleteAccount(n)
    logoutAccount(n)





#--------------------Create Account---------------------------
# create account 
def createAccount(n):
    f4=Frame(bg="#091e42")
    n.add(f4,text="Create Account")

    i1=StringVar() # account number
    i2=StringVar() # FUll name
    i3=StringVar() # city of residence
    i4=StringVar() # amount Deposite
    i5=StringVar() #
    
    u1=Label(f4,text="Account No.",bg="#091e42",fg="white", font=("",11))
    u1.place(x=200,y=50)
    e1=Entry(f4,font=("",11),textvariable=i1)
    e1.place(x=300,y=50, width=130)

    u2=Label(f4,text="Full Name",bg="#091e42",fg="white", font=("",11))
    u2.place(x=200,y=100)
    e2=Entry(f4,font=("",11),textvariable=i2)
    e2.place(x=300,y=100, width=130)

    u3=Label(f4,text="State/City",bg="#091e42",fg="white", font=("",11))
    u3.place(x=200,y=150)
    e3=Entry(f4,font=("",11),textvariable=i3)
    e3.place(x=300,y=150, width=130)

    u4=Label(f4,text="Amt. Deposite",bg="#091e42",fg="white", font=("",11))
    u4.place(x=200,y=200)
    e4=Entry(f4,font=("",11),textvariable=i4)
    e4.place(x=300,y=200, width=130)

    
#__________________________Insert Data into "ins" table___________________________________
    def insertdemo1():
        db=sqlite3.connect("Bank.db")
        cr=db.cursor()
        cr.execute("Insert into account values('"+i1.get()+"','"+i2.get()+"','"+i3.get()+"','"+i4.get()+"')")
        db.commit()
        db.close()
        messagebox.showinfo('Title',"INSERTED SUCESFULL...")
        i1.set("")
        i2.set("")
        i3.set("")
        i4.set("")
        i5.set("")
        showalldata1(f55) #to update the show data in show data menu.------ it first f55 is  decleared in the top for global then f55 is decleared globally in the function_call()

#________________________________________________________________________
    b1=Button(f4,text='Insert', command=insertdemo1)
    b1.place(x=260, y=330,width=80,height=40)






#-------------------------------SHOW ALL ACCOUNT----------------------------------
#Show all account
def showallAccount(n):
    f5=Frame(bg="#091e42")
    n.add(f5,text="showallAccount")
    global f55
    f55=f5
    showalldata1(f5)
    #f4.place(x=0,y=0, width=600, height=400)

def showalldata1(f5):
        for w in f5.winfo_children():
            w.destroy()
        db=sqlite3.connect("Bank.db")
        cr=db.cursor()
        r=cr.execute("Select * from account")
        
        u1=Label(f5, text="Account no.", font=("",11),bg="#091e42",fg="white")
        u1.place(x=0,y=0,width=120)

        u2=Label(f5,text="Full Name",font=("",11),bg="#091e42",fg="white")
        u2.place(x=120,y=0,width=120)

        u3=Label(f5,text="State/City",font=("",11),bg="#091e42",fg="white")
        u3.place(x=240,y=0,width=120)

        u4=Label(f5,text="Balance",font=("",11),bg="#091e42",fg="white")
        u4.place(x=360,y=0,width=120)

        #u5=Label(f5,text="Maths",font=("",11),bg="#091e42",fg="white")
        #u5.place(x=480,y=0,width=120)
        x=0
        y=60
        for r1 in r:
            Label(f5,text=r1[0],font=("",11),bg="#091e42",fg="white").place(x=x,y=y,width=120)
            x+=120
            Label(f5,text=r1[1],font=("",11),bg="#091e42",fg="white").place(x=x,y=y,width=120)
            x+=120
            Label(f5,text=r1[2],font=("",11),bg="#091e42",fg="white").place(x=x,y=y,width=120)
            x+=120
            Label(f5,text=r1[3],font=("",11),bg="#091e42",fg="white").place(x=x,y=y,width=120)
            x+=120
            #Label(f5,text=r1[4],font=("",11),bg="#091e42",fg="white").place(x=x,y=y,width=120)
            y+=40
            x=0
        db.commit()
        db.close()






#-------------------SEARCH ACCOUNT-----------------------------------------
# search account 
def searchAccount(n):
    f6=Frame(bg="#091e42")
    n.add(f6,text="search Account")
    #f4.place(x=0,y=0, width=600, height=400)
    s1=StringVar()
    
    u1=Label(f6,text="Account No.",bg="#091e42",fg="white", font=("",11))
    u1.place(x=100,y=50)
    e1=Entry(f6,font=("",11),textvariable=s1)
    e1.place(x=200,y=50, width=130)

   


    def searchdata1():
        db=sqlite3.connect("Bank.db")
        cr=db.cursor()
        r=cr.execute("select * from account where ac_no='"+s1.get()+"'")

        
        x=0
        y=100
            
        for r1 in r:
            Label(f6,text=r1[0],font=("",11),bg="#091e42",fg="white").place(x=x,y=y,width=120)
            x+=120
            Label(f6,text=r1[1],font=("",11),bg="#091e42",fg="white").place(x=x,y=y,width=120)
            x+=120
            Label(f6,text=r1[2],font=("",11),bg="#091e42",fg="white").place(x=x,y=y,width=120)
            x+=120
            Label(f6,text=r1[3],font=("",11),bg="#091e42",fg="white").place(x=x,y=y,width=120)
            x+=120
               
            x=0
        """else:
            messagebox.showinfo('Title','Result found!')"""
        db.commit()
        db.close()
        
                   
    b1=Button(f6,text="SEARCH",command=searchdata1)
    b1.place(x=400,y=50)




#--------------------------------UPDATE DATA------------------------------------------
#Update account details
def updateAccountInfo(n):
    f7=Frame(bg="#091e42")
    n.add(f7,text="Update Account Info.")
    #f4.place(x=0,y=0, width=600, height=400)

    h1=StringVar()
    
     
    u1=Label(f7,text="Account No.",bg="#091e42",fg="white", font=("",11))
    u1.place(x=100,y=50)
    e1=Entry(f7,font=("",11),textvariable=h1)
    e1.place(x=200,y=50, width=130)

   
    def updatedata1():
        db=sqlite3.connect('Bank.db')
        cr=db.cursor()
        r=cr.execute("select * from account where ac_no='"+h1.get()+"'")
        for r1 in r:
            h2=StringVar()
            h3=StringVar()
            h4=StringVar()
            h5=StringVar()

            u3=Label(f7,font=("",11),text="Full Name", bg="#091e42",fg='white')
            u3.place(x=200,y=100)
            u4=Entry(f7,font=("",11), bg="#091e42",fg='white',textvariable=h2)
            u4.insert(0,r1[1])
            u4.place(x=300,y=100)


            u5=Label(f7,font=("",11),text="State/City", bg="#091e42",fg='white')
            u5.place(x=200,y=150)
            u6=Entry(f7,font=("",11), bg="#091e42",fg='white',textvariable=h3)
            u6.insert(0,r1[2])
            u6.place(x=300,y=150)

            u7=Label(f7,font=("",11),text="Balance", bg="#091e42",fg='white')
            u7.place(x=200,y=200)
            u8=Entry(f7,font=("",11), bg="#091e42",fg='white',textvariable=h4)
            u8.insert(0,r1[3])
            u8.place(x=300,y=200)

            #u9=Label(f7,font=("",11),text="Math is", bg="#091e42",fg='white')
            #u9.place(x=200,y=250)
            #u10=Entry(f7,font=("",11), bg="#091e42",fg='white',textvariable=h5)
            #u10.insert(0,r1[4])
            #u10.place(x=300,y=250)

            def updatedata1():
                db=sqlite3.connect("Bank.db")
                cr=db.cursor()
                cr.execute("update account set f_name='"+h2.get()+"',city='"+h3.get()+"',amount='"+h4.get()+"' where ac_no='"+h1.get()+"' ")
                db.commit()
                db.close()
                showalldata1(f55)
                messagebox.showinfo("Title",'Updated Sucssfull..')
                h2.set("")
                h3.set("")
                h4.set("")
                h5.set("")
                

            b11=Button(f7,font=("",11),text="Update",command=updatedata1)
            b11.place(x=250,y=310,width=80,height=40)
            
        
            
    b1=Button(f7,text="SEARCH",command=updatedata1)
    b1.place(x=400,y=50)


#-----------------------------------------DELETE ACCOUNT----------------------------------------------
#DELETE ACCOUNT
def deleteAccount(n):
    f8=Frame(bg="#091e42")
    n.add(f8,text="Delete Account")
    #f4.place(x=0,y=0, width=600, height=400)

    m1=StringVar()
    u0=Label(f8, text='ACCOUNT GET DELETED PERMANENTLY',bg="#091e42",fg="white", font=("",15)).place(x=95,y=0)

    u1=Label(f8,text="Account No.",bg="#091e42",fg="white", font=("",11))
    u1.place(x=100,y=50)
    e1=Entry(f8,font=("",11),textvariable=m1)
    e1.place(x=200,y=50, width=130)

    def deletedata1():
        db=sqlite3.connect('Bank.db')
        c=db.cursor()
        c.execute("delete from account where ac_no='"+m1.get()+"'")
        messagebox.showinfo("Title","Deleted Sucesfully..")
        db.commit()
        db.close()
        showalldata1(f55)
        m1.set("")

    b1=Button(f8,text="Delete",font=("",11),command=deletedata1)
    b1.place(x=400,y=50)



def logoutAccount(n):
    f9=Frame(bg="#091e42")
    n.add(f9,text="LogOut")
    #f4.place(x=0,y=0, width=600, height=400)





        

#--------------------HOME SCREEN----------------------------

#Home Screen
def home():
    # first frame
    f1=Frame(bg='#091e42')
    f1.place(x=0,y=0, width=600,height=400)

    #Welcome text
    u1=Label(f1,text="PROGRAMMERS  BANK OF INDIA",bg="#091e42",fg="white", font=("",17))
    u1.place(x=120,y=30)


    # Login Button
    b1=Button(f1,text='LogIn', command=login)
    b1.place(x=220,y=100, width=80, height=40)
    #Register Button
    b2=Button(f1, text="Register" ,command=regis)
    b2.place(x=310,y=100, width=80,height=40)



home()

t.mainloop()
