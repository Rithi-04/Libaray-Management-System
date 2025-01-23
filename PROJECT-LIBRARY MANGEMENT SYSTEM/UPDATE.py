import mysql.connector
import smtplib
from email.message import EmailMessage
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import*
mydb=mysql.connector.connect(host='localhost',user="root",password="",database="triocoders")
mycr=mydb.cursor()
def updatebookcore():
    try:
        nm=bk1.get()
        a=bk2.get()
        p=bk3.get()
        g=bk4.get()
        s=bk5.get()
        n1=book1.get() 
        mycr.execute("update libdatabase set bookname='{}' where bookno={}".format(nm,n1))
        mycr.execute("update libdatabase set bookauthor='{}' where bookno={}".format(a,n1))
        mycr.execute("update libdatabase set bookpublisher='{}' where bookno={}".format(p,n1))
        mycr.execute("update libdatabase set bookgenre='{}' where bookno={}".format(g,n1))
        mycr.execute("update libdatabase set status='{}' where bookno={}".format(s,n1))
        messagebox.showinfo("UPDATED")
    except:
        messagebox.showinfo("FAILED")
    
def updatebookmain():
    global bk1,bk2,bk3,bk4,bk5,Canvas1,con,cur,bookTable,root
    
    top = Tk()
    top.title("NEW BOOK DETAILS")
    top.minsize(width=400,height=400)
    top.geometry("600x500")

    mydb=mysql.connector.connect(host='localhost',user="root",password="",database="triocoders")
    mycr=mydb.cursor()

    
    bookTable="libdatabase" 

    Canvas2=Canvas(top)
    
    Canvas2.config(bg="#DEEEEA")
    Canvas2.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(top,bg="#FEFFDE",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="ENTER NEW BOOK DETAILS", bg='black', fg='white', font=('Forte',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(top,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)


    lb1 = Label(labelFrame,text="NEW BOOK NAME",bg='black', fg='white',font=('Stencil',15))
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bk1 = Entry(labelFrame)
    bk1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

    lb2 = Label(labelFrame,text="NEW AUTHOR NAME",bg='black', fg='white',font=('Stencil',15))
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bk2 = Entry(labelFrame)
    bk2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)

    lb3= Label(labelFrame,text="NEW PUBLISHER",bg='black', fg='white',font=('Stencil',15))
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bk3= Entry(labelFrame)
    bk3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

    lb4= Label(labelFrame,text="NEW GENRE",bg='black', fg='white',font=('Stencil',15))
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    bk4 = Entry(labelFrame)
    bk4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)

    lb5= Label(labelFrame,text="AVAILABILITY",bg='black', fg='white',font=('Stencil',15))
    lb5.place(relx=0.05,rely=0.80, relheight=0.08)
        
    bk5= Entry(labelFrame)
    bk5.place(relx=0.3,rely=0.80, relwidth=0.62, relheight=0.08)

    SubmitBtn = Button(top,text="SUBMIT",bg='#D6E5FA', fg='black',font=('Impact',15),command=updatebookcore)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    quitBtn = Button(top,text="QUIT",bg='#D6E5FA', fg='black',font=('Impact',15),command=top.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    top.mainloop()
            

def updatebook():
    global book1,Canvas1,con,cur,bookTable,root
    root = Tk()
    root.title("UPDATE BOOK DETAILS")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    mydb=mysql.connector.connect(host='localhost',user="root",password="",database="triocoders")
    mycr=mydb.cursor()

    
    bookTable = "libdatabase" 

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#EE99A0")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="white",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="UPDATE BOOK DETAILS", bg='black', fg='white', font=('Forte',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    lb1 = Label(labelFrame,text="NO TO BE UPDATED", bg='black', fg='white',font=('Stencil',15))
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    book1 = Entry(labelFrame)
    book1.place(relx=0.5,rely=0.2, relwidth=0.45, relheight=0.08)

    SubmitBtn = Button(root,text="SUBMIT",bg='#D6E5FA', fg='black',font=('Impact',15),command=updatebookmain)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#D6E5FA', fg='black',font=('Impact',15),command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()


