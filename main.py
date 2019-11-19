from tkinter import*
from Admin_log import*
from lbrn_log import*
from student_log import*
r= Tk()
r.title("LBMS")
r.configure(bg='pink')


lbl=Label(r,text="NATIONAL UNIVERSITY",font=("Arial Bold",30),bg="skyblue",width=30, fg="black")
lbl.grid(column=0,row=0,columnspan=5)


lb2=Label(r,text="LIBRARY SECTION",font=("Arial Bold",15),fg="black",bg="white")
lb2.grid(column=2,row=2)

btn1=Button(r,text="Admin Log In",command=new_win1,bg="red", fg="black",padx=56,pady=15,font=("Arial Bold",12),bd=4)
btn1.grid(column=1,row=4)

btn2=Button(r,text="Libraraian Log In",command=new_win2,bg="yellow", fg="black",padx=41,pady=15,font=("Arial Bold",12),bd=4)
btn2.grid(column=2,row=5)

btn3=Button(r,text="Student Log In",command=new_win3,bg="blue", fg="black",padx=50,pady=15,font=("Arial Bold",12),bd=4)
btn3.grid(column=3,row=6)

r.mainloop()
