from tkinter import *
from math import *
GUI = Tk()
GUI.title("EeZ_SMLB")
GUI.geometry("550x300")
def CirArea():
    C_Area =  pi * float(txt.get())* float(txt.get()) 
    L_Result = Label(GUI,text=f"Circle Area (Radius) = {C_Area : ,.2f} ",font = 100).grid(row=5,column=2)
def CirArea_D():
    C_Area_D =  0.25 * pi * float(txt2.get())* float(txt2.get())
    L_Result_D = Label(GUI,text=f"Circle Area (Diameter) = {C_Area_D : ,.2f} ",font = 100).grid(row=8,column=2)
    
def ExitWin():
      GUI.destroy()

L0 = Label(GUI,text="Program Calculate Circle Area",font=100).grid(row=0,column=2)
L1 = Label(GUI,text="Enter Radius",font=100).grid(row=2,column=1)
txt = StringVar()
R_Entry = Entry(GUI,textvariable=txt,font=100).grid(row=2,column=2)
B1 = Button(GUI,text="CALCULATE",width = 12,font=100,fg="Brown",bg="Pink",command=CirArea).grid(row=4,column=2)

L2 = Label(GUI,text="Enter Diameter",font=100).grid(row=6,column=1)
txt2 = StringVar()
R2_Entry = Entry(GUI,textvariable=txt2,font=100).grid(row=6,column=2)
Bd2 = Button(GUI,text="CALCULATE",width = 12,font=100,fg="Brown",bg="Pink",command=CirArea_D).grid(row=7,column=2)
B2_d = Button(GUI,text="Exit",width = 12,font=100,fg="Brown",bg="Yellow",command=ExitWin).grid(row=9,column=2)


GUI.mainloop()
