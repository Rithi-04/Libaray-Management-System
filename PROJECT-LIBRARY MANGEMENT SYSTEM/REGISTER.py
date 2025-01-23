import mysql.connector
from tkinter import messagebox
from DASHBOARD import*
mydb=mysql.connector.connect(host='localhost',user="root",password="",database="triocoders")
mycr=mydb.cursor()
mycr.execute("create table if not exists register(username varchar(25) not null,emailid varchar(50) not null,password varchar(50) not null)")
def dashboardf():
    root.destroy()
    dashboard()
def bookregister():
    pa=bookInfo3.get()
    cpa=bookInfo4.get()
    un=bookInfo1.get()
    em=bookInfo2.get()
    
    try:        
        if pa==cpa:
            mycr.execute("insert into register values('{}','{}','{}')".format(un,em,pa))
            mydb.commit()
            messagebox.showinfo("REGISTERED",un)
            dashboardf()
    except:
        messagebox.showinfo("REGISTER FAILED")
def regis():
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,root
    
    root=Tk()
    root.title("REGISTER")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#DACC96")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#000000",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="REGISTER\n(fill all the details)", bg='black', fg='white', font=('Forte',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
    
    lb1 = Label(labelFrame,text="USERNAME:", bg='black', fg='white',font=('Stencil',15))
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.4,rely=0.2, relwidth=0.50, relheight=0.08)
        

    lb2 = Label(labelFrame,text="MAIL-ID(GMAIL):", bg='black', fg='white',font=('Stencil',15))
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.4,rely=0.35, relwidth=0.50, relheight=0.08)
        
    
    lb3 = Label(labelFrame,text="SET CODE:", bg='black', fg='white',font=('Stencil',15))
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.4,rely=0.50, relwidth=0.50, relheight=0.08)
    
    
    lb4 = Label(labelFrame,text="CONFIRM CODE:", bg='black', fg='white',font=('Stencil',15))
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.4,rely=0.65, relwidth=0.50, relheight=0.08)

    SubmitBtn = Button(root,text="SUBMIT",bg='#D6E5FA', fg='black',font=('Impact',15),command=bookregister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="QUIT",bg='#D6E5FA', fg='black', font=('Impact',15),command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    root.mainloop()
