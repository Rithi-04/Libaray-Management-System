import mysql.connector
from tkinter import*
from tkinter import messagebox
from LOGIN import*
from REGISTER import*
import PIL.Image
import PIL.ImageTk
#CONNECTING TO SQL 
mydb=mysql.connector.connect(host='localhost',user="root",password="",database='triocoders')
mycr=mydb.cursor()
mycr.execute("create table if not exists libdatabase(bookno integer not null primary key,bookname varchar(100) not null,bookauthor varchar(50) not null,bookpublisher varchar(25) not null,bookgenre varchar(25) not null,status varchar(11) not null)")
mycr.execute("create table if not exists customer_details(name varchar(50) not null,mobileno varchar(10) not null,bookname varchar(100) not null,bookno integer not null)")
def regist():
    root.destroy()
    regis()
def logint():
    root.destroy()
    login()
#CREATING TKINTER WINDOW             
root=Tk()
root.title("LIBRARY MANAGEMENT SYSTEM")
root.minsize(width=400,height=400)
root.geometry("1600x1200")
same=True
n=2.25#0.25-5
# Adding a background image
background_image =PIL.Image.open("library3.jpeg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),PIL.Image.ANTIALIAS)
img = PIL.ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#FEFFDE",bd=5)
headingFrame1.place(relx=0.2,rely=0.02,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="WELCOME TO TRIO CODERS \n LIBRARY MANAGEMENT SYSTEM", bg='black', fg='white', font=('Forte',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn=Button(root,text="REGISTER/SIGNUP",bg='#FFEBCC',fg='black',font=('Impact',15),command=regist)
btn.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

btn0 = Button(root,text="LOGIN/SIGNIN",bg='#FFEBCC', fg='black',font=('Impact',15), command=logint)
btn0.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

btn1 = Button(root,text="QUIT",bg='#FFEBCC', fg='black',font=('Impact',15), command=root.destroy)
btn1.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

root.mainloop()

