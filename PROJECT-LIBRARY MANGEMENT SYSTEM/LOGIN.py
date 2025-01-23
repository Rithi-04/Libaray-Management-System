import mysql.connector
import smtplib
from email.message import EmailMessage
from tkinter import*
from tkinter import messagebox
from DASHBOARD import*

mydb=mysql.connector.connect(host='localhost',user="root",password="",database="triocoders")
mycr=mydb.cursor()
mycr.execute("create table if not exists register(username varchar(25) not null,emailid varchar(50) not null,password varchar(50) not null)")
mycr.execute("select*from register")
res=mycr.fetchall()
def dashboardt():
    root.destroy()
    dashboard()

def booklogin():
    global un,emailid,res
    mydb=mysql.connector.connect(host='localhost',user="root",password="",database="triocoders")
    mycr=mydb.cursor()
    mycr.execute("select*from register")
    res=mycr.fetchall()
    
    un=bookInfo1.get()
    pd=bookInfo2.get()

    bookTable="register"
    for i in res:
        flag=True
        if un==i[0] and pd==i[2]:
            emailid=i[1]
            messagebox.showinfo("SUCCESSFULLY LOGGED IN AS",un)
            flag=False
            dashboardt()
            break
        else:
            continue
    while flag==True:
        forgotpassword()
        break
    
def password():
    try:
        i=0
        while True:
            if un==res[i][0]:
                emailid=res[i][1]
                break
            else:
                i+=1


        contacts=[emailid]
        msg = EmailMessage()
        msg['Subject'] = 'HERE IS YOUR PASSWORD!! LIBRARY MANAGEMENT SYSTEM'
        msg['From'] = 'triocoders09@gmail.com'
        msg['To'] = ', '.join(contacts)
        with open("content.txt", "w") as fh:
            fh.write("check out your password here\n")
            if un == res[i][0]:
                fh.write(str(res[i][2]))
                fh.write("\nTHANK YOU!!!")
        with open("content.txt") as myfile:
            data = myfile.read()
            msg.set_content(data)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login("triocoders09@gmail.com", "KRS@2021")
            server.send_message(msg)
            server.quit()
            messagebox.showinfo("email sent successfully")
    except:
        messagebox.showinfo("FAILED",'try giving a proper gmail while registering')
def login():
    
    global bookInfo1,bookInfo2,Canvas1,root
    root=Tk()
    root.title("LOGIN PAGE")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#96CEB4")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#160040",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="LOGIN", bg='black', fg='white', font=('Forte',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
    
    lb1 = Label(labelFrame,text="USERNAME", bg='black', fg='white',font=('Stencil',10))
    lb1.place(relx=0.06,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.4,rely=0.2, relwidth=0.50, relheight=0.08)
        

    lb2 = Label(labelFrame,text="PASSWORD", bg='black', fg='white',font=('Stencil',10))
    lb2.place(relx=0.06,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.4,rely=0.35, relwidth=0.50, relheight=0.08)

    SubmitBtn = Button(root,text="SUBMIT",bg='#D6E5FA', fg='black',font=('Impact',15),command=booklogin)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="QUIT",bg='#D6E5FA', fg='black',font=('Impact',15),command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    root.mainloop()
    
    
def forgotpassword():
    global bookInfo3,Canvas2,root
    messagebox.showinfo("LOGIN FAILED",'1.check your username and password properly!!\n 2.your username might not exist\n 3.your password might be wrong')
    root=Tk()
    root.title("FORGOT PASSWORD")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    Canvas2 = Canvas(root)

    Canvas2.config(bg="#E7FBBE")
    Canvas2.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="FORGOT PASSWORD?", bg='black', fg='white', font=('Forte',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

   
    SubmitBtn = Button(root,text="YES",bg='#D6E5FA', fg='black',font=('Impact',15),command=password)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="NO",bg='#D6E5FA', fg='black',font=('Impact',15),command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
