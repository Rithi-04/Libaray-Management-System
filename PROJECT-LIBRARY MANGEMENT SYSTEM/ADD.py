import mysql.connector
from tkinter import messagebox
from tkinter import*

def addbook():
    try:
        no=book1.get()
        nam=book2.get()
        author=book3.get()
        publisher=book4.get()
        genre=book5.get()
        status=book6.get()
        mydb=mysql.connector.connect(host='localhost',user='root',password='',database='triocoders')
        mycr=mydb.cursor()
        mycr.execute("insert into libdatabase values("+no+",'"+nam+"','"+author+"','"+publisher+"','"+genre+"','"+status+"')")
        mydb.commit()
        messagebox.showinfo("ADDED")
    except:
        messagebox.showinfo("FAILED",'each BOOK should have a unique number dont try to use other no')

    
        
def addbookmain():
    
    global book1,book2,book3,book4,book5,book6,Canvas1,con,cur,bookTable,top
    
    top = Tk()
    top.title("ADD BOOK DETAILS")
    top.minsize(width=400,height=400)
    top.geometry("600x500")

    mydb=mysql.connector.connect(host='localhost',user="root",password="",database="triocoders")
    mycr=mydb.cursor()

    
    bookTable = "libdatabase" 

    Canvas1 = Canvas(top)
    
    Canvas1.config(bg="#9E7777")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(top,bg="#FFEDDA",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="ADD BOOKS", bg='black', fg='white', font=('Forte',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(top,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.6)
        
    # Book ID
    lb1 = Label(labelFrame,text="NO", bg='black', fg='white',font=('Stencil',15))
    lb1.place(relx=0.05,rely=0.1, relheight=0.08)
        
    book1 = Entry(labelFrame)
    book1.place(relx=0.4,rely=0.1, relwidth=0.50, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="TITLE", bg='black', fg='white',font=('Stencil',15))
    lb2.place(relx=0.05,rely=0.25, relheight=0.08)
        
    book2= Entry(labelFrame)
    book2.place(relx=0.4,rely=0.25, relwidth=0.50, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="AUTHOR", bg='black', fg='white',font=('Stencil',15))
    lb3.place(relx=0.05,rely=0.40, relheight=0.08)
        
    book3 = Entry(labelFrame)
    book3.place(relx=0.4,rely=0.40, relwidth=0.50, relheight=0.08)
        
    # Book publisher
    lb4 = Label(labelFrame,text="PUBLISHER", bg='black', fg='white',font=('Stencil',15))
    lb4.place(relx=0.05,rely=0.55, relheight=0.08)
        
    book4 = Entry(labelFrame)
    book4.place(relx=0.4,rely=0.55, relwidth=0.50, relheight=0.08)

    #book genre
    lb5 = Label(labelFrame,text="GENRE", bg='black', fg='white',font=('Stencil',15))
    lb5.place(relx=0.05,rely=0.70, relheight=0.08)
        
    book5 = Entry(labelFrame)
    book5.place(relx=0.4,rely=0.70, relwidth=0.50, relheight=0.08)

    lb6= Label(labelFrame,text="AVAILABILITY", bg='black', fg='white',font=('Stencil',15))
    lb6.place(relx=0.05,rely=0.85, relheight=0.08)
        
    book6 = Entry(labelFrame)
    book6.place(relx=0.4,rely=0.85, relwidth=0.50, relheight=0.08)


     
        

    #Submit Button
    SubmitBtn = Button(top,text="SUBMIT",bg='#D6E5FA', fg='black',font=('Impact',20),command=addbook)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(top,text="QUIT",bg='#D6E5FA', fg='black',font=('Impact',20),command=top.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    top.mainloop()
    
