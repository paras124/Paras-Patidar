from tkinter import *
from Add_lbrn import *
from del_lbrn import *
from view_student import *
from view_lbrn import *
from view_book import *
import tkinter.messagebox
import mysql.connector

def update(r):
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="anurag",database="lbms")
    
    mycursor = mydb.cursor()
    qr="update admin set password=('{1}') where username=('{0}')".format(e1.get(),e2.get())
    print(qr)
    mycursor.execute(qr)
    if(mycursor.rowcount>0):
        tkinter.messagebox.showinfo("Information","Password Updated Successfully")
        r.after(2000, r.destroy)
    mydb.commit()

def renewpwd(r):
    r=Tk()
    r.configure(bg='pink')
    r.title("Admin Section")

    lblname=Label(r,text="Username",height=1,width=12)
    lblname.configure(background='blue', foreground="white")
    lblname.grid(row=1,column=1)

    
    global e1;
    e1=Entry(r)
    e1.grid(row=1,column=2)

    lblname3=Label(r,text="New-password",height=1,width=12)
    lblname3.configure(background='blue', foreground="white")
    lblname3.grid(row=2,column=1)

    global e2;
    e2=Entry(r)
    e2.grid(row=2,column=2)

    button=Button(r,text="Update",command=lambda:update(r),font=('times new roman',10,"bold"),bg="yellow",fg="black")
    button.grid(row=3,column=2,columnspan=2)
    r.after(2000, r.destroy)
 
def admin_login():
    root=Tk()
    root.configure(bg='pink')
    root.title("Admin Section")
    l1=Label(root,text="Administrator-Section",font=('times new roman',30,"bold"),bg="BLUE",fg="black",width="20")
    l1.grid(row=1,column=1,columnspan="5")

    b1=Button(root,text="ADD NEW LIBRARIAN",command=add_lbrn,font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="red",activeforeground="black",width="30",height="3")
    b1.grid(row=5,column=2)

    b1=Button(root,text="REMOVE LIBRARIAN",command=remove_lbrn,font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="red",activeforeground="black",width="30",height="3")
    b1.grid(row=7,column=2)

    b1=Button(root,text="VIEW STUDENT-DATA",command=view_student,font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="red",activeforeground="black",width="30",height="3")
    b1.grid(row=9,column=2)

    b1=Button(root,text="VIEW BOOKS-DATA",command=view_book,font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="red",activeforeground="black",width="30",height="3")
    b1.grid(row=11,column=2)


    b1=Button(root,text="VIEW LIBRARIAN",command=view_lbrn,font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="red",activeforeground="grey",width="30",height="3")
    b1.grid(row=15,column=2)

    b1=Button(root,text="RENEW-PASSWORD",command=lambda:renewpwd(root),font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="PURPLE",activeforeground="grey",width="30",height="3")
    b1.grid(row=17,column=2)

    b1=Button(root,text="EXIT",font=('times new roman',10,"bold"),bg="RED",fg="YELLOW",activebackground="BLACK",activeforeground="grey",width="15",height="3")
    b1.grid(row=17,column=1)

    b1=Button(root,text="LOGOUT",font=('times new roman',10,"bold"),bg="RED",fg="YELLOW",activebackground="BLACK",activeforeground="grey",width="15",height="3")
    b1.grid(row=17,column=3)

    root.mainloop()
   


