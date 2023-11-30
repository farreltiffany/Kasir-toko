from tkinter import *
from tkinter import messagebox
import random,os
#functionality part


if not os.path.exists('bills'):
    os.mkdir('bills')


def save_bill():
       global billnumber
       result= messagebox.askyesno('confirm','do you want to save the bill?')
       if result:
               bill_content=textarea.get(1.0,END)
               file=open(f'bills/ {billnumber}.txt','m')
               file.write(bill_content)
               file.close()
               messagebox.showinfo('success',f'{billnumber} is save successfully')
               billnumber = random.randint(500, 1000)

billnumber=random.randint(500,1000)


def bill_area():
    if nameEntry.get()=='' or phoneEntry.get()=='':
       messagebox.showerror('error','customer details are required')
    elif bukupriceEntry.get()=='' and alattulispriceEntry.get()=='' and ATKpriceEntry.get()=='':
       messagebox.showerror('error','no product are selected')
    elif bukupriceEntry.get()=='0 Rp' and alattulispriceEntry.get()=='0 Rp' and ATKpriceEntry.get()=='0 Rp':
       messagebox.showerror('error','no product are selected')
    textarea.delete(1.0,END)

    textarea.insert(END,'\t\t** Welcome Customer**\n')
    textarea.insert(END,f'\nBill Number: {billnumber}\n')
    textarea.insert(END,f'\nCustomer Name: {nameEntry.get()}\n')
    textarea.insert(END,f'\nCustomer Phone Number: {phoneEntry.get()}\n')
    textarea.insert(END,'\n=======================================================')
    textarea.insert(END,'Product\t\t\tQuantity\t\t\tprice')
    textarea.insert(END,'\n=======================================================')
    if bukutulisEntry.get()!='0':
              textarea.insert(END,f'\nBuku Tulis\t\t\t{bukutulisEntry.get()}\t\t\t{bukutulisprice} Rp')
    if bukugambara3Entry.get()!='0':
              textarea.insert(END,f'\nBuku Tulis\t\t\t{bukugambara3Entry.get()}\t\t\t{bukugambara3price} Rp')
    if bukugambara4Entry.get()!='0':
              textarea.insert(END,f'\nBuku Tulis\t\t\t{bukugambara4Entry.get()}\t\t\t{bukugambara4price} Rp')
    if bukuhalusEntry.get()!='0':
              textarea.insert(END,f'\nBuku Tulis\t\t\t{bukuhalusEntry.get()}\t\t\t{bukuhalusprice} Rp')
    if bukustriminEntry.get()!='0':
              textarea.insert(END,f'\nBuku Tulis\t\t\t{bukustriminEntry.get()}\t\t\t{bukustriminprice} Rp')
    if pepakbasajawaEntry.get()!='0':
              textarea.insert(END,f'\nBuku Tulis\t\t\t{pepakbasajawaEntry.get()}\t\t\t{pepakbasajawaprice} Rp')


    if pensilEntry.get()!='0':
              textarea.insert(END,f'\nAlat Tulis\t\t\t{pensilEntry.get()}\t\t\t{pensilprice} Rp')
    if bolpointEntry.get()!='0':
              textarea.insert(END,f'\nAlat Tulis\t\t\t{bolpointEntry.get()}\t\t\t{bolpointprice} Rp')
    if pensilwarnaEntry.get()!='0':
              textarea.insert(END,f'\nAlat Tulis\t\t\t{pensilwarnaEntry.get()}\t\t\t{pensilwarnaprice} Rp')
    if penggarisEntry.get()!='0':
              textarea.insert(END,f'\nAlat Tulis\t\t\t{penggarisEntry.get()}\t\t\t{penggarisprice} Rp')
    if spidolEntry.get()!='0':
              textarea.insert(END,f'\nAlat Tulis\t\t\t{spidolEntry.get()}\t\t\t{spidolprice} Rp')
    if penghapusEntry.get()!='0':
              textarea.insert(END,f'\nAlat Tulis\t\t\t{penghapusEntry.get()}\t\t\t{penghapusprice} Rp')


    if selotipEntry.get()!='0':
              textarea.insert(END,f'\nAtk\t\t\t{selotipEntry.get()}\t\t\t{pensilprice} Rp')
    if amplopEntry.get()!='0':
              textarea.insert(END,f'\nAtk\t\t\t{amplopEntry.get()}\t\t\t{bolpointprice} Rp')
    if lemEntry.get()!='0':
              textarea.insert(END,f'\nAtk\t\t\t{lemEntry.get()}\t\t\t{pensilwarnaprice} Rp')
    if rautanEntry.get()!='0':
              textarea.insert(END,f'\nAtk\t\t\t{rautanEntry.get()}\t\t\t{penggarisprice} Rp')
    if stabiloEntry.get()!='0':
              textarea.insert(END,f'\nAtk\t\t\t{stabiloEntry.get()}\t\t\t{spidolprice} Rp')
    if tippxEntry.get()!='0':
              textarea.insert(END,f'\nAtk\t\t\t{tippxEntry.get()}\t\t\t{penghapusprice} Rp')

    textarea.insert(END,'\n-------------------------------------------------------')

    if bukutaxEntry.get()!='0.0 Rp':
              textarea.insert(END,f'\nBuku Tax\t\t\t\t{bukutaxEntry.get()}')
    if alattulistaxEntry.get()!='0.0 Rp':
              textarea.insert(END,f'\nBuku Tax\t\t\t\t{alattulistaxEntry.get()}')
    if ATKtaxEntry.get()!='0.0 Rp':
              textarea.insert(END,f'\nBuku Tax\t\t\t\t{ATKtaxEntry.get()}')
    textarea.insert(END,f'\n\nTotal Bill \t\t\t\t {totalbill}')
    textarea.insert(END,'\n-------------------------------------------------------')
    save_bill()

