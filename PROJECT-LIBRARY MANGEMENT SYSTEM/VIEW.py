import mysql.connector
import csv
import os
from tkinter import messagebox
from tkinter import*
import tkinter as tk
from tkinter import ttk
mydb=mysql.connector.connect(host='localhost',user="root",password="",database="triocoders")
mycr=mydb.cursor()
def excelbook():
    mycr.execute("select*from libdatabase")
    res=mycr.fetchall()
    field=['BOOKNO','BOOKNAME','BOOKAUTHOR','BOOKPUBLISHER','BOOKGENRE','STATUS']
    with open("books.csv",'w',newline='')as f:
        
        wobj=csv.writer(f,delimiter=',')
        wobj.writerow(field)
        for j in res:
            wobj.writerow(j)
    with open("books.csv",'r')as fh:
        robj=csv.reader(fh)
        rows=[]
        for rec in robj:
            rows.append(rec)
    s=os.getcwd()
    p='/books.csv'
    q=s+p
    os.startfile(q)
def viewallbook():

    mycr.execute("select* from libdatabase")
    res=mycr.fetchall()
    def show():

    
        res.sort(key=lambda e: e[1], reverse=True)

        for i, (NO,NAME,AUTHOR,PUBLISHER,GENRE,STATUS) in enumerate(res, start=1):
            listBox.insert("", "end", values=(i,NO,NAME,AUTHOR,PUBLISHER,GENRE,STATUS))

    scores = tk.Tk() 
    label = tk.Label(scores, text="BOOK LIST",bg='#4FBDBA', font=("Forte",30)).grid(row=0, columnspan=3)
    # create Treeview with 3 columns
    cols = ('SNO', 'BOOKNO','NAME', 'AUTHOR','PUBLISHER','GENRE','STATUS')
    listBox = ttk.Treeview(scores, columns=cols, show='headings')
    # set column headings
    for col in cols:
        listBox.heading(col, text=col)    
    listBox.grid(row=1, column=0, columnspan=2)

    show()
    showScores = Button(scores, text = "VIEW IN EXCEL",width = 15, command =excelbook).grid(row = 4, column = 0)
    closeButton = tk.Button(scores, text="Close", width=15, command=scores.destroy).grid(row=4, column=1)
    scores.mainloop()
def authorbook():
    try:
        author=book1.get()
        mycr.execute("select * from libdatabase where bookauthor='"+author+"'")
        res=mycr.fetchall()
        def show():

        
            res.sort(key=lambda e: e[1], reverse=True)

            for i, (NO,NAME,AUTHOR,PUBLISHER,GENRE,STATUS) in enumerate(res, start=1):
                listBox.insert("", "end", values=(i,NAME,AUTHOR,PUBLISHER,GENRE,STATUS))

        scores = tk.Tk() 
        label = tk.Label(scores, text="BOOK LIST",bg='#4FBDBA', font=("Forte",30)).grid(row=0, columnspan=3)
        # create Treeview with 3 columns
        cols = ('NO', 'Name', 'AUTHOR','PUBLISHER','GENRE','STATUS')
        listBox = ttk.Treeview(scores, columns=cols, show='headings')
        # set column headings
        for col in cols:
            listBox.heading(col, text=col)    
        listBox.grid(row=1, column=0, columnspan=2)

        show()
        closeButton = tk.Button(scores, text="Close", width=15, command=scores.destroy).grid(row=4, column=1)
        scores.mainloop()
    except:
        messagebox.showinfo("FAILED",'this authorname might not exist,try seeing other author books')
def authorwise():
    global book1
    root = Tk()
    root.title("AUTHORWISE BOOK DETAILS")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    mydb=mysql.connector.connect(host='localhost',user="root",password="",database="triocoders")
    mycr=mydb.cursor()

    
    bookTable = "libdatabase" 

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#F6D7A7")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="white",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="AUTHORWISE BOOKS", bg='black', fg='white',font=('Forte',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.9,relheight=0.5)
        
    
    lb1 = Label(labelFrame,text="BOOK AUTHOR", bg='black', fg='white',font=('Stencil',12))
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    book1 = Entry(labelFrame)
    book1.place(relx=0.4,rely=0.2, relwidth=0.62, relheight=0.08)

    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',font=('Impact',15),command=authorbook)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="QUIT",bg='#f7f1e3', fg='black',font=('Impact',15),command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
def genrebook():
    try:
        genre=book2.get()
        mycr.execute("select * from libdatabase where bookgenre='"+genre+"'")
        res=mycr.fetchall()
        def show():
            res.sort(key=lambda e: e[1], reverse=True)

            for i, (NO,NAME,AUTHOR,PUBLISHER,GENRE,STATUS) in enumerate(res, start=1):
                listBox.insert("", "end", values=(i,NAME,AUTHOR,PUBLISHER,GENRE,STATUS))
        scores = tk.Tk() 
        label = tk.Label(scores, text="BOOK LIST",bg='#4FBDBA', font=("Forte",30)).grid(row=0, columnspan=3)
        cols = ('NO', 'Name', 'AUTHOR','PUBLISHER','GENRE','STATUS')
        listBox = ttk.Treeview(scores, columns=cols, show='headings')
        for col in cols:
            listBox.heading(col, text=col)    
        listBox.grid(row=1, column=0, columnspan=2)
        show()
        closeButton = tk.Button(scores, text="Close", width=15, command=scores.destroy).grid(row=4, column=1)
        scores.mainloop()
    except:
        messagebox.showinfo("FAILED",'this genre might not exist,try seeing other genre')
def genrewise():
    global book2
    root = Tk()
    root.title("GENREWISE BOOK DETAILS")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    mydb=mysql.connector.connect(host='localhost',user="root",password="",database="triocoders")
    mycr=mydb.cursor()

    
    bookTable = "libdatabase" 

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#87AAAA")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="white",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="GENREWISE BOOKS", bg='black', fg='white',font=('Forte',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.9,relheight=0.5)
        
    
    lb1 = Label(labelFrame,text="ENTER THE BOOK GENRE", bg='black', fg='white',font=('Stencil',12))
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    book2 = Entry(labelFrame)
    book2.place(relx=0.4,rely=0.2, relwidth=0.62, relheight=0.08)

    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',font=('Impact',15),command=genrebook)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="QUIT",bg='#f7f1e3', fg='black',font=('Impact',15),command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
