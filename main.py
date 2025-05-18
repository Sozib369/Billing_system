from cProfile import label
from email.headerregistry import Group
from glob import glob0
from idlelib.configdialog import font_sample_text
from itertools import product
from pickle import GLOBAL
from string import whitespace
from tkinter import*
from turtledemo.nim import randomrow


#functionality part
def total():
    soapPrice=int(BatchSopEntry.get())*20
    Facecream=int(FaceCreamEntry.get())*50
    FaceWash=int(FaceWashEntry.get())*100
    HairSpray=int(HairSprayEntry.get())*150
    HairGel=int(HairGelEntry.get())*80
    BodyLotion=int(BodyLotionEntry.get())*60

    cosmaticprice= soapPrice + Facecream + FaceWash + HairSpray + HairGel + BodyLotion
    CosmaticEntry.insert(0,cosmaticprice)



#GUI PART
root =Tk()
root.title('Grocery Billing System')
root.geometry('1270x685')
root.iconbitmap('Icon.ico')

#Heading Label
headingLabel = Label(root, text='Grocery Billing System created by SOZIB', font=('times new roman',25,'bold')
                     ,bg='gray20',fg='gold',bd=12,relief='groove')
headingLabel.pack(fill=X,pady=2)

#Customer details frame
customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',14,'bold'),
                                  fg='gold',bd=8,relief="groove",bg='gray20')
customer_details_frame.pack(fill=X)

#Name
nameLabel= Label(customer_details_frame, text='Name',font=('times new roman',15,'bold'),bg='gray20',fg='white')
nameLabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=8,width=15)
nameEntry.grid(row=0,column=1,padx=8,pady=2)

#phone
phoneLabel=Label(customer_details_frame, text='Phone Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=8,width=15)
phoneEntry.grid(row=0,column=3,padx=20,pady=2)

#Billing Number
BillLabel=Label(customer_details_frame, text='Billing Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
BillLabel.grid(row=0,column=4,padx=20,pady=2)

BillEntry=Entry(customer_details_frame,font=('arial',15),bd=8,width=15)
BillEntry.grid(row=0,column=5,padx=20,pady=2)

#Serch
searchButton=Button(customer_details_frame, text='SEARCH',font=('arial',12,'bold'),border=8,width=10)
searchButton.grid(row=0,column=6,padx=20,pady=3)

#products frame
productsFrame=Frame(root)
productsFrame.pack()

#Cosmetice Frame
cosmeticFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold'),bg='gray20',fg='gold',
                    relief=GROOVE,bd=8)
cosmeticFrame.grid(row=0,column=0)

#bath sop
BatchSop=Label(cosmeticFrame,text='Bat sop',font=('times new roman',15,'bold'),bg='gray20',fg='white')
BatchSop.grid(row=0,column=0,pady=6,padx=10,sticky='w')

BatchSopEntry=Entry(cosmeticFrame,font=('time new roman',15,'bold'),width=10,bd=5)
BatchSopEntry.grid(row=0,column=1,pady=6,padx=10,sticky='w')
BatchSopEntry.insert(0,0)
#face cream
FaceCream=Label(cosmeticFrame,text='Face Cream',font=('times new roman',15,'bold'),bg='gray20',fg='white')
FaceCream.grid(row=1,column=0,pady=6,padx=10,sticky='w')

FaceCreamEntry=Entry(cosmeticFrame,font=('time new roman',15,'bold'),width=10,bd=5)
FaceCreamEntry.grid(row=1,column=1,pady=6,padx=10,sticky='w')
FaceCreamEntry.insert(0,0)
#Face wash
FaceWash=Label(cosmeticFrame,text='Face wash',font=('times new roman',15,'bold'),bg='gray20',fg='white')
FaceWash.grid(row=2,column=0,pady=6,padx=10,sticky='w')

FaceWashEntry=Entry(cosmeticFrame,font=('time new roman',15,'bold'),width=10,bd=5)
FaceWashEntry.grid(row=2,column=1,pady=6,padx=10,sticky='w')
FaceWashEntry.insert(0,0)
#Hair spray
HairSpray=Label(cosmeticFrame,text='Hair spray',font=('times new roman',15,'bold'),bg='gray20',fg='white')
HairSpray.grid(row=3,column=0,pady=6,padx=10,sticky='w')

HairSprayEntry=Entry(cosmeticFrame,font=('time new roman',15,'bold'),width=10,bd=5)
HairSprayEntry.grid(row=3,column=1,pady=6,padx=10,sticky='w')
HairSprayEntry.insert(0,0)
#Hair gel
HairGel=Label(cosmeticFrame,text='Hair Gel',font=('times new roman',15,'bold'),bg='gray20',fg='white')
HairGel.grid(row=4,column=0,pady=6,padx=10,sticky='w')

HairGelEntry=Entry(cosmeticFrame,font=('time new roman',15,'bold'),width=10,bd=5)
HairGelEntry.grid(row=4,column=1,pady=6,padx=10,sticky='w')
HairGelEntry.insert(0,0)

#Body Lotion
BodyLotion=Label(cosmeticFrame,text='Body Lotion',font=('times new roman',15,'bold'),bg='gray20',fg='white')
BodyLotion.grid(row=5,column=0,pady=6,padx=10,sticky='w')

BodyLotionEntry=Entry(cosmeticFrame,font=('time new roman',15,'bold'),width=10,bd=5)
BodyLotionEntry.grid(row=5,column=1,pady=6,padx=10,sticky='w')
BodyLotionEntry.insert(0,0)
#Grocery Item frame
GroceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold'),bg='gray20',fg='gold',
                    relief=GROOVE,bd=8)
