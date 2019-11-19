from tkinter import *
def student_login():
    root=Tk()
    root.title("LBMS")
    l1=Label(root,text="Student-Section",font=('times new roman',30,"bold"),bg="BLUE",fg="black",width="20")
    l1.grid(row=1,column=1,columnspan="5")

    b1=Button(root,text="Book_Type_A",font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="red",activeforeground="black",width="30",height="3")
    b1.grid(row=5,column=2)

    b1=Button(root,text="Book_Type_B",font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="red",activeforeground="black",width="30",height="3")
    b1.grid(row=7,column=2)

    b1=Button(root,text="Book_Type_C",font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="red",activeforeground="black",width="30",height="3")
    b1.grid(row=9,column=2)

    b1=Button(root,text="Book_Type_D",font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="red",activeforeground="black",width="30",height="3")
    b1.grid(row=11,column=2)


    b1=Button(root,text="SEARCH_ANOTHER_TYPE",font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="PURPLE",activeforeground="grey",width="30",height="3")
    b1.grid(row=17,column=2)

    b1=Button(root,text="EXIT",font=('times new roman',10,"bold"),bg="RED",fg="YELLOW",activebackground="BLACK",activeforeground="grey",width="15",height="3")
    b1.grid(row=17,column=1)

    b1=Button(root,text="LOGOUT",font=('times new roman',10,"bold"),bg="RED",fg="YELLOW",activebackground="BLACK",activeforeground="grey",width="15",height="3")
    b1.grid(row=17,column=3)

    root.mainloop()
    
