from tkinter import *
import mysql.connector
import tkinter.messagebox

def Save():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="anurag",database="lbms")
    
    mycursor = mydb.cursor()
    qr="insert into bookdata values('{0}','{1}',{2},'{3}','{4}')".format(textname2.get(),textname3.get(),textname4.get(),textname5.get(),textname6.get())
    print(qr)
    mycursor.execute(qr)
    if(mycursor.rowcount>0):
        tkinter.messagebox.showinfo("Information","Data inserted Successfully")
    mydb.commit()
   

def Add_book():
    r=Tk()
    r.configure(background='skyblue',height=600,width=500)

    r.geometry('350x400')
    
    lblname=Label(r,text="Add Book",font=('times new roman',22),background='skyblue', foreground="Red")
    lblname.place(x=140,y=30)

    lblname=Label(r,text="Book_Name",height=2,width=12)
    lblname.configure(background='blue', foreground="white")
    lblname.place(x=40,y=80)

    
    global textname2
    textname2=Entry(r)
    textname2.place(x=150,y=90)

    lblname3=Label(r,text="Book_Id",height=2,width=12)
    lblname3.configure(background='blue', foreground="white")
    lblname3.place(x=40,y=130)

    global textname3
    textname3=Entry(r)
    textname3.place(x=150,y=140)
    
    lblname8=Label(r,text="Author_Name",height=2,width=12)
    lblname8.configure(background='blue', foreground="white")
    lblname8.place(x=40,y=180)
    
    global textname4
    textname4=Entry(r)
    textname4.place(x=150,y=190)


    lblname5=Label(r,text="Publication_Year",height=2,width=12)
    lblname5.configure(background='blue', foreground="white")
    lblname5.place(x=40,y=230)

   
    global textname5
    textname5=Entry(r)
    textname5.place(x=150,y=240)

    lblname7=Label(r,text="Book_Type",height=2,width=12)
    lblname7.configure(background='blue', foreground="white")
    lblname7.place(x=40,y=280)

    global textname6
    textname6=Entry(r)
    textname6.place(x=150,y=290)


    insert=Button(r,text="Submit",command=Save,height=1,width=8)
    insert.configure(background='blue', foreground="white")
    insert.place(x=170,y=320)


    r.mainloop
   
    
