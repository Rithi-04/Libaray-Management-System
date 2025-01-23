from tkinter import*
import mysql.connector
from tkinter import messagebox
def issuebookmain():
    cusname=book1.get()
    cusno=book2.get()
    bkno=book3.get()
    bkname=book4.get()
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='triocoders')
    mycr=mydb.cursor()
    mycr.execute("insert into customer_details values('"+cusname+"','"+cusno+"','"+bkname+"','"+bkno+"')")
    mycr.execute("update libdatabase set status='UNAVAILABLE' where bookno="+bkno+"")
    mydb.commit()
    messagebox.showinfo("ISSUED")
    
    root.destroy
def issuebook():
    global book1,book2,book3,book4,Canvas1,con,cur,bookTable,root
    root = Tk()
    root.title("ISSUE BOOK")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    mydb=mysql.connector.connect(host='localhost',user="root",password="",database="triocoders")
    mycr=mydb.cursor()

    
    bookTable = "libdatabase" 

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#C8C6A7")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#92967D",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="ISSUE BOOKS", bg='black', fg='white',font=('Forte',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    
    lb1 = Label(labelFrame,text="CUSTOMER NAME:", bg='black', fg='white',font=('Stencil',15))
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    book1 = Entry(labelFrame)
    book1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

    lb2 = Label(labelFrame,text="CUSTOMER MOBILE NO:", bg='black', fg='white',font=('Stencil',15))
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    book2 = Entry(labelFrame)
    book2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)

    lb3 = Label(labelFrame,text="BOOK NO:", bg='black', fg='white',font=('Stencil',15))
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    book3= Entry(labelFrame)
    book3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

    lb4 = Label(labelFrame,text="BOOK NAME:", bg='black', fg='white',font=('Stencil',15))
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    book4 = Entry(labelFrame)
    book4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)

    SubmitBtn = Button(root,text="SUBMIT",bg='#D6E5FA', fg='black',font=('Impact',15),command=issuebookmain)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="QUIT",bg='#D6E5FA', fg='black',font=('Impact',15),command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
 
  
    
