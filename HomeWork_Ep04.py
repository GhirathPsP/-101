import csv
from tkinter import *
from tkinter import messagebox
GUI = Tk()
GUI.title("EeZ_SMLB")
GUI.geometry("800x550")
def writecsv(datalist):
    with open('CSV_Test_01.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) # datalist = ['pen','pencil','eraser']

def read_csv():
    with open('CSV_Test_01.csv',encoding='utf-8',newline='') as fr:
        fread = csv.reader(fr)
        

        i = 6       
        for rng in fread:
            #print(rng)
            Label(GUI,text=rng,font=('Cordia New',20,'bold')).grid(row=i+1,column=2)
            i+=1   
            
        
    
def Calbmi():   #คำนวณค่า BMI แล้ว Write ลง csv
    BMI =  float(E_weight.get()) / ((float(E_height.get())/100)**2)
    L_Result = Label(GUI,text=f' ฺค่า BMI =  {BMI : ,.2f}  ก.ก/ตร.ม. ',font=('Cordia New',20,'bold')).grid(row= 5 , column = 2)
    bmi = f'{BMI : ,.2f}'
    #messagebox.showinfo('BMI =  ' , bmi)
    if BMI <  18.5 :                             bmi_result =  'ต่ำกว่าเกณฑ์'
    elif BMI >= 18.5 and BMI <  22.9 : bmi_result =  'ปรกติ'
    elif BMI >=22.9 and BMI < 24.9 :  bmi_result =  'น้ำหนักเกิน'
    elif BMI >= 24.9 and  BMI < 29.9 :  bmi_result =  'โรคอ้วน'
    else:                                          bmi_result =  'โรคอ้วนอันตราย'

    L_bmi = Label(GUI,text='สถาวะ : ' + bmi_result,font=('Cordia New',20,'bold')).grid(row= 5 , column = 3)   
    box = []
    box.append(E_Name.get())
    box.append(E_height.get())
    box.append(E_weight.get())
    box.append(bmi)
    box.append(bmi_result)
    writecsv(box)
    messagebox.showinfo('Write CSV','D O N E')
def putheader():
    box = []
    box.append('Name')
    box.append('Height (cm)')
    box.append('Weight.(kg)')
    box.append('BMI (kg/m2)')
    box.append('Status')
    writecsv(box)

def ExitWindow():
    GUI.destroy()
    
    
L0 = Label(GUI,text="โปรแกรมอ่าน/เขียน ไฟล์ CSV",font=('Cordia New',25,'bold')).grid(row=0,column=3)
L_Name = Label(GUI,text='ใส่ชื่อ',font=('Cordia New',20,'bold')).grid(row=2,column=2)
E_Name = StringVar()
E1 = Entry(GUI,font=('Cordia New',20,'bold'),textvariable=E_Name).grid(row=2,column=3)           

L2 = Label(GUI,text="ส่วนสูง (ซ.ม.)",font=('Cordia New',20,'bold')).grid(row=3,column=2)
E_height = StringVar()
E2 = Entry(GUI,font=('Cordia New',20,'bold'),textvariable=E_height,).grid(row=3,column=3)           

L3 = Label(GUI,text="น้ำหนัก (ก.ก.)",font=('Cordia New',20,'bold')).grid(row=4,column=2)
E_weight = StringVar()
E3 = Entry(GUI,font=('Cordia New',20,'bold'),textvariable=E_weight).grid(row=4,column=3)

B1 = Button(GUI,text="Calculate & Write CSV ",font =('Cordia New',20,'bold'),width = 17,height=1,command=Calbmi,fg="Brown",bg="Pink").grid(row=2,column=5)
B2 = Button(GUI,text="Exit",font =('Cordia New',20,'bold'),width = 17,height=1,command=ExitWindow,fg="Brown",bg="Yellow").grid(row=3,column=5)
#B3 = Button(GUI,text="Clear Value",font =('Cordia New',20,'bold'),width = 17,height=1,command=Clear_Data,fg="Blue",bg="Orange").grid(row=4,column=5)

Bread_CSV = Button(GUI,text="Read CSV",font =('Cordia New',20,'bold'),width = 17,height=1,command=read_csv,fg="Brown",bg="Lightgreen").grid(row=4,column=5)

GUI.mainloop()
