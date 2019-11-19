from tkinter import *
import mysql.connector as con


def delete():
     
     mydb = con.connect(host="localhost",user="root",passwd="anurag",database="db")
    
     mycursor = mydb.cursor()
     qr="delete from student where username='{0}'".format(v.get())    
     mycursor.execute(qr)
     v.set("")
    
     
     if(mycursor.rowcount>0):
         L1.config(text="Record deleted")
         
     else:
         L1.config(text=" Record Not found")
         
     mydb.commit()

root=Tk()
#root.configure(bg='pink')
root.title("Admin Section")
l1=Label(root,text="Administrator-Section",font=('times new roman',30,"bold"),bg="BLUE",fg="black",width="20")
l1.grid(row=1,column=0,columnspan="5")

l2=Label(root,text="Remove Librarian Member",font=('times new roman',16,"bold"),bg="yellow",fg="purple")
l2.grid(row=2,column=0,columnspan=2)
 
l3=Label(root,text="Enter Identical User_Name",font=('times new roman',16,"bold"),bg="pink",fg="purple")
l3.grid(row=3,column=0)
     
v=StringVar()

e1=Entry(root,width=30,justify=LEFT,textvariable=v)
e1.grid(row=3,column=1)

btn1=Button(root,text="Remove",command=delete,bg="red", fg="black",padx=10,pady=2,font=("Arial Bold",10),bd=4)
btn1.grid(column=1,row=4)
L1=Label(root,text="",font=('times new roman',10,"bold"))
L1.grid(row=4,column=0)

root.mainloop()