GroceryFrame.grid(row=0,column=1)

#Rice
Rice=Label(GroceryFrame,text='Rice',font=('times new roman',15,'bold'),bg='gray20',fg='white')
Rice.grid(row=0,column=0,pady=6,padx=10,sticky='w')

RiceEntry=Entry(GroceryFrame,font=('time new roman',15,'bold'),width=10,bd=5)
RiceEntry.grid(row=0,column=1,pady=6,padx=10,sticky='w')
RiceEntry.insert(0,0)
#Oil
Oil=Label(GroceryFrame,text='Oil',font=('times new roman',15,'bold'),bg='gray20',fg='white')
Oil.grid(row=1,column=0,pady=6,padx=10,sticky='w')

OilEntry=Entry(GroceryFrame,font=('time new roman',15,'bold'),width=10,bd=5)
OilEntry.grid(row=1,column=1,pady=6,padx=10,sticky='w')
OilEntry.insert(0,0)
#Wheal
Wheal=Label(GroceryFrame,text='Wheal',font=('times new roman',15,'bold'),bg='gray20',fg='white')
Wheal.grid(row=2,column=0,pady=6,padx=10,sticky='w')

WhealEntry=Entry(GroceryFrame,font=('time new roman',15,'bold'),width=10,bd=5)
WhealEntry.grid(row=2,column=1,pady=6,padx=10,sticky='w')
WhealEntry.insert(0,0)
#Sugar
SugerLabel=Label(GroceryFrame,text='Suger',font=('times new roman',15,'bold'),bg='gray20',fg='white')
SugerLabel.grid(row=3,column=0,pady=6,padx=10,sticky='w')

SugerEntry=Entry(GroceryFrame,font=('time new roman',15,'bold'),width=10,bd=5)
SugerEntry.grid(row=3,column=1,pady=6,padx=10,sticky='w')
SugerEntry.insert(0,0)
#Daal
DaalLabel=Label(GroceryFrame,text='Daal',font=('times new roman',15,'bold'),bg='gray20',fg='white')
DaalLabel.grid(row=4,column=0,pady=6,padx=10,sticky='w')

DaalEntry=Entry(GroceryFrame,font=('time new roman',15,'bold'),width=10,bd=5)
DaalEntry.grid(row=4,column=1,pady=6,padx=10,sticky='w')
DaalEntry.insert(0,0)
#Tea
TeaLabel=Label(GroceryFrame,text='Tea',font=('times new roman',15,'bold'),bg='gray20',fg='white')
TeaLabel.grid(row=5,column=0,pady=6,padx=10,sticky='w')

