totalPrice = int(input("Fill the total Price : "))
def vatCalculate(totalPrice):
    result = totalPrice+totalPrice*(7/100)
    return result

print("The total Price (VAT include) : ", vatCalculate(totalPrice))