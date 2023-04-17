CustomerNumber = input("CustomerNumber :")
Password = input("Password :")
if CustomerNumber == "11232" and Password == "Pointbreak" :
    print("Welcome dear customer no.11232")
    print("This is your assistant for calculate your items")
    print("Please select at the menu")
    print("1. Your current items")
    print("2. VAT")
    print("3. Price Calculator")
    print("More question call 02-090xxxx")
    Customerselect = input(">>")
    if Customerselect == "1":
        print("1. Resin 3 pieces")
        print("2. Potion 2 bottles")
        print("3. Special leaf 1 pack")
    elif Customerselect == "2":
        print("The VAT is increase to 10% from now")
    elif Customerselect == "3":
        price1 = int(input("First Product Price : "))
        price2 = int(input("Second Product Price : "))
        price3 = int(input("Third Product Price : "))
        print(price1+price2+price3+((price1+price2+price3)*(10/100)))
        print("The price will charge VAT 10%")
else:
    print("Access denied")