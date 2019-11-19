from tkinter import *
def renew():
    root=Tk()
    root.configure(bg='yellow')
    global l1;
    root.title("Renew Password")
    l1=Label(root,text="This Service Is \n Temporary Unavalible",font=('times new roman',20,"bold"),bg="yellow",fg="black")
    l1.pack()
    root.after(2000, root.destroy)
    root.mainloop()


