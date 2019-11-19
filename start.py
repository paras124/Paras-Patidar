from tkinter import *
from Admin_log import *
from lbrn_log import *
from student_log import *

r = Tk()
r.configure(bg='pink')

lbl=Label(r,text="NATIONAL LIBRARY",font=("Arial Bold",30),bg="skyblue", height=1,width=37, fg="blue")
lbl.grid(column=1,row=0,columnspan=5)

text1 = Text(r, height=30, width=30)
photo=PhotoImage(file='lib3.png')
text1.insert(END,'\n')
text1.image_create(END, image=photo)
text1.grid(column=0,row=0,rowspan=8)

text2 = Text(r, height=16, width=111)
photo1=PhotoImage(file='lib4.png')
text2.insert(END,'\n')
text2.image_create(END, image=photo1)
text2.grid(column=1,row=3,rowspan=20,columnspan=10)

lb2=Label(r,text="**Welcome To National Library**",font=("Arial Bold",18),fg="black",bg="yellow", height=1,width=30)
lb2.grid(column=3,row=1)

lb3=Label(r,text=" We hope that libraries will always exist as places for learners to find information, resources, services\n and instruction. But formats, technologies, learning needs, and our schools are evolving. And so are \n students themselves. Our entire information and communication landscapes have shifted — and this shift\n will only continue.\n\n  — @nurag & Vish@l (April 2019)",font=("Arial Bold",11),bg="pink",fg="red")
lb3.grid(column=1,row=2,columnspan=5)


lb4=Label(r,text="**Log-In From Here**",font=("Arial Bold",14),fg="green",bg="pink",padx=20,pady=4)
lb4.grid(column=0,row=3)


btn1=Button(r,text="Admin Log In",command=new_win1,bg="red", fg="black",padx=56,pady=15,font=("Arial Bold",12),bd=4)
btn1.grid(column=0,row=4)

btn2=Button(r,text="Libraraian Log In",command=new_win2,bg="yellow", fg="black",padx=41,pady=15,font=("Arial Bold",12),bd=4)
btn2.grid(column=0,row=5)

btn3=Button(r,text="Student Log In",command=new_win3,bg="blue", fg="black",padx=50,pady=15,font=("Arial Bold",12),bd=4)
btn3.grid(column=0,row=6)



r.mainloop()