#functionality part
def total():
    global bukutulisprice,bukugambara3price,bukugambara4price,bukuhalusprice,bukustriminprice,pepakbasajawaprice
    global pensilprice,bolpointprice,pensilwarnaprice,penggarisprice,spidolprice,penghapusprice
    global selotipprice,amplopprice,lemprice,rautanprice,stabiloprice,tippxprice
    global totalbill
    #buku price calculation
    bukutulisprice = int(bukutulisEntry.get())*4500
    bukugambara3price = int(bukugambara3Entry.get())*7000
    bukugambara4price = int(bukugambara4Entry.get())*7000
    bukuhalusprice = int(bukuhalusEntry.get())*3000
    bukustriminprice = int(bukustriminEntry.get())*3000
    pepakbasajawaprice = int(pepakbasajawaEntry.get())*30000

    totalbukuprice = bukutulisprice+bukugambara3price+bukugambara4price+bukuhalusprice+bukustriminprice+pepakbasajawaprice
    bukupriceEntry.delete(0,END)
    bukupriceEntry.insert(0,f'{totalbukuprice} rupiah')
    bukupricestax = totalbukuprice * 0.08
    bukutaxEntry.delete(0, END)
    bukutaxEntry.insert(0, f'{bukupricestax} rupiah') 

    #alat tulis price calculation
    pensilprice=int(pensilEntry.get())*3000
    bolpointprice=int(bolpointEntry.get())*3000
    pensilwarnaprice=int(pensilwarnaEntry.get())*3000
    penggarisprice=int(penggarisEntry.get())*3000
    spidolprice=int(spidolEntry.get())*2500
    penghapusprice=int(penghapusEntry.get())*2000

    totalalattulisprice = pensilprice+bolpointprice+pensilwarnaprice+penggarisprice+spidolprice+penghapusprice
    alattulispriceEntry.delete(0,END)
    alattulispriceEntry.insert(0,f'{totalalattulisprice} rupiah')
    alattulispricestax = totalalattulisprice * 0.08
    alattulistaxEntry.delete(0, END)
    alattulistaxEntry.insert(0, str(alattulispricestax) +'rupiah')

    #ATK price calculation
    selotipprice=int(selotipEntry.get()) * 2000
    amplopprice=int(amplopEntry.get()) * 1000
    lemprice=int(lemEntry.get()) * 8000
    rautanprice=int(rautanEntry.get()) * 2000
    stabiloprice=int(stabiloEntry.get()) * 6000
    tippxprice=int(tippxEntry.get()) * 6000

    totalATKprice=selotipprice+amplopprice+lemprice+rautanprice+stabiloprice+tippxprice
    ATKpriceEntry.delete(0,END)
    ATKpriceEntry.insert(0,str(totalATKprice)+ 'rupiah')
    ATKtax = totalATKprice * 0.08
    ATKtaxEntry.delete(0, END)
    ATKtaxEntry.insert(0, str(ATKtax)+'rupiah')

    totalbill=totalbukuprice+totalalattulisprice+totalATKprice+bukupricestax+alattulispricestax+ATKtax

    




root=Tk()
root.title('Kasir Toko Gue')
root.geometry('1270x685')

headingLabel=Label(root,text='Kasir Toko Gue',font=('times new roman',30,'bold'),bg='grey20',fg='white',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)


customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='grey20',fg='white')
nameLabel.grid(row=0,column=0,padx=20,pady=2)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='grey20',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='grey20',fg='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=10)
searchButton.grid(row=0,column=6,padx=20,pady=8)

productsFrame=Frame(root)
productsFrame.pack()

