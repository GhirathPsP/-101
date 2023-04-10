from tkinter import *
from tkinter import messagebox
import random
GUI = Tk()
GUI.title("EeZ_SMLB")
GUI.geometry("800x400")

friend = list({"Amornthep","Betty","Caterine","Elvis","George","Hendric"})
Gift =   list({"ทองคำแท่งหนัก 1 บาท ","Iphone 14 Pro","Gaming Notebook","ตู้เย็น 2 ประต 12 คิวบ์ู","สมาร์ททีวี 43 นิ้ว","เครื่องเสียง Marshell"})
#print(Ls[1])
def RAND():
    i = random.randint(0,len(friend)-1)
    j = random.randint(0,len(Gift)-1)
    #messagebox.showinfo('Rand',friend[i] + Gift[j])
    bg_color = '#' + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    Label(GUI,text=friend[i] + 'ได้รับรางวัล : ' + Gift[j],font=('Cordia New',25,'bold'),bg=bg_color,width = 40).pack()
    del friend[i]
    del Gift[j]
    messagebox.showinfo("รางวัลที่เหลืออย",Gift)

def Exit_Win():
    GUI.destroy()
    
B_1 = Button(GUI,text="จับรางวัล",font=('Cordia New',20,'bold'),command=RAND,bg='LightGreen',width=12).pack()
B_Exit = Button(GUI,text="ออก",font=('Cordia New',20,'bold'),command=Exit_Win,bg='Pink',width=12).pack()
  
GUI.mainloop()

