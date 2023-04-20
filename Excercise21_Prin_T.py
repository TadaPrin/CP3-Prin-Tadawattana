'''
อ้วนมาก 30.0 ขึ้นไป
อ้วน 25.0 - 29.9
น้ำหนักเกิน 23.0 - 24.9
น้ำหนักปกติ เหมาะสม 18.6 - 22.9
ผอมเกินไป น้อยกว่า 18.5
'''

from tkinter import *
import math

def leftClickButton(event): #(event) คือการบอกว่าให้ทำสิ่งนี้
    print(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)) #.get คือการดึงข้อมูลมาจากwidegetที่เราสร้างไว้
    bmiResult = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    labelresult1.configure(text =float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    if bmiResult <= 18.5:
        labelresult2.configure(text="ผอมเกินไป")
    elif bmiResult <= 22.9:
        labelresult2.configure(text="น้ำหนักปกติ, เหมาะสม")
    elif bmiResult <= 24.9:
        labelresult2.configure(text="น้ำหนักเกิน")
    elif bmiResult <= 29.9:
        labelresult2.configure(text="อ้วน")
    elif bmiResult >= 30.0:
        labelresult2.configure(text="อ้วนมาก")


MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>', leftClickButton) #Left click
calculateButton.grid(row=2, column=0)
labelresult1 = Label(MainWindow, text="ผลลัพธ์")
labelresult1.grid(row=2,column=1)
labelresult2 = Label(MainWindow, text = " ")
labelresult2.grid(row=3,column=1)
MainWindow.mainloop()