from cProfile import label
from email.headerregistry import Group
from glob import glob0
from idlelib.configdialog import font_sample_text
from itertools import product
from pickle import GLOBAL
from string import whitespace
from tkinter import*
import random
from tkinter import messagebox
import random, os,tempfile,smtplib
from turtledemo.nim import randomrow

#Function part
def clear_():
    BatchSopEntry.delete(0,END)
    FaceCreamEntry.delete(0, END)
    FaceWashEntry.delete(0, END)
    HairSprayEntry.delete(0, END)
    HairGelEntry.delete(0, END)
    BodyLotionEntry.delete(0, END)

    # grocery empty clear function
    RiceEntry.delete(0, END)
    OilEntry.delete(0, END)
    DaalEntry.delete(0, END)
    WhealEntry.delete(0, END)
    SugerEntry.delete(0, END)
    TeaEntry.delete(0, END)

    # Cold Drinks
    MaazaEntry.delete(0, END)
    PepsiEntry.delete(0, END)
    SpriteEntry.delete(0, END)
    DewEntry.delete(0, END)
    FrootiEntry.delete(0, END)
    CoCaColaEntry.delete(0, END)

    BatchSopEntry.insert(0,0)
    FaceCreamEntry.insert(0, 0)
    FaceWashEntry.insert(0, 0)
    HairSprayEntry.insert(0, 0)
    HairGelEntry.insert(0, 0)
    BodyLotionEntry.insert(0, 0)

    # grocery empty clear function
    RiceEntry.insert(0, 0)
    OilEntry.insert(0, 0)
    DaalEntry.insert(0, 0)
    WhealEntry.insert(0, 0)
    SugerEntry.insert(0, 0)
    TeaEntry.insert(0, 0)

    # Cold Drinks
    MaazaEntry.insert(0, 0)
    PepsiEntry.insert(0, 0)
    SpriteEntry.insert(0, 0)
    DewEntry.insert(0, 0)
    FrootiEntry.insert(0, 0)
    CoCaColaEntry.insert(0, 0)

    #cosmatic,grocery, and coldDrink price clear function
    CosmaticEntry.delete(0,END)
    GroceryPriceEntry.delete(0, END)
    ColdDrinkTaxPriceEntry.delete(0, END)

    #cosmatic,grocery, and coldDrink tax price clear function
    CosmaticTaxPriceEntry.delete(0,END)
    GroceryTaxPriceEntry.delete(0, END)
    ColdDrinkPriceEntry.delete(0, END)

    #Name,phone,billingNumber,BillArea clear function

    nameEntry.delete(0,END)
    phoneEntry.delete(0, END)
    BillEntry.delete(0, END)

    textarea.delete(1.0,END)




