import tkinter as tk
GUI = tk.Tk()
GUI.title("EeZ_SMLB")
GUI.geometry("800x250+100+100")
def calculate_Volumn():
    base = float(base_entry.get())
    height = float(height_entry.get())
    Thick = float(Thick_entry.get())
    Cube_Volumn = base * height * Thick
    result_label.config(text=f"ปริมาตรของลูกบาศก์ =    {Cube_Volumn: ,.2f}  ลบ.ม.")

def Colse_Win():
       GUI.destroy()
       

L0 = tk.Label(GUI,text="โปรแกรมคำนวณ ปริมาตรของลูกบาศ์ก",font=50)
L0.grid(row=0,column=3)
L1 = tk.Label(GUI,text="ใส่ความกว้าง (เมตร)",font=50)
L1.grid(row=2,column=2)
base_entry = tk.Entry(GUI)
base_entry.grid(row=2,column=3)
L2 = tk.Label(GUI,text="ใส่ความยาว (เมตร)",font=50)
L2.grid(row=4,column=2)
height_entry = tk.Entry(GUI)
height_entry.grid(row=4,column=3)
L3 = tk.Label(GUI,text="ใส่ความสูง (เมตร)",font=50)
L3.grid(row=6,column=2)
Thick_entry = tk.Entry(GUI)
Thick_entry.grid(row=6,column=3)

calculate_button = tk.Button(GUI, text="Calculate", width=15,command=calculate_Volumn)
calculate_button.grid(row=7,column=4)
Close_Button = tk.Button(GUI,text="Exit",fg="Blue",bg="Lightgreen",width=15,command=Colse_Win)
Close_Button.grid(row=7,column=6)
result_label = tk.Label(GUI,font=80)
result_label.grid(row=9,column=3)
# Start the main loop
GUI.mainloop()
