import datetime
import currency_converter
from currency_converter import CurrencyConverter
from datetime import date
c = CurrencyConverter()
d = date

from tkinter import *
import math

#Currency conversion from 1st_currency to 2nd_currency
#Example: 100 EUR to USD = 109.81
def Left_Click_Button_1(event):
    import currency_converter
    from currency_converter import CurrencyConverter
    conversion_1 = c.convert(text_box_amount.get(), text_box_currency_1.get(), text_box_currency_2.get())
    print(conversion_1)
    labelresult_1.configure(text =conversion_1)

#Currency conversion with specific date
#Example: 100 EUR to USD at 2013-3-1 = 130.0
#The currency at the date is limited by creator
def Left_Click_Button_2(event):
    import currency_converter
    from currency_converter import CurrencyConverter
    from datetime import date
    c = CurrencyConverter()
    conversion_2 = c.convert(text_box_amount.get(),text_box_currency_1.get(),text_box_currency_2.get(), date=date(int(text_box_year.get()),int(text_box_month.get()),int(text_box_date.get())))
    print(conversion_2)
    labelresult_2.configure(text =conversion_2)

MainWindow = Tk()
label_title_1 = Label(MainWindow, text="Currency Converter Calculation")
label_title_1.grid(row=0,column=1)
label_title_2 = Label(MainWindow, text="Conversion from Currency to Currency")
label_title_2.grid(row=1,column=1)
label_title_from = Label(MainWindow, text="From")
label_title_from.grid(row=2,column=0)
label_currency_1 = Label(MainWindow, text="Currency")
label_currency_1.grid(row=3,column=0)
text_box_currency_1 = Entry(MainWindow)
text_box_currency_1.grid(row=3,column=1)
label_title_to = Label(MainWindow, text="to")
label_title_to.grid(row=4,column=0)
label_currency_2 = Label(MainWindow, text="Currency")
label_currency_2.grid(row=5,column=0)
text_box_currency_2 = Entry(MainWindow)
text_box_currency_2.grid(row=5,column=1)
label_amount = Label(MainWindow, text="Amount")
label_amount.grid(row=6,column=0)
text_box_amount = Entry(MainWindow)
text_box_amount.grid(row=6,column=1)
calculateButton = Button(MainWindow,text = "Calculate")
calculateButton.bind('<Button-1>', Left_Click_Button_1)
calculateButton.grid(row=7, column=0)
labelresult_1 = Label(MainWindow, text="Result")
labelresult_1.grid(row=7,column=1)
label_title_2 = Label(MainWindow, text="Conversion by date")
label_title_2.grid(row=8,column=1)
label_year = Label(MainWindow, text="Year")
label_year.grid(row=9,column=0)
text_box_year = Entry(MainWindow)
text_box_year.grid(row=9,column=1)
label_month = Label(MainWindow, text="Month")
label_month.grid(row=10,column=0)
text_box_month = Entry(MainWindow)
text_box_month.grid(row=10,column=1)
label_date = Label(MainWindow, text="Date")
label_date.grid(row=11,column=0)
text_box_date = Entry(MainWindow)
text_box_date.grid(row=11,column=1)
calculateButton = Button(MainWindow,text = "Calculate")
calculateButton.bind('<Button-1>', Left_Click_Button_2)
calculateButton.grid(row=12, column=0)
labelresult_2 = Label(MainWindow, text="Result")
labelresult_2.grid(row=12,column=1)

MainWindow.mainloop()





