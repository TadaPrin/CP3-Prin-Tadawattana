class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")
class Car(Vehicle):
    def Detail(self):
        print("The License Number : ", self.licenseCode, "Serial Number : ", self.serialCode)
class Van(Vehicle):
    def SpeedLimit(self):
        print("The License Number : ", self.licenseCode, "Serial Number : ", self.serialCode)
        print("Speed Limitation <= 80 km/hr")
class Pickup(Vehicle):
    def Regulation(self):
        print("The License Number : ", self.licenseCode, "Serial Number : ", self.serialCode)
        print("Do not sit in the back of the truck")

car1 = Car()
car1.licenseCode = "AB4150"
car1.serialCode = "AABNUD45215"
car1.turnOnAirConditioner()
car1.Detail()

van1 = Van()
van1.licenseCode = "SC8452"
van1.serialCode = "XBD44874HG"
van1.turnOnAirConditioner()
van1.SpeedLimit()

pickup1 = Pickup()
pickup1.licenseCode = "DX7809"
pickup1.serialCode = "JHG788456"
pickup1.turnOnAirConditioner()
pickup1.Regulation()