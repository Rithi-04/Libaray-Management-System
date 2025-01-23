import mysql.connector
from tkinter import messagebox
from tkinter import*
import tkinter as tk
from tkinter import ttk
mydb=mysql.connector.connect(host='localhost',user="root",password="",database="triocoders")
mycr=mydb.cursor()
def issued():
  mycr.execute("select* from customer_details")
  res=mycr.fetchall()
  def show():

  
      res.sort(key=lambda e: e[1], reverse=True)

      for i, (NAME,MOBILENO,BOOKNAME,BOOKNO) in enumerate(res, start=1):
          listBox.insert("", "end", values=(i,NAME,MOBILENO,BOOKNAME,BOOKNO))

  scores = tk.Tk() 
  label = tk.Label(scores, text="BOOK LIST",bg='#4FBDBA', font=("Forte",30)).grid(row=0, columnspan=3)
  # create Treeview with 3 columns
  cols = ('SNO','NAME','MOBILENO','BOOKNAME','BOOKNO')
  listBox = ttk.Treeview(scores, columns=cols, show='headings')
  # set column headings
  for col in cols:
      listBox.heading(col, text=col)    
  listBox.grid(row=1, column=0, columnspan=2)

  show()
  closeButton = tk.Button(scores, text="Close", width=15, command=scores.destroy).grid(row=4, column=1)
  scores.mainloop()