TeaEntry=Entry(GroceryFrame,font=('time new roman',15,'bold'),width=10,bd=5)
TeaEntry.grid(row=5,column=1,pady=6,padx=10,sticky='w')
TeaEntry.insert(0,0)
#Cold Drinks Frame
ColdDrinksFrame=LabelFrame(productsFrame,text='Cold Drinks',font=('times new roman',15,'bold'),bg='gray20',fg='gold',
                    relief=GROOVE,bd=8)
ColdDrinksFrame.grid(row=0,column=2)

#Maaza
MaazaLabel=Label(ColdDrinksFrame,text='Maaza',font=('times new roman',15,'bold'),bg='gray20',fg='white')
MaazaLabel.grid(row=0,column=0,pady=6,padx=10,sticky='w')

MaazaEntry=Entry(ColdDrinksFrame,font=('time new roman',15,'bold'),width=10,bd=5)
MaazaEntry.grid(row=0,column=1,pady=6,padx=10,sticky='w')
MaazaEntry.insert(0,0)

#pepsi
PepsiLabel=Label(ColdDrinksFrame,text='Pepsi',font=('times new roman',15,'bold'),bg='gray20',fg='white')
PepsiLabel.grid(row=1,column=0,pady=6,padx=10,sticky='w')

PepsiEntry=Entry(ColdDrinksFrame,font=('time new roman',15,'bold'),width=10,bd=5)
PepsiEntry.grid(row=1,column=1,pady=6,padx=10,sticky='w')
PepsiEntry.insert(0,0)

#Sprite
SpriteLabel=Label(ColdDrinksFrame,text='Sprite',font=('times new roman',15,'bold'),bg='gray20',fg='white')
SpriteLabel.grid(row=2,column=0,pady=6,padx=10,sticky='w')

SpriteEntry=Entry(ColdDrinksFrame,font=('time new roman',15,'bold'),width=10,bd=5)
SpriteEntry.grid(row=2,column=1,pady=6,padx=10,sticky='w')
SpriteEntry.insert(0,0)
#Dew
DewLabel=Label(ColdDrinksFrame,text='Dew',font=('times new roman',15,'bold'),bg='gray20',fg='white')
DewLabel.grid(row=3,column=0,pady=6,padx=10,sticky='w')

DewEntry=Entry(ColdDrinksFrame,font=('time new roman',15,'bold'),width=10,bd=5)
DewEntry.grid(row=3,column=1,pady=6,padx=10,sticky='w')
DewEntry.insert(0,0)
#frooti
FrootiLabel=Label(ColdDrinksFrame,text='Frooti',font=('times new roman',15,'bold'),bg='gray20',fg='white')
FrootiLabel.grid(row=4,column=0,pady=6,padx=10,sticky='w')

FrootiEntry=Entry(ColdDrinksFrame,font=('time new roman',15,'bold'),width=10,bd=5)
FrootiEntry.grid(row=4,column=1,pady=6,padx=10,sticky='w')
FrootiEntry.insert(0,0)
#Coca cola
CoCaColaLabel=Label(ColdDrinksFrame,text='CoCaCola',font=('times new roman',15,'bold'),bg='gray20',fg='white')
CoCaColaLabel.grid(row=5,column=0,pady=6,padx=10,sticky='w')

CoCaColaEntry=Entry(ColdDrinksFrame,font=('time new roman',15,'bold'),width=10,bd=5)
CoCaColaEntry.grid(row=5,column=1,pady=6,padx=10,sticky='w')
CoCaColaEntry.insert(0,0)
#Bill Frame
billFrame=Frame(productsFrame,bd=8,relief=GROOVE)
billFrame.grid(row=0,column=3,padx=7)

billareaLabel=Label(billFrame,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

Scrollbar=Scrollbar(billFrame,orient=VERTICAL)
Scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billFrame,height=17,width=53,yscrollcommand=Scrollbar.set)
textarea.pack()
Scrollbar.config(command=textarea.yview())



#bill manu frame
BillManuFrame=LabelFrame(root,text='Bill Manu',font=('times new roman',14,'bold'),bg='gray20',fg='gold',
                    relief=GROOVE,bd=8)
