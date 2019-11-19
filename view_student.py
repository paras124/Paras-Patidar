from tkinter import *
import mysql.connector as con


def view():
     
     mydb = con.connect(host="localhost",user="root",passwd="anurag",database="lbms")
    
     mycursor = mydb.cursor()
     qr="select afname,alname,ffname,flname,gender,mobnum from student WHERE username='{0}'".format(e1.get())
     
     mycursor.execute(qr)
     result=mycursor.fetchone()
     if(result):
         L1.config(text="Student Data Found")
         L2.config(text=result)
         for r in result:
          print(r)
          
          
          
     else:
          L1.config(text="Not found")
         
     mydb.commit()

def display():
          mydb = con.connect(host="localhost",user="root",passwd="anurag",database="lbms")
    
          mycursor = mydb.cursor()
          qr="select afname,alname,ffname,flname,gender,mobnum from lbrn WHERE username='{0}'".format(e1.get())
     
          mycursor.execute(qr)
          result=mycursor.fetchone()
          
          f=open('view.txt','w')
          for data in result:
              f.write(str(data)+'\n')
          f.close()

          import subprocess as sp
          pName='notepad.exe'
          fName='view.txt'
          sp.Popen([pName,fName])



     

def view_student():


     root=Tk()
     global e1,L1,L2;
     lblenroll=Label(root,text="Enter username ")
     lblenroll.pack()
     e1=Entry(root)
     e1.pack()

     btndelete=Button(root,text="View",command=view)
     btndelete.pack(side=TOP)
     btndelete=Button(root,text="Print",command=display)
     btndelete.pack(side=TOP)
     L1=Label(root,text="")
     L1.pack()
     L2=Label(root,text="")
     L2.pack()                         

     root.mainloop()

