from tkinter import *
from Create_Acc import *
root=Tk()
root.title("Banking management system")
l1=Label(root,text="NATIONAL BANK OF INDIA",font=('times new roman',25,"bold"),bg="skyblue",fg="red",)
l1.grid(row=1,column=1,columnspan="5")
l1=Label(root,text="WEL-COME",font=('times new roman',15,"italic"),fg="blue")
l1.grid(row=2,column=1)

l1=Label(root,text="MAIN MENU",font=('times new roman',15,"bold"))
l1.grid(row=3,column=2)
b1=Button(root,text="CREATE NEW ACCOUNT",command=new_win,font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="red",activeforeground="black",width="30",height="3")
b1.grid(row=5,column=2)

b1=Button(root,text="DEPOSITE AMOUNT",font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="red",activeforeground="black",width="30",height="3")
b1.grid(row=7,column=2)

b1=Button(root,text="WITHDRAW AMOUNT",font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="red",activeforeground="black",width="30",height="3")
b1.grid(row=9,column=2)

b1=Button(root,text="BALANCE ENQUIRY",font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="red",activeforeground="black",width="30",height="3")
b1.grid(row=11,column=2)

b1=Button(root,text="ALL ACCOUNT HOLDER LIST",font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="red",activeforeground="black",width="30",height="3")
b1.grid(row=13,column=2)

b1=Button(root,text="CLOSE AN ACCOUNT",font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="red",activeforeground="grey",width="30",height="3")
b1.grid(row=15,column=2)

b1=Button(root,text="MODIFY AN ACCOUNT",font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="red",activeforeground="grey",width="30",height="3")
b1.grid(row=17,column=2)

b1=Button(root,text="LOAN HOLDER ACCOUNT ",font=('times new roman',10,"bold"),bg="skyblue",fg="red",activebackground="red",activeforeground="grey",width="30",height="3")
b1.grid(row=19,column=2)

b1=Button(root,text="EXIT",bg="skyblue",font=('times new roman',10,"bold"),fg="red",activebackground="red",activeforeground="grey",width="15",)
b1.grid(row=21,column=1)

b1=Button(root,text="LOGOUT",bg="skyblue",font=('times new roman',10,"bold"),fg="red",activebackground="red",activeforeground="grey",width="15")
b1.grid(row=21,column=3)

root.mainloop()
