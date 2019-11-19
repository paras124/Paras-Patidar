from tkinter import*
from Admin_section import*
import mysql.connector as con

def a_login(root,v1,v2):
    mydb = con.connect(host="localhost",user="root",passwd="anurag",database="lbms")
    
    mycursor = mydb.cursor()
    qr="select * from admin where username='{0}' and password='{1}'".format(v1.get(),v2.get())
    
    mycursor.execute(qr)
    myresult = mycursor.fetchone()
    if(myresult):
        usr=myresult[0]
        pwd=myresult[1]
        print("Success")
        admin_login()
        
    else:
        error=Label(root,text="Incorrect passore or user name")
        error.place(x=250,y=300)
        admin_login()
    
        mydb.commit()
        


def new_win1():
    r= Tk()
    r.title("LBMS")
    global v1,v2;
    lbl=Label(r,text="Library Management System",font=("Arial Bold",30),bg="blue", fg="black")
    lbl.grid(column=0,row=0,columnspan=4)

    lb2=Label(r,text="Admin Log In",font=("Arial Bold",20),bg="red", fg="blue")
    lb2.grid(column=1,row=1,columnspan=3)

    lb3=Label(r,text="Username:-",font=("Arial Bold",20))
    lb3.grid(column=1,row=2)
    #v1=StringVar()
    
    txt1= Entry(r,width=25)
    txt1.grid(column=2,row=2)

    lb4=Label(r,text="Password:-",font=("Arial Bold",20))
    lb4.grid(column=1, row=3)
    #v2=StringVar()
    
    txt2=Entry(r,width=25)
    txt2.grid(column=2, row=3)
    v1=txt1
    v2=txt2

    btn=Button(r,text="Log In",command=lambda:a_login(r,v1,v2),font=("Arial Bold",10),bg="yellow", fg="black")
    btn.grid(column=2,row=4)

    r.mainloop()

