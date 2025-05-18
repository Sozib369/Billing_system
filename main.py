from email.headerregistry import Group
from glob import glob0
from idlelib.configdialog import font_sample_text
from pickle import GLOBAL
from tkinter import*
from turtledemo.nim import randomrow

root =Tk()
root.title('Grocery Billing System')
root.geometry('1270x685')
root.iconbitmap('Icon.ico')
headingLabel = Label(root, text='Grocery Billing System created by SOZIB', font=('times new roman',25,'bold')
                     ,bg='gray20',fg='gold',bd=12,relief='groove')
headingLabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold'),
                                  fg='gold',bd=8,relief="groove",bg='gray20')
customer_details_frame.pack()

#Name
nameLabel= Label(customer_details_frame, text='Name',bg='gray20',fg='white')
nameLabel.grid(row=0,column=0,padx=20,pady=2)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=8,width=18)
nameEntry.grid(row=0,column=1,padx=8,pady=2)

#phone
phoneLabel=Label(customer_details_frame, text='phone',bg='gray20',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=8,width=18)
phoneEntry.grid(row=0,column=3,padx=20,pady=2)

#Billing Number
BillLabel=Label(customer_details_frame, text='Billing Number ',bg='gray20',fg='white')
BillLabel.grid(row=0,column=4,padx=20,pady=2)

BillEntry=Entry(customer_details_frame,font=('arial',15),bd=8,width=18)
BillEntry.grid(row=0,column=5,padx=20,pady=2)

#Serch
BillLabel=Label(customer_details_frame, text='Billing Number ',bg='gray20',fg='white')
BillLabel.grid(row=0,column=6,padx=20,pady=2)

BillEntry=Entry(customer_details_frame,font=('arial',15),bd=8,width=18)
BillEntry.grid(row=0,column=7,padx=20,pady=2)


root.mainloop()