#Email button feature program
def send_email():


    #end gmail function
    def Send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587) # smtp.gmail.com 587 This is the port number.
            ob.starttls()
            ob.login(senderEntry.get(),passwordEntry.get())
            message=email_textArea.get(1.0,END)
            ob.sendmail(senderEntry.get(),reciverEntry.get(),message)
            ob.quit()
            messagebox.showinfo('Success','Bill is successfully sent',parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error','Something went wrong, Please try again ',parent=root1)



    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        root1 = Toplevel()
        root1.grab_set()
        root1.title('send gmail')
        root1.config(bg='gray20')
        root1.resizable(0,0)

        #sender frame
        senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)

        #sender name and entry
        senderLabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bd=6,bg='gray20',fg='white')
        senderLabel.grid(row=0,column=0,padx=10,pady=8)

        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)

        #password name and entry
        passwordLabel = Label(senderFrame, text="Password", font=('arial', 14, 'bold'), bd=6, bg='gray20', fg='white')
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)

        passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE,show='*')#show password *
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        #recept frame
        recipientFrame = LabelFrame(root1, text='RECIPIENT', font=('arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
        recipientFrame.grid(row=1, column=0, padx=40, pady=20)

        #Email address name and entry
        reciverLabel = Label(recipientFrame, text="Email Address", font=('arial', 14, 'bold'), bd=6, bg='gray20', fg='white')
        reciverLabel.grid(row=0, column=0, padx=10, pady=8)

        reciverEntry = Entry(recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        reciverEntry.grid(row=0, column=1, padx=10, pady=8)

        #message name
        messageLabel = Label(recipientFrame, text="Message", font=('arial', 14, 'bold'), bd=6, bg='gray20', fg='white')
        messageLabel.grid(row=1, column=0, padx=10, pady=8)

        #email text area
        email_textArea=Text(recipientFrame, font=('arial', 14, 'bold'),bd=2,relief=SUNKEN,
                            width=42,height=11)
        email_textArea.grid(row=2,column=0,columnspan=2)
        email_textArea.delete(1.0,END)

        #Insert text ariea
        email_textArea.insert(END,textarea.get(1.0,END).replace('=','')
                              .replace('-','').replace('\t\t\t','\t\t'))

        sendButton=Button(root1,text='SEND', font=('arial', 16, 'bold'),width=15,command=Send_gmail)
        sendButton.grid(row=2,column=0,pady=20)


        root1.mainloop()


#bill recept print
def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')




#input bill number then show recept
def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==BillEntry.get():
           f=open(f'bills/{i}','r')
           textarea.delete(1.0,END)
           for data in f:
               textarea.insert(END,data)
           f.close()
           break
    else:
        messagebox.showerror('error','Invalid Bill Number')





if not os.path.exists('bills'):
    os.mkdir('bills')


#recipientFrame message save bill or not
def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you Want to Save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'Bill Number {billnumber} is saved successfully ')
        billnumber = random.randint(400, 1000)


# Random bill number er jonne
billnumber = random.randint(400, 1000)
#functionality part

#Calculate bill area
def bill_area():
    if nameEntry.get().strip() == '' or phoneEntry.get().strip() == '':
        messagebox.showerror('Error', 'Customer Details Are Required')
    elif (CosmaticEntry.get().strip() in ['', '0 BD']) and \
         (GroceryPriceEntry.get().strip() in ['', '0 BD']) and \
         (ColdDrinkPriceEntry.get().strip() in ['', '0 BD']):
     messagebox.showerror('Error', 'কোন প্রোডাক্ট সিলেক্ট করা হয়নি । প্লিজ সিলেক্ট করুন')
    else:
        # Proceed to generate the bill (You can write bill generation logic here)

            textarea.delete(1.0,END)

            textarea.insert(END,'\t\t**Welcome Customer**\n')
            textarea.insert(END,f'\nBill Number: {billnumber}\n')
            textarea.insert(END,f'\nCustomer Name:{nameEntry.get()}\n')
            textarea.insert(END,f'\nCustomer Phone Number: {phoneEntry.get()}\n')
            textarea.insert(END,'\n-------------------------------------------------------')
            textarea.insert(END,'\nProduct\t\t\tQuantity\t\t  Price')
            textarea.insert(END, '\n-------------------------------------------------------')

            #cosmatic item show bill receipt
            if BatchSopEntry.get()!='0':
                textarea.insert(END,f'\nBat Soap  \t\t\t{BatchSopEntry.get()}\t\t\t{soapPrice} BD')
            if FaceCreamEntry.get()!='0':
                textarea.insert(END,f'\nFace Cream\t\t\t{FaceCreamEntry.get()}\t\t\t{Facecream} BD')
            if FaceWashEntry.get()!='0':
                textarea.insert(END,f'\nFace Wash \t\t\t{FaceWashEntry.get()}\t\t\t{FaceWash} BD')
            if HairSprayEntry.get()!='0':
                textarea.insert(END,f'\nHair spary\t\t\t{HairSprayEntry.get()}\t\t\t{HairSpray} BD')
            if HairGelEntry.get()!='0':
                textarea.insert(END,f'\nHair Gel  \t\t\t{HairGelEntry.get()}\t\t\t{HairGel} BD')
            if BodyLotionEntry.get()!='0':
                textarea.insert(END,f'\nFace Cream\t\t\t{BodyLotionEntry.get()}\t\t\t{BodyLotion} BD')

            #Grocery item recept calculate and show
            if RiceEntry.get() != '0':
                textarea.insert(END, f'\nRice \t\t\t{RiceEntry.get()}\t\t\t{RicePrice} BD')
            if OilEntry.get() != '0':
                textarea.insert(END, f'\nOil \t\t\t{OilEntry.get()}\t\t\t{ OilPrice} BD')
            if DaalEntry.get() != '0':
                textarea.insert(END, f'\nDaal \t\t\t{DaalEntry.get()}\t\t\t{DaalPrice} BD')
            if WhealEntry.get() != '0':
                textarea.insert(END, f'\nWhile \t\t\t{WhealEntry.get()}\t\t\t{WhealPrice} BD')
            if SugerEntry.get() != '0':
                textarea.insert(END, f'\nSugar \t\t\t{SugerEntry.get()}\t\t\t{ SugarPrice} BD')
            if TeaEntry.get() != '0':
                textarea.insert(END, f'\nTea \t\t\t{TeaEntry.get()}\t\t\t{ TeaPrice} BD')

            #Cold Drinks recept and show calculate
            if MaazaEntry.get() != '0':
                textarea.insert(END, f'\nMaaza \t\t\t{MaazaEntry.get()}\t\t\t{MaazaPrice} BD')
            if PepsiEntry.get() != '0':
                    textarea.insert(END, f'\nPepsi \t\t\t{PepsiEntry.get()}\t\t\t{ pepsiprice} BD')
            if SpriteEntry.get() != '0':
                textarea.insert(END, f'\nSprite \t\t\t{SpriteEntry.get()}\t\t\t{spriteprice} BD')
            if DewEntry.get() != '0':
                textarea.insert(END, f'\nDew \t\t\t{DewEntry.get()}\t\t\t{dewprice} BD')
            if FrootiEntry.get() != '0':
                textarea.insert(END, f'\nfrooti \t\t\t{FrootiEntry.get()}\t\t\t{ frootiprice} BD')
            if CoCaColaEntry.get() != '0':
                textarea.insert(END, f'\nTea \t\t\t{CoCaColaEntry.get()}\t\t\t{ CocaColaprice} BD')

            #Separate line
            textarea.insert(END,'\n-------------------------------------------------------')

            #All tax calculate and recep show
            if CosmaticTaxPriceEntry.get()!='0.0 BD':
                textarea.insert(END,f'\nCosmatic Tax\t\t\t\t{CosmaticTaxPriceEntry.get()}')
            if GroceryTaxPriceEntry.get()!='0.0 BD':
                textarea.insert(END,f'\nGrocery Tax\t\t\t\t{GroceryTaxPriceEntry.get()}')
            if ColdDrinkTaxPriceEntry.get()!='0.0 BD':
                textarea.insert(END,f'\nCold Drink Tax\t\t\t\t{ColdDrinkTaxPriceEntry.get()}')

            #totall bill calculate recep
            textarea.insert(END,f'\n\nTotal Bill\t\t\t\t{TotalBill} BD')
            #Separate line
            textarea.insert(END,'\n-------------------------------------------------------')
            save_bill()


#Total
def total():
    global soapPrice,Facecream,FaceWash,HairSpray,HairGel,BodyLotion
    global RicePrice,  OilPrice,DaalPrice,WhealPrice,  SugarPrice,  TeaPrice
    global MaazaPrice,pepsiprice,spriteprice,dewprice,frootiprice,CocaColaprice
    global  TotalBill
    #Cosmatic price calculation
    soapPrice=int(BatchSopEntry.get())*20
    Facecream=int(FaceCreamEntry.get())*50
    FaceWash=int(FaceWashEntry.get())*100
    HairSpray=int(HairSprayEntry.get())*150
    HairGel=int(HairGelEntry.get())*80
    BodyLotion=int(BodyLotionEntry.get())*60

    Totalcosmaticprice = soapPrice + Facecream + FaceWash + HairSpray + HairGel + BodyLotion
    CosmaticEntry.delete(0,END)
    CosmaticEntry.insert(0,f'{Totalcosmaticprice} BD')
    cosmaticTax=Totalcosmaticprice * 0.12
    CosmaticTaxPriceEntry.delete(0,END)
    CosmaticTaxPriceEntry.insert(0,str(cosmaticTax)+ ' BD')



    #Grocery price calculation
    RicePrice=int(RiceEntry.get())*30
    OilPrice=int(OilEntry.get())*100
    DaalPrice=int(DaalEntry.get())*120
    WhealPrice=int(WhealEntry.get())*50
    SugarPrice=int(SugerEntry.get())*140
    TeaPrice=int(TeaEntry.get())*80

    TotalGroceryPrice = RicePrice+OilPrice+DaalPrice+WhealPrice+SugarPrice+TeaPrice
    GroceryPriceEntry.delete(0,END)
    GroceryPriceEntry.insert(0,f'{TotalGroceryPrice} BD ')
    GroceryTax = TotalGroceryPrice * 0.6
    GroceryTaxPriceEntry.delete(0, END)
    GroceryTaxPriceEntry.insert(0, f'{GroceryTax} BD ')


    #Cold Drinks price calculation
    MaazaPrice=int(MaazaEntry.get())*30
    pepsiprice=int(PepsiEntry.get())*20
    spriteprice=int(SpriteEntry.get())*30
    dewprice=int(DewEntry.get())*40
    frootiprice=int(FrootiEntry.get())*50
    CocaColaprice=int(CoCaColaEntry.get())*60

    TotalColdDrinkPrice = MaazaPrice+pepsiprice+spriteprice+dewprice+frootiprice+CocaColaprice
    ColdDrinkPriceEntry.delete(0,END)
    ColdDrinkPriceEntry.insert(0,str(TotalColdDrinkPrice)+' BD')
    ColdDrinksTax = TotalColdDrinkPrice * 0.5
    ColdDrinkTaxPriceEntry.delete(0, END)
    ColdDrinkTaxPriceEntry.insert(0, str(ColdDrinksTax) + ' BD')

    #Total bill calculate
    TotalBill = Totalcosmaticprice+TotalGroceryPrice+TotalColdDrinkPrice+cosmaticTax+GroceryTax+ColdDrinksTax

#GUI PART
root =Tk()
root.title('Grocery Billing System')
root.geometry('1270x685')
root.iconbitmap('Icon.ico')

#Heading Label
headingLabel = Label(root, text='Grocery Billing System recipientFrameed by SOZIB', font=('times new roman',25,'bold')
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
searchButton=Button(customer_details_frame, text='SEARCH',font=('arial',12,'bold'),border=8,width=10
                   ,command=search_bill)
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

#scrollbar section
Scrollbar=Scrollbar(billFrame,orient=VERTICAL)
Scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billFrame,height=17,width=55,yscrollcommand=Scrollbar.set)
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
GroceryTaxPriceLabel=Label(BillManuFrame,text='Grocery Tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
GroceryTaxPriceLabel.grid(row=1,column=2,pady=4,padx=17,sticky='w')

GroceryTaxPriceEntry=Entry(BillManuFrame,font=('time new roman',14,'bold'),width=10,bd=5)
GroceryTaxPriceEntry.grid(row=1,column=3,pady=4,padx=17,sticky='w')

#ColdDrink Tax
ColdDrinkTaxPriceLabel=Label(BillManuFrame,text='Cold Drink Tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
ColdDrinkTaxPriceLabel.grid(row=2,column=2,pady=4,padx=17,sticky='w')

ColdDrinkTaxPriceEntry=Entry(BillManuFrame,font=('time new roman',14,'bold'),width=10,bd=5)
ColdDrinkTaxPriceEntry.grid(row=2,column=3,pady=4,padx=17,sticky='w')


#ButtoneFrame
buttonFrame=Frame(BillManuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

#Tootal button
TotalButton=Button(buttonFrame,text='Total',font=('arial',15,'bold'),bg='gray20',fg='white',bd=5,
                    width=8,command=total)
TotalButton.grid(row=0,column=0,pady=15,padx=5)

#Bill button
BillButton=Button(buttonFrame,text='Bill',font=('Bill',15,'bold'),bg='gray20',fg='white',bd=5
                  ,width=8,command=bill_area)
BillButton.grid(row=0,column=1,pady=15,padx=5)
#Email button
EmailButton=Button(buttonFrame,text='Email',font=('arial',15,'bold'),bg='gray20',fg='white',bd=5,width=8,command=send_email)
EmailButton.grid(row=0,column=2,pady=15,padx=5)
#Print button
PrintButton=Button(buttonFrame,text='Print',font=('arial',15,'bold'),bg='gray20',fg='white',bd=5,width=8,
                   command=print_bill)
PrintButton.grid(row=0,column=3,pady=15,padx=5)
#clear button
clearFrameButton=Button(buttonFrame,text='Clear',font=('arial',15,'bold'),bg='gray20',fg='white',
                        bd=5,width=8,command=clear_)
clearFrameButton.grid(row=0,column=4,pady=15,padx=5,)
root.mainloop()