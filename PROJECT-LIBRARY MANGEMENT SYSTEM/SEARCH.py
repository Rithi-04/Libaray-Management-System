import mysql.connector
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import*
from ISSUE import*
from RETURN import*
from VIEW import*
from ISSUEDBOOK import*
mydb=mysql.connector.connect(host='localhost',user="root",password="",database="triocoders")
mycr=mydb.cursor()
def searchbook():
    global book1,Canvas1,con,cur,bookTable,root
    root = Tk()
    root.title("SEARCH BOOK DETAILS")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    mydb=mysql.connector.connect(host='localhost',user="root",password="",database="triocoders")
    mycr=mydb.cursor()
       
    bookTable = "libdatabase" 

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#DEBA9D")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#310B0B",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="SEARCH BOOKS", bg='#5C3D2E', fg='white',font=('Forte',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    viewbtn=Button(root,text="ALL BOOKS",bg="#C06C84",fg='black',font=('Stencil',15),command=viewallbook)
    viewbtn.place(relx=0.40,rely=0.3, relwidth=0.25,relheight=0.08)

    authorbtn=Button(root,text="AUTHOR WISE",bg="#6C5B7B",fg='black',font=('Stencil',15),command=authorwise)
    authorbtn.place(relx=0.40,rely=0.4, relwidth=0.25,relheight=0.08)

    genrebtn=Button(root,text="GENRE WISE",bg="#355C7D",fg='black',font=('Stencil',15),command=genrewise)
    genrebtn.place(relx=0.40,rely=0.5, relwidth=0.25,relheight=0.08)

    issuedbtn=Button(root,text="ISSUED BOOK",bg="#EAFFD0",fg='black',font=('Stencil',15),command=issued)
    issuedbtn.place(relx=0.40,rely=0.6, relwidth=0.25,relheight=0.08)

            
    issuebtn=Button(root,text="ISSUE",bg="#FE4365",fg='black',font=('Impact',15),command=issuebook)
    issuebtn.place(relx=0.10,rely=0.9, relwidth=0.18,relheight=0.08)

    returnbtn=Button(root,text="RETURN",bg="#83AF9B",fg='black',font=('Impact',15),command=returnbook)
    returnbtn.place(relx=0.40,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="QUIT",bg='#D6E5FA', fg='black',font=('Impact',15),command=root.destroy)
    quitBtn.place(relx=0.70,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()
