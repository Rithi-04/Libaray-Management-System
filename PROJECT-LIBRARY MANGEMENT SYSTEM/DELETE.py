import mysql.connector
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import*
def deletebookmain():
    try:
        n=book1.get()
        mydb=mysql.connector.connect(host='localhost',user='root',password='',database='triocoders')
        mycr=mydb.cursor()
        mycr.execute("delete from libdatabase where bookno={}".format(n))
        mydb.commit()
          
            
        messagebox.showinfo("DELETED")
    except:
        messagebox.showinfo("FAILED",'this book might not exist')
    
    root.destroy
def deletebook():
    global book1,Canvas1,con,cur,bookTable,root
    root = Tk()
    root.title("DELETE BOOK DETAILS")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    mydb=mysql.connector.connect(host='localhost',user="root",password="",database="triocoders")
    mycr=mydb.cursor()
       
    bookTable = "libdatabase" 

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#FFC288")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="white",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="DELETE BOOKS", bg='black', fg='white', font=('Forte',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    lb1 = Label(labelFrame,text="BOOK NO TO BE DELETED", bg='black', fg='white',font=('Stencil',15))
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    book1 = Entry(labelFrame)
    book1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

    SubmitBtn = Button(root,text="SUBMIT",bg='#D6E5FA', fg='black',font=('Impact',15),command=deletebookmain)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="QUIT",bg='#D6E5FA', fg='black',font=('Impact',15), command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()
    
