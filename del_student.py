from tkinter import *
import mysql.connector as con


def delete():
     
     mydb = con.connect(host="localhost",user="root",passwd="anurag",database="lbms")
    
     mycursor = mydb.cursor()
     qr="delete from student where username='{0}'".format(e1.get())    
     mycursor.execute(qr)

    
     
     if(mycursor.rowcount>0):
         L1.config(text="Record deleted")
         
     else:
         L1.config(text="Not found")
         
     mydb.commit()

def remove_student():


     root=Tk()
     global e1,L1;
     lblenroll=Label(root,text="Enter username ")
     lblenroll.pack()
     e1=Entry(root)
     e1.pack()

     btndelete=Button(root,text="Delete",command=delete)
     btndelete.pack()
     L1=Label(root,text="")
     L1.pack()

     root.mainloop()
