from tkinter import *
from tkinter import messagebox
from random import  *
import math


GUI = Tk()
GUI.title("EeZ_SMLB")
GUI.geometry("800x300")
def  ShowAns():
       Vol =  float(Width.get()) * float(Length.get()) * float(Thick.get())
       B2 = Label(GUI,text= f"ปริมาตรลูกบาศก์  =   {Vol :,.2f}  ลบ.ม.",font=100).grid(row=8,column=2)
def ExitWin():
       GUI.destroy()
       #B2 = Button(GUI,text=str(Vol),fg="Red",bg="Green",font=100).grid(row=5,column=4)

L0 = Label(GUI,text="โปรแกรมคำนวณปริมารตลูกบาศก์",font=70).grid(row=0,column=3)
L1 = Label(GUI,text="กรุณาใส่ความกว้าง (เมตร)",font=50).grid(row=1,column=2)
num1 = randint(100,200)
Width = StringVar()
Ent1 = Entry(GUI,textvariable=Width,font=50).grid(row=1,column=3)
L2 = Label(GUI,text="กรุณาใส่ความยาว (เมตร)",font=50).grid(row=3,column=2)
Length = StringVar()
Ent2 = Entry(GUI,text="",textvariable=Length,font=50).grid(row=3,column=3)
L3 = Label(GUI,text="กรุณาใส่ความหนา (เมตร)",font=50).grid(row=5,column=2)
Thick = StringVar()
Ent3 = Entry(GUI,textvariable=Thick,font=50).grid(row=5,column=3)

B1 = Button(GUI,width=12,command = ShowAns,text="Calculate",fg="Red",bg="Green",font=100).grid(row=6,column=4)
B2 = Button(GUI,width=12,command = ExitWin,text="Exit",fg="Black",bg="Yellow",font=100).grid(row=7,column=4)


GUI.mainloop()          
