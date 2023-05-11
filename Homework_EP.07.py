from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import csv
global data 

def exportcsv():
    data = ["แปลง : " + s1.h_id,"แบบบ้าน : " + s1.h_type,"สไตล์ : " + s1.h_style,"พื้นที่ : " + str(s1.actual_area),"ราคา : " + str(s1.actual_price),"พนักงานขาย :" + s1.name , "ชื่อลูกค้า : " + s1.b_name , "อายุลูกค้า : " + str(s1.b_age)   ,"เบอร์โทรอลูกค้า : " + s1.b_phone , "ที่อยู่ลูกค้า : " + s1.b_address]
    with open('CSV_Write.csv', 'a', encoding='utf-8',newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(data)

        messagebox.showinfo("Test",data)
        #messagebox.showinfo("Write CSV" , "A L L    D O N E")


global data
Home_ID = []
Fnt = ('Cordia New',20,'bold')

class Home():
    
    def __init__(self,proj_name,proj_owner,std_area,std_price,actual_price):
        self.proj_name = proj_name
        self.proj_owner = proj_owner
        self.std_area = std_area
        self.std_price = std_price
        self.actual_price = actual_price
    def h_details(self,h_type,h_style,actual_area,h_id):
        self.h_type = h_type
        self.h_style = h_style
        self.actual_area = actual_area
        self.h_id = h_id

    def chk_price(self):
        if self.actual_area > self.std_area:
            self.actual_price = self.std_price + (self.actual_area - self.std_area)*20000

        elif self.actual_area < self.std_area:
            self.actual_price = self.std_price - (self.std_area - self.actual_area)*20000
        else:
            self.actual_price = self.std_price
    
     
class Sell(Home):
    def s_details(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
    def buyer(self,b_name,b_age,b_phone,b_address):
        self.b_name = b_name
        self.b_age = b_age
        self.b_phone = b_phone
        self.b_address = b_address
    def reserve(self):
        Home_ID.remove(self.h_id)
        return Home_ID

    
    def show_data(self):
        print("โครงการ : " + self.proj_name + "  บริหารโครงการโดย : " + self.proj_owner)
        print("ประเภท : " + self.h_type + "  สไตล์ : " + self.h_style + "  เนื้อที่ : " + str(self.actual_area) + " ตร.วา")
        print("พนักงานขาย : " + self.name + " อายุ : " + str(self.age) + " เพศ : " + self.gender)
        print("ชื่อลูกค้า : " + self.b_name + " อายุ : " + str(self.b_age) + "เบอร์โทร : " + self.b_phone + " ที่อยู่ : " + self.b_address)
        print( f' ราคาบ้าน :  {self.actual_price : ,.2f} บาท')

        GUI = Tk()
        GUI.title("EeZ_SMLB")
        GUI.geometry("800x500")
        L_title = Label(GUI,text="สรุปข้อมูลการจองบ้าน",font=Fnt,width=55,bg='lightgreen',).place(x=100,y=0)
        L_0 = Label(GUI,text="ชื่อโครงการ : " + self.proj_name + "   บริหารโครงการโดย : " + self.proj_owner,font=Fnt).place(x=20,y=50)
        L_area = Label(GUI,text="พื้นที่มาตรฐาน",font=Fnt).place(x=20,y=100)
        E_area_input = StringVar(value =  f' {self.std_area:,.2f}')
        E_area = Entry(GUI,textvariable=E_area_input,font=Fnt,width=7,bg='lightgrey',state=DISABLED).place(x=150,y=100)
        L_unit =  Label(GUI,text="ตร.วา   ราคามาตรฐาน  ",font=Fnt).place(x=230,y=100)
        
        E_price_input = StringVar(value =  f' {self.std_price:,.2f} ')
        E_price = Entry(GUI,textvariable=E_price_input,font=Fnt,width=18,bg='lightgrey',state=DISABLED).place(x=450,y=100)
        L_unit =  Label(GUI,text="บาท",font=Fnt).place(x=600,y=100)
        L_sale =  Label(GUI,text="พนักงานขาย",font=Fnt).place(x=20,y=150)
        E_sale_input = StringVar(value =  self.name)
        E_sale = Entry(GUI,textvariable=E_sale_input,font=Fnt,width=25,bg='lightgrey').place(x=150,y=150)
        
        L_sgender = Label(GUI,text=" เพศ : ",font=Fnt).place(x =400,y=150)
        E_sgender_input = StringVar(value= self.gender)
        E_sgender = Entry(GUI,textvariable = E_sgender_input ,width=5, font=Fnt , bg='lightgrey',justify=CENTER).place(x=450,y=150)

        L_sage = Label(GUI,text=" อายุ : ",font=Fnt).place(x =500,y=150)
        E_sage_input = StringVar(value= self.age)
        E_sage = Entry(GUI,textvariable = E_sage_input ,width=5, font=Fnt , bg='lightgrey',justify=CENTER).place(x=550,y=150)
        L_sale_unit = Label(GUI,text="ปี",font=Fnt).place(x =600,y=150)
        
        # Customer
        L_buyer = Label(GUI,text="ชื่อลูกค้า",font=Fnt,width=10).place(x=20,y=200)
        E_buyer_input = StringVar(value= self.b_name)
        E_buyer = Entry(GUI,textvariable=E_buyer_input , font=Fnt , width=20,bg='lightgrey',state=DISABLED).place(x=150,y=200)
        
        L_bage = Label(GUI,text=" อายุ : ",font=Fnt).place(x =380,y=200)
        E_bage_input = StringVar(value= self.age)
        E_bage = Entry(GUI,textvariable = E_bage_input ,width=5, font=Fnt , bg='lightgrey',justify=CENTER,state=DISABLED).place(x=430,y=200)
        L_bage_unit = Label(GUI,text=" ปี   เบอร์โทร : ",font=Fnt).place(x =480,y=200)
        
         #customer phine
        E_bphone_input = StringVar(value= self.b_phone)
        E_bphone = Entry(GUI,textvariable = E_bphone_input ,width=15, font=Fnt , bg='lightgrey',justify=CENTER).place(x=600,y=200)
        
        L_b_address = Label(GUI,text="ที่อยู่",font=Fnt,width=10).place(x=20,y=250)
        E_b_address_input = StringVar(value= self.b_address)
        E_b_address = Entry(GUI,textvariable=E_b_address_input , font=Fnt , width=50,bg='lightgrey').place(x=120,y=250)
        
        L_hid = Label(GUI,text="ขายบ้านแปลง : ",font=Fnt).place(x=20,y=300)
        E_hid_input = StringVar(value= self.h_id)
        E_bhid = Entry(GUI,textvariable = E_hid_input ,width=5, font=Fnt , bg='lightgrey',justify=CENTER).place(x=150,y=300)
        L_htype = Label(GUI,text="ประเภท : ",font=Fnt).place(x=220,y=300)
        E_htype_input = StringVar(value= self.h_type)
        E_htype = Entry(GUI,textvariable = E_htype_input ,width=15, font=Fnt , bg='lightgrey',justify=CENTER).place(x=320,y=300)
        L_hstyle = Label(GUI,text="สไตล์ : ",font=Fnt).place(x=480,y=300)
        E_hstyle_input = StringVar(value= self.h_style)
        E_hstyle = Entry(GUI,textvariable = E_hstyle_input ,width=15, font=Fnt , bg='lightgrey',justify=CENTER).place(x=550,y=300)
        
        # Actual Area , Actual Price
        L_act_area = Label(GUI,text="พื้นที่จริง",font=Fnt).place(x=20,y=350)
        E_act_area_input = StringVar(value =  f' {self.actual_area:,.2f}')
        E_act_area = Entry(GUI,textvariable=E_act_area_input,font=Fnt,width=7,bg='lightgrey').place(x=150,y=350)
        L_actual_unit =  Label(GUI,text="ตร.วา   ราคาสุทธิ  ",font=Fnt).place(x=230,y=350)
        
        E_actual_price_input = StringVar(value =  f' {self.actual_price:,.2f} ')
        E_actual_price = Entry(GUI,textvariable=E_actual_price_input,font=Fnt,width=15,bg='lightgrey').place(x=380,y=350)
        L_actual_unit =  Label(GUI,text="บาท",font=Fnt).place(x=530,y=350)

        def exit_win():
            GUI.destroy()

        def disp():
            
            data1 = ["แปลง : " + E_hid_input.get(),"แบบบ้าน : " + E_htype_input.get(),"สไตล์ : " + E_hstyle_input.get()
             ,"พื้นที่ : " + str(E_act_area_input.get()),"ราคา : " + str(E_actual_price_input)
             ,"พนักงานขาย :" + E_sale_input.get() , "เพศ : " + E_sgender_input.get() ,"อายุ : " + str(E_sage_input.get()) + " ปี"
             , "ชื่อลูกค้า : " + E_buyer_input.get() , "อายุลูกค้า : " + str(E_bage_input.get())
             ,"เบอร์โทรอลูกค้า : " + E_bphone_input.get() , "ที่อยู่ลูกค้า : " + E_b_address_input.get()
         ]
            with open('CSV_Write.csv', 'a', encoding='utf-8',newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(data1)

                messagebox.showinfo("Write CSV" , data1)


        B_1 = Button(GUI,text="Close",font=Fnt,bg='orange',width=12,height=2,command=exit_win).place(x=350,y=400)
        B_2 = Button(GUI,text="บันทึก CSV\n CLASS",font=Fnt,bg='violet',width=12,command=exportcsv).place(x=500,y=400)
        B_3 = Button(GUI,text="บันทึก CSV\n GUI",command=disp,font=Fnt,bg='skyblue',width=12).place(x=650,y=400)

        GUI.mainloop()

# Create Object s1 🏀🏀🏀🏀🏀🏀🏀🏀🏀🏀🏀🏀🏀🏀🏀🏀🏀🏀🏀
#Home_ID = ['A01','A02','A03','A04','A05','A06','A07','A08','A09','A10']
for i  in range(10):
    if i < 9:
        Home_ID.append("A0" + str(i+1))
    else:
        Home_ID.append("A0" + str(i+1))
                       

s1 = Sell("Lung Wisawa","ลุง-ป้า-น้า-อา",70,1.8E+6,0)
s1.h_id = random.choice(Home_ID)
s1.h_details("บ้านเดี่ยว","โมเดิร์น",95.59,s1.h_id)
s1.chk_price()
s1.s_details("น.ส.รัชนี   มีทรัพย์มาก","หญิง",25)
s1.buyer("นายวัฒนา   ใฝ่หาความรู้",35,"045-585-0852","32/1 หมู่ 4 ต.พลา อ.บ้านฉาง จ.ระยอง  21130")

#s1.show_data()

#_Create Object s2 🍊🍊🍊🍊🍊🍊🍊🍊🍊
s2 = Sell("Lung Wisawa","ลุง-ป้า-น้า-อา",80,2.0E+6,0)
s2.h_id = random.choice(Home_ID)
s2.h_details("บ้านเดี่ยว","โมเดิร์น",78.87,s2.h_id)
s2.chk_price()
s2.s_details("น.ส.ลักษณา  มหาโชค","หญิง",27)
s2.buyer("นายประเสริฐ  เลิศทุกสิ่ง",38,"085-252-0250","123/4 หมู่ 5 ต.ห้วยใหญ่ อ.บางละมุง จ.ชลบุรี  20150")
#s2.reserve()
#s2.show_data()

#__Create Object s13🍉🍉🍉🍉🍉🍉🍉🍉🍉
s3 = Sell("Lung Wisawa","ลุง-ป้า-น้า-อา",70,1.8E+6,0)
s3.h_id = random.choice(Home_ID)
s3.h_details("บ้านเดี่ยว","โมเดิร์น",80.88,s3.h_id)
s3.chk_price()
s3.s_details("น.ส.ณัฐกานต์   การงานชอบ","หญิง",26)
s3.buyer("นางวารี ศรีเทพ",37,"055-454-5455","34/5 หมู่ 6 ต.ตะเคียนทอง อ.เขาคิชฌกูฏ จ.จันทบุรี  22210")
#s3.reserve()
#s3.show_data()
#🌻🌻🌻🌻🌻🌻🌻🌻🌻
s4 = Sell("Lung Wisawa","ลุง-ป้า-น้า-อา",80,2.0E+6,0)
s4.h_id = random.choice(Home_ID)
s4.h_details("บ้านเดี่ยว","โมเดิร์น",99.88,s3.h_id)
s4.chk_price()
s4.s_details("น.ส.ลักษณา  มหาโชค","หญิง",27)
s4.buyer("นายสุรเดช   มีเมตตา",30,"045-025-5225","55/6 หมู่ 7 ต.บ่อวิน อ.ศรีราชา จ.ชลบุรี 20230")
#s4.reserve()
#s4.show_data()
#🎏🎏🎏🎏🎏🎏🎏🎏

# Run Object
s1.reserve()
s1.show_data()