BillManuFrame.pack()

#Cosmetic Price
CosmaticLabel=Label(BillManuFrame,text='Cosmetic price',font=('times new roman',14,'bold'),bg='gray20',fg='white')
CosmaticLabel.grid(row=0,column=0,pady=4,padx=10,sticky='w')

CosmaticEntry=Entry(BillManuFrame,font=('time new roman',14,'bold'),width=10,bd=5)
CosmaticEntry.grid(row=0,column=1,pady=4,padx=10,sticky='w')

#Grocery price
GroceryPriceLabel=Label(BillManuFrame,text='Grocery price',font=('times new roman',14,'bold'),bg='gray20',fg='white')
GroceryPriceLabel.grid(row=1,column=0,pady=4,padx=10,sticky='w')

GroceryPriceEntry=Entry(BillManuFrame,font=('time new roman',14,'bold'),width=10,bd=5)
GroceryPriceEntry.grid(row=1,column=1,pady=4,padx=10,sticky='w')

#Coldrink price
ColdDrinkPriceLabel=Label(BillManuFrame,text='Cold Drink price',font=('times new roman',14,'bold'),bg='gray20',fg='white')
ColdDrinkPriceLabel.grid(row=2,column=0,pady=4,padx=10,sticky='w')

ColdDrinkPriceEntry=Entry(BillManuFrame,font=('time new roman',14,'bold'),width=10,bd=5)
ColdDrinkPriceEntry.grid(row=2,column=1,pady=4,padx=10,sticky='w')

#Cosmetic Tax
CosmaticTaxPriceLabel=Label(BillManuFrame,text='Cosmatic Tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
CosmaticTaxPriceLabel.grid(row=0,column=2,pady=4,padx=17,sticky='w')

CosmaticTaxPriceEntry=Entry(BillManuFrame,font=('time new roman',14,'bold'),width=10,bd=5)
CosmaticTaxPriceEntry.grid(row=0,column=3,pady=4,padx=17,sticky='w')

#Grcery Tax
CosmaticTaxPriceLabel=Label(BillManuFrame,text='Cosmatic Tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
CosmaticTaxPriceLabel.grid(row=1,column=2,pady=4,padx=17,sticky='w')

CosmaticTaxPriceEntry=Entry(BillManuFrame,font=('time new roman',14,'bold'),width=10,bd=5)
CosmaticTaxPriceEntry.grid(row=1,column=3,pady=4,padx=17,sticky='w')

#ColdDrink Tax
ColdDrinkTaxPriceLabel=Label(BillManuFrame,text='Cold Drink Tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
ColdDrinkTaxPriceLabel.grid(row=2,column=2,pady=4,padx=17,sticky='w')

ColdDrinkTaxPriceEntry=Entry(BillManuFrame,font=('time new roman',14,'bold'),width=10,bd=5)
ColdDrinkTaxPriceEntry.grid(row=2,column=3,pady=4,padx=17,sticky='w')


#ButtoneFrame
buttonFrame=Frame(BillManuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

#Tootal
TotalButton=Button(buttonFrame,text='Total',font=('arial',15,'bold'),bg='gray20',fg='white',bd=5,
                    width=8,command=total)
TotalButton.grid(row=0,column=0,pady=15,padx=5)

#Email
EmailButton=Button(buttonFrame,text='Email',font=('Email',15,'bold'),bg='gray20',fg='white',bd=5,width=8)
EmailButton.grid(row=0,column=1,pady=15,padx=5)
#Bill
BillButton=Button(buttonFrame,text='Bill',font=('arial',15,'bold'),bg='gray20',fg='white',bd=5,width=8)
BillButton.grid(row=0,column=2,pady=15,padx=5)
#Print
PrintButton=Button(buttonFrame,text='Print',font=('arial',15,'bold'),bg='gray20',fg='white',bd=5,width=8)
PrintButton.grid(row=0,column=3,pady=15,padx=5)
#Creat
CreatButton=Button(buttonFrame,text='Creat',font=('arial',15,'bold'),bg='gray20',fg='white',bd=5,width=8)
CreatButton.grid(row=0,column=4,pady=15,padx=5,)
root.mainloop()