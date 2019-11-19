from tkinter import *
import mysql.connector as con

def save():
    mydb = con.connect(host="localhost",user="root",passwd="anurag",database="lbms")
    mycursor = mydb.cursor()
    print(e7.get())
    sql = "insert into student(username,password,afname,alname,ffname,flname,gender,aadharnum,mobnum,email) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}')".format(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get())
    print(sql)
    mycursor.execute(sql)
    
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

  # v1.set("")
  #v.set("") '''
    
def Add_student():
    root=Tk()
    root.title("Add Student")
    global e1,e2,e3,e4,e5,e6,e7,e8,e9,e10;

    lbl=Label(root,text="NATIONAL LIBRARY",font=("Arial Bold",30),bg="skyblue", height=1,width=37, fg="blue")
    lbl.grid(column=0,row=0,columnspan=15)

    #text1 = Text(root, height=30, width=111)
    #photo=PhotoImage(file='lib2.png')
    #text1.insert(END,'\n')
    #text1.image_create(END, image=photo)
    #text1.grid(column=0,row=1,rowspan=20,columnspan=10)
    
    l1=Label(root,text="Add New Student",font=('times new roman',16,"bold"),fg="purple")
    l1.grid(row=2,column=0)

    l1=Label(root,text="*General Information (Filled Same As Any valid identity)*",font=('times new roman',14,"bold"),fg="Red")
    l1.grid(row=3,column=0,columnspan=5)

    l1=Label(root,text="Name(Applicant):- ",font=('times new roman',15,"bold"),fg="black")
    
    e3=Entry(root)
    
    e4=Entry(root)
    l1.grid(row=4,column=0)
    e3.grid(row=4,column=1)
    e4.grid(row=4,column=2)

    l1=Label(root,text="First name",font=('times new roman',12,"bold"),fg="black")
    l1.grid(row=5,column=1)
    l1=Label(root,text="Last name",font=('times new roman',12,"bold"),fg="black")
    l1.grid(row=5,column=2)


    l1=Label(root,text="Father Name:-",font=('times new roman',15,"bold"),fg="black")
    
    e5=Entry(root)
    
    e6=Entry(root)
    l1.grid(row=6,column=0)
    e5.grid(row=6,column=1)
    e6.grid(row=6,column=2)

    l1=Label(root,text="First name",font=('times new roman',12,"bold"),fg="black")
    l1.grid(row=7,column=1)
    l1=Label(root,text="Last name",font=('times new roman',12,"bold"),fg="black")
    l1.grid(row=7,column=2)

    e7=StringVar(value="Male")
    l1=Label(root,text="Gender",font=('times new roman',15,"bold"),fg="black")
    l1.grid(row=8,column=0)
    global r1,r2;
    r1=Radiobutton(root,text="Male",variable=e7,value="Male")
    r1.grid(row=8,column=1)
    r2=Radiobutton(root,text="Female",variable=e7,value="Female")
    r2.grid(row=8,column=2)
  

    c1=Checkbutton(root,text="Aadhar No.:-",font=('times new roman',15,"bold"),fg="black")
    
    e8=Entry(root)
    c1.grid(row=10,column=0)
    e8.grid(row=10,column=1)

    c1=Checkbutton(root,text="Mobile No.:-",font=('times new roman',15,"bold"),fg="black")
  
    e9=Entry(root)
    c1.grid(row=11,column=0)
    e9.grid(row=11,column=1)



    l1=Label(root,text="*Generate Login Details (User_Name & Password)*",font=('times new roman',14,"italic"),fg="Red")
    l1.grid(row=12,column=1)


    l1=Label(root,text="User_Name",font=('times new roman',15,"bold"),fg="black")
    l1.grid(row=13,column=0)
    
    e1=Entry(root)
    e1.grid(row=13,column=1)

    l1=Label(root,text="Email_id",font=('times new roman',15,"bold"),fg="black")
    l1.grid(row=14,column=0)
    
    e10=Entry(root)
    e10.grid(row=14,column=1)

    l1=Label(root,text="Password",font=('times new roman',15,"bold"),fg="black")
    l1.grid(row=15,column=0)
    
    e2=Entry(root)
    e2.grid(row=15,column=1)

    l1=Label(root,text="Re-Password",font=('times new roman',15,"bold"),fg="black")
    l1.grid(row=16,column=0)
    e2=Entry(root)

    e2.grid(row=16,column=1)


    btn4=Button(root,text="Save&Submit",command=save,bg="red", fg="black",padx=10,pady=2,font=("Arial Bold",10),bd=4)
    btn4.grid(column=1,row=17)

    root.mainloop()
