import mysql.connector
from tkinter import*
import PIL.Image
import PIL.ImageTk
from tkinter import messagebox
from ADD import*
from VIEW import*
from SEARCH import*
from UPDATE import*
from DELETE import*
mydb=mysql.connector.connect(host='localhost',user="root",password="",database="triocoders")
mycr=mydb.cursor()
def dashboard():
    root = Tk()
    root.title("DASHBOARD")
    root.minsize(width=400,height=400)
    root.geometry("1600x1200")

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#CCFFBD")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#fffacd",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="TRIO CODERS LIBRARY\n DASHBOARD", bg='black', fg='white', font=('Forte',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='#87AAAA')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    btn1 = Button(root,text="ADD BOOK DETAILS",bg='#632626', fg='white', font=('Stencil',15),command=addbookmain)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
        
    btn2 = Button(root,text="SEARCH BOOK DETAILS",bg='#9D5353', fg='white', font=('Stencil',15),command=searchbook)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
                
    btn4 = Button(root,text="UPDATE BOOK DETAILS",bg='#BF8B67', fg='white', font=('Stencil',15),command=updatebook)
    btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
        
    btn5 = Button(root,text="DELETE BOOK DETAILS",bg='#DACC96', fg='white', font=('Stencil',15),command=deletebook)
    btn5.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
    quitBtn = Button(root,text="QUIT",bg='#D6E5FA', fg='black', font=('Impact',15),command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()
