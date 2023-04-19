CustomerNumber = input("CustomerNumber : ")
def login(CustomerNumber):
    print("Welcome to Shop Service")
    while CustomerNumber != "11232" :
        CustomerNumber = input("CustomerNumber incorrect, Please try again : ")
    if CustomerNumber == "11232" :
        print("Welcome customer Number : ", CustomerNumber)
        Password = input("Password : ")
    while Password != "Pointbreak":
        Password = input("Incorrect Password, Please try again : ")
    if Password == "Pointbreak" :
        return showmenu()

def showmenu():
    print("This is your assistant for calculate your items")
    print("Please select at the menu")
    print("1. Your current items")
    print("2. vat Calculator")
    print("3. Price Calculator")
    print("4. Exit")
    print("More question call 02-090xxxx")
    return CustomerSelect(CustomerSelect)

def CustomerSelect(CustomerSelect):
    CustomerSelect = input(">>")
    if CustomerSelect == "1" :
        print("1. Resin 3 pieces")
        print("2. Potion 2 bottles")
        print("3. Special leaf 1 pack")
        print("------")
        return showmenu()
    elif CustomerSelect == "2" :
        return vatCalculate()
    elif CustomerSelect == "3" :
        return priceCalculate()
    elif CustomerSelect == "4" :
        print("THANK YOU")

def vatCalculate():
    totalPrice = int(input("Enter Total Price>> "))
    vat = 10
    result = totalPrice+(totalPrice * (vat / 100))
    print(result)
    print("------")
    return showmenu()

def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    price3 = int(input("Third Product Price : "))
    result = price1+price2+price3
    print("The total are", result)
    print("Do you want to calculate total Price include VAT", "y or n  >> ")
    if input() == "y":
        return vatCalculate()
    else:
        print("THANK YOU")



login(CustomerNumber)