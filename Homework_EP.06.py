class Homeforsales():
    def __init__(self,proj_name,proj_owner,std_area,std_price,actual_price):
        self.proj_name = proj_name      #ชื่อโครงการ
        self.proj_owner = proj_owner     #ชื่อผูบริหารโครงการ
        self.std_area = std_area            #พื้นที่มาตรฐาน (ตร.ว.)
        self.std_price = std_price             #ราคามาตรฐาน
        self.actual_price =  actual_price    #ราคาสุทธิ รวมหรือหัก พื้นที่ส่วนที่เกิน หรือน้อยกว่าพื้นที่มาตรฐาน
    def Home_Style(self,h_type,h_style,actual_area):
            self.h_type = h_type                     #ลักษณะบ้าน
            self.h_style = h_style                    #แบบบ้าน
            self.actual_area = actual_area       #พื้นที่จริง (ตร.ว.)
            
    def chk_area(self):
        if self.actual_area > self.std_area :
            self.actual_price =   (self.std_price + ((self.actual_area - self.std_area)*20000))
            #ถ้าพื้นที่จริง > พื้นที่มารฐาน ก็จะดิดเพิ่ม ตร.วาละ 2 หมื่นบาท
        elif self.actual_area < self.std_area :
            self.actual_price =   (self.std_price - ((self.std_area - self.actual_area )*20000))
            #ถ้าพื้นที่จริง < พื้นที่มารฐาน ก็จะลดราคาให้ ตร.วาละ 2 หมื่นบาทเช่นกัน
            return self.actual_price 

        
       
class Seller(Homeforsales):
    def seller_details(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    def customer(self,customer_name,customer_gender,customer_age):
        self.customer_name = customer_name
        self.customer_gender = customer_gender
        self.customer_age = customer_age

    def showsale(self):
        print("ชื่อโครงการ : " , self.proj_name , "บริหารโครงการโดย", self.proj_owner)
        print("พนักงานขาย : " , self.name ,"เพศ : "  , self.gender , "อายุ :  ",self.age , "  ปี")
        print("ขายบ้านให้กับ : " , self.customer_name , "เพศ : " ,self.customer_gender,"อายุ : " , self.customer_age," ปี")
        print("ประเภทบ้าน : ", self.h_type,"สไตล์ : " , self.h_style,"พื้นที่ ",self.actual_area , " ตร.วา  ราคาสุทธิ : " ,  f' {self.actual_price : ,.2f} บาท')
        
   #def __str__(self):
   #    return   "{พนักงานขาย} {เพศ} {อาย}".format(self.name,self.gender,self.age)
    #print("ขายบ้าน : ",self.h_type , "สไตล์  : " , self.h_style  , "ให้กับุ : " , self.customer_name,  "เพศ : " , self.customer_gender , "อายุ : " , customer_age , " ปี")
       
    

s01 = Seller("LungWisawa","ลุง-ป้า-น้าอา",50,2000000,0)
s01.seller_details("น.ส.ฉัตรตรี มีสุข","หญิง",26)
s01.customer("นายสมหวัง ดังใจ","ชาย",35)
s01.Home_Style("บ้านเดี่ยว","โมเดิร์น",80.75)
s01.chk_area()

s02 = Seller("LungWisawa","ลุง-ป้า-น้าอา",45,1800000,0)
s02.seller_details("นส.ขวัญฤดี ศรีสว่าง","หญิง",27)
s02.customer("น.ส.จริยา จรรยาดี","หญิง",32)
s02.Home_Style("บ้าแฝด","คลาสสิก",75.28)
s02.chk_area()
print(" + -:) +- :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - ")
s01.showsale()
print(" + -:) +- :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - ")
s02.showsale()
print(" + -:) +- :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - :) + - ")
