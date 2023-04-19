SystemMenu = {"ก๋วยเตี๋ยวไก่" : 45, "เกาเหลาไก่" : 50, "ก๋วยเตี๋ยวไก่พิเศษ" : 50, "ก๋วยจั๊บ" : 50}
menuList = []

def showBill():
    total = 0
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1], "บาท")
        total += int(menuList[number][1])
    print("ราคารวม ", total, "บาท")

while True:
    menuName = input("Plese Enter Menu : ")
    if menuName.lower() == "ออก":
        break
    else:
        menuList.append([menuName, SystemMenu[menuName]])

showBill()