bukuFrame=LabelFrame(productsFrame,text="Buku",font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
bukuFrame.grid(row=0,column=0,pady=9,padx=0)

bukutulisLabel=Label(bukuFrame,text="Buku Tulis",font=('times new roman',15,'bold'),bg='grey20',fg='white')
bukutulisLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

bukutulisEntry=Entry(bukuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bukutulisEntry.grid(row=0,column=1,pady=9,padx=10)
bukutulisEntry.insert(0,0)

bukugambara3Label=Label(bukuFrame,text="Buku Gambar A3",font=('times new roman',15,'bold'),bg='grey20',fg='white')
bukugambara3Label.grid(row=1,column=0,pady=9,padx=10,sticky='w')

bukugambara3Entry=Entry(bukuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bukugambara3Entry.grid(row=1,column=1,pady=9,padx=10)
bukugambara3Entry.insert(0,0)

bukugambara4Label=Label(bukuFrame,text="Buku Gambar A4",font=('times new roman',15,'bold'),bg='grey20',fg='white')
bukugambara4Label.grid(row=2,column=0,pady=9,padx=10,sticky='w')

bukugambara4Entry=Entry(bukuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bukugambara4Entry.grid(row=2,column=1,pady=9,padx=10)
bukugambara4Entry.insert(0,0)

bukuhalusLabel=Label(bukuFrame,text="Buku Halus",font=('times new roman',15,'bold'),bg='grey20',fg='white')
bukuhalusLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

bukuhalusEntry=Entry(bukuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bukuhalusEntry.grid(row=3,column=1,pady=9,padx=10)
bukuhalusEntry.insert(0,0)

bukustriminLabel=Label(bukuFrame,text="Buku Strimin",font=('times new roman',15,'bold'),bg='grey20',fg='white')
bukustriminLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

bukustriminEntry=Entry(bukuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bukustriminEntry.grid(row=4,column=1,pady=9,padx=10)
bukustriminEntry.insert(0,0)

bukustriminLabel=Label(bukuFrame,text="Pepak Basa Jawa",font=('times new roman',15,'bold'),bg='grey20',fg='white')
bukustriminLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

pepakbasajawaEntry=Entry(bukuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
pepakbasajawaEntry.grid(row=5,column=1,pady=9,padx=10)
pepakbasajawaEntry.insert(0,0)

alattulisFrame=LabelFrame(productsFrame,text="Alat Tulis",font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
alattulisFrame.grid(row=0,column=1,pady=9,padx=10)

pensilLabel=Label(alattulisFrame,text="Pensil",font=('times new roman',15,'bold'),bg='grey20',fg='white')
pensilLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

pensilEntry=Entry(alattulisFrame,font=('times new roman',15,'bold'),width=10,bd=5)
pensilEntry.grid(row=0,column=1,pady=9,padx=10)
pensilEntry.insert(0,0)

bulpointLabel=Label(alattulisFrame,text="Bolpoint",font=('times new roman',15,'bold'),bg='grey20',fg='white')
bulpointLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

bolpointEntry=Entry(alattulisFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bolpointEntry.grid(row=1,column=1,pady=9,padx=10,sticky='w')
bolpointEntry.insert(0,0)

pensilwarnaLabel=Label(alattulisFrame,text="Pensil Warna",font=('times new roman',15,'bold'),bg='grey20',fg='white')
pensilwarnaLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

pensilwarnaEntry=Entry(alattulisFrame,font=('times new roman',15,'bold'),width=10,bd=5)
pensilwarnaEntry.grid(row=2,column=1,pady=9,padx=10)
pensilwarnaEntry.insert(0,0)

penggarisLabel=Label(alattulisFrame,text="Penggaris",font=('times new roman',15,'bold'),bg='grey20',fg='white')
penggarisLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

penggarisEntry=Entry(alattulisFrame,font=('times new roman',15,'bold'),width=10,bd=5)
penggarisEntry.grid(row=3,column=1,pady=9,padx=10)
penggarisEntry.insert(0,0)

spidolLabel=Label(alattulisFrame,text="Spidol",font=('times new roman',15,'bold'),bg='grey20',fg='white')
spidolLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

spidolEntry=Entry(alattulisFrame,font=('times new roman',15,'bold'),width=10,bd=5)
spidolEntry.grid(row=4,column=1,pady=9,padx=10)
spidolEntry.insert(0,0)

penghapusLabel=Label(alattulisFrame,text="Penghapus",font=('times new roman',15,'bold'),bg='grey20',fg='white')
penghapusLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

penghapusEntry=Entry(alattulisFrame,font=('times new roman',15,'bold'),width=10,bd=5)
penghapusEntry.grid(row=5,column=1,pady=9,padx=10)
penghapusEntry.insert(0,0)

ATKFrame=LabelFrame(productsFrame,text="ATK",font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
ATKFrame.grid(row=0,column=2,pady=9,padx=0)

selotipLabel=Label(ATKFrame,text="Selotip",font=('times new roman',15,'bold'),bg='grey20',fg='white')
selotipLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

selotipEntry=Entry(ATKFrame,font=('times new roman',15,'bold'),width=10,bd=5)
selotipEntry.grid(row=0,column=1,pady=9,padx=10)
selotipEntry.insert(0,0)

amplopLabel=Label(ATKFrame,text="Amplop",font=('times new roman',15,'bold'),bg='grey20',fg='white')
amplopLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

amplopEntry=Entry(ATKFrame,font=('times new roman',15,'bold'),width=10,bd=5)
amplopEntry.grid(row=1,column=1,pady=9,padx=10)
amplopEntry.insert(0,0)

lemLabel=Label(ATKFrame,text="Lem",font=('times new roman',15,'bold'),bg='grey20',fg='white')
lemLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

lemEntry=Entry(ATKFrame,font=('times new roman',15,'bold'),width=10,bd=5)
lemEntry.grid(row=2,column=1,pady=9,padx=10)
lemEntry.insert(0,0)

rautanLabel=Label(ATKFrame,text="Rautan",font=('times new roman',15,'bold'),bg='grey20',fg='white')
rautanLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

rautanEntry=Entry(ATKFrame,font=('times new roman',15,'bold'),width=10,bd=5)
rautanEntry.grid(row=3,column=1,pady=9,padx=10)
rautanEntry.insert(0,0)

stabiloLabel=Label(ATKFrame,text="Stabilo",font=('times new roman',15,'bold'),bg='grey20',fg='white')
stabiloLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

stabiloEntry=Entry(ATKFrame,font=('times new roman',15,'bold'),width=10,bd=5)
stabiloEntry.grid(row=4,column=1,pady=9,padx=10)
stabiloEntry.insert(0,0)

tippxLabel=Label(ATKFrame,text="Tip-x",font=('times new roman',15,'bold'),bg='grey20',fg='white')
tippxLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

tippxEntry=Entry(ATKFrame,font=('times new roman',15,'bold'),width=10,bd=5)
tippxEntry.grid(row=5,column=1,pady=9,padx=10)
tippxEntry.insert(0,0)

billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billareaLabel=Label(billframe,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=18,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root,text="Bill Menu",font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
billmenuFrame.pack()

bukupriceLabel=Label(billmenuFrame,text="Buku Price",font=('times new roman',14,'bold'),bg='grey20',fg='white')
bukupriceLabel.grid(row=0,column=0,pady=6,padx=10,sticky='w')

bukupriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
bukupriceEntry.grid(row=0,column=1,pady=6,padx=10)

alattulispriceLabel=Label(billmenuFrame,text="Alat Tulis Price",font=('times new roman',14,'bold'),bg='grey20',fg='white')
alattulispriceLabel.grid(row=1,column=0,pady=6,padx=10,sticky='w')

alattulispriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
alattulispriceEntry.grid(row=1,column=1,pady=6,padx=10)

ATKpriceLabel=Label(billmenuFrame,text="ATK Price",font=('times new roman',14,'bold'),bg='grey20',fg='white')
ATKpriceLabel.grid(row=2,column=0,pady=6,padx=10,sticky='w')

ATKpriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
ATKpriceEntry.grid(row=2,column=1,pady=6,padx=10)

bukutaxLabel=Label(billmenuFrame,text="Buku Tax",font=('times new roman',14,'bold'),bg='grey20',fg='white')
bukutaxLabel.grid(row=0,column=2,pady=6,padx=10,sticky='w')

bukutaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
bukutaxEntry.grid(row=0,column=3,pady=6,padx=10)

alattulistaxLabel=Label(billmenuFrame,text="Alat Tulis Tax",font=('times new roman',14,'bold'),bg='grey20',fg='white')
alattulistaxLabel.grid(row=1,column=2,pady=6,padx=10,sticky='w')

alattulistaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
alattulistaxEntry.grid(row=1,column=3,pady=6,padx=10)

ATKtaxLabel=Label(billmenuFrame,text="ATK tax",font=('times new roman',14,'bold'),bg='grey20',fg='white')
ATKtaxLabel.grid(row=2,column=2,pady=6,padx=10,sticky='w')

ATKtaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
ATKtaxEntry.grid(row=2,column=3,pady=6,padx=10)

buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10)
emailButton.grid(row=0,column=2,pady=20,padx=5)

printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10)
printButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10)
clearButton.grid(row=0,column=4,pady=20,padx=5)

root.mainloop()
