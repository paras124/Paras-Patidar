from tkinter import *
from Add_student import *
from del_student import *
from Add_book import *
def Lbrn_login():
    root=Tk()
    root.title("LBMS")
    l1=Label(root,text="Librarian-Section",font=('times new roman',30,"bold"),bg="BLUE",fg="black",width="20")
    l1.grid(row=1,column=1,columnspan="5")

    b1=Button(root,text="ADD NEW STUDENT",command=Add_student,font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="red",activeforeground="black",width="30",height="3")
    b1.grid(row=5,column=2)

    b1=Button(root,text="REMOVE STUDENT",command=remove_student,font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="red",activeforeground="black",width="30",height="3")
    b1.grid(row=7,column=2)

    b1=Button(root,text="VIEW STUDENT-DATA",font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="red",activeforeground="black",width="30",height="3")
    b1.grid(row=9,column=2)

    b1=Button(root,text="VIEW BOOKS-DATA",font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="red",activeforeground="black",width="30",height="3")
    b1.grid(row=11,column=2)


    b1=Button(root,text="ADD NEW BOOK",command=Add_book,font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="red",activeforeground="grey",width="30",height="3")
    b1.grid(row=15,column=2)

    b1=Button(root,text="REMOVE BOOK",font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="red",activeforeground="grey",width="30",height="3")
    b1.grid(row=16,column=2)

    b1=Button(root,text="RENEW-PASSWORD",font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="PURPLE",activeforeground="grey",width="30",height="3")
    b1.grid(row=17,column=2)

    b1=Button(root,text="EXIT",font=('times new roman',10,"bold"),bg="RED",fg="YELLOW",activebackground="BLACK",activeforeground="grey",width="15",height="3")
    b1.grid(row=17,column=1)

    b1=Button(root,text="LOGOUT",font=('times new roman',10,"bold"),bg="RED",fg="YELLOW",activebackground="BLACK",activeforeground="grey",width="15",height="3")
    b1.grid(row=17,column=3)

    root.mainloop()
    
