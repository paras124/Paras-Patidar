from tkinter import*
from Lbrn_section import*
import mysql.connector as con


def login(root,txt1,txt2):
    
    mydb = con.connect(host="localhost",user="root",passwd="anurag",database="lbms")
    
    mycursor = mydb.cursor()
   
    qr="select * from lbrn where username='{0}' and password='{1}'".format(txt1.get(),txt2.get())
    
    mycursor.execute(qr)
    myresult = mycursor.fetchall()
    
    if(mycursor.rowcount>0):
        print("Success")
        Lbrn_login()
    else:
        error=Label(root,text="Incorrect password or user name")
        error.place(x=250,y=300)
        
    
    mydb.commit()


def new_win2():
    global txt1,txt2;
    r= Tk()
    r.title("LBMS")
    
    lbl=Label(r,text="Library Management System",font=("Arial Bold",30),bg="blue", fg="black")
    lbl.grid(column=0,row=0,columnspan=4)

    lb2=Label(r,text="Libraian Login",font=("Arial Bold",20),bg="red", fg="blue")
    lb2.grid(column=1,row=1,columnspan=3)

    lb3=Label(r,text="Username:-",font=("Arial Bold",20))
    lb3.grid(column=1,row=2)
    
    txt1= Entry(r,width=25)
    txt1.grid(column=2,row=2)
    


    lb4=Label(r,text="Password:-",font=("Arial Bold",20))
    lb4.grid(column=1, row=3)
    
    txt2=Entry(r,width=25)
    txt2.grid(column=2, row=3)

    btn=Button(r,text="Log In",command=lambda:login(r,txt1,txt2),font=("Arial Bold",10),bg="yellow", fg="black")
    btn.grid(column=2,row=4)
    r.mainloop()

    






    
