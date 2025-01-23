from tkinter import*
import mysql.connector
from tkinter import messagebox
def returnbookmain():
    cusname=book1.get()
    bkno=book3.get()
    
    bkname=book4.get()
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='triocoders')
    mycr=mydb.cursor()
    mycr.execute("delete from customer_details where bookno="+bkno+"")
    mycr.execute("update libdatabase set status='AVAILABLE' where bookno="+bkno+"")
    mydb.commit()
    messagebox.showinfo("RETURNED")
    
    root.destroy
def returnbook():
    global book1,book3,book4,Canvas1,con,cur,bookTable,root
    root = Tk()
    root.title("RETURN BOOK")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    mydb=mysql.connector.connect(host='localhost',user="root",password="",database="triocoders")
    mycr=mydb.cursor()

    
    bookTable = "libdatabase" 

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#E7FBBE")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="white",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="RETURN BOOKS", bg='black', fg='white',font=('Forte',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    
    lb1 = Label(labelFrame,text="CUSTOMER NAME:", bg='black', fg='white',font=('Stencil',12))
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    book1 = Entry(labelFrame)
    book1.place(relx=0.4,rely=0.2, relwidth=0.50, relheight=0.08)

    
    lb3 = Label(labelFrame,text="BOOK NO:", bg='black', fg='white',font=('Stencil',12))
    lb3.place(relx=0.05,rely=0.35, relheight=0.08)
        
    book3= Entry(labelFrame)
    book3.place(relx=0.4,rely=0.35, relwidth=0.50, relheight=0.08)

    lb4 = Label(labelFrame,text="BOOK NAME:", bg='black', fg='white',font=('Stencil',12))
    lb4.place(relx=0.05,rely=0.50, relheight=0.08)
        
    book4 = Entry(labelFrame)
    book4.place(relx=0.4,rely=0.50, relwidth=0.50, relheight=0.08)

    SubmitBtn = Button(root,text="SUBMIT",bg='#D6E5FA', fg='black',font=('Impact',15),command=returnbookmain)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="QUIT",bg='#D6E5FA', fg='black',font=('Impact',15),command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
 
