from abc import ABC,abstractmethod

# Class Creation
class Cars(ABC):
    def __init__(self, model, year, price, availableForSale = False):
        self.model = model
        self.year = year
        self.price = price
        self.availableForSale = availableForSale

    def sumPrice(self, passedPrice, passedPrice2 = 0):
        return float(self.price) + float(passedPrice) + float(passedPrice2)
        
    # Abstraction
    def forSale(self):
        pass

    # Encapsulation
    def __str__(self):
        available = "No"
        if self.availableForSale == False:
            available = "No"
        else:
            available = "Yes"

        return "Details of your Vehicle" + \
            "\nModel: "+self.model +\
            "\nYear: "+self.year +\
            "\nPrice: "+self.price+\
            "\nAvailable For Sale: " + available
             
# Object Creation 
toyota = Cars("Rav4", "2015", "18999.99")
lexus = Cars("IS250", "2018", "24599.99", False)
honda = Cars("Civic", "2009", "8999.99", True)

# Inhertance & Polymorphism
print(toyota.sumPrice(lexus.price))
print(toyota.sumPrice(lexus.price, honda.price))
# Use of str()
print(honda)
 


class militaryVehicles(Cars):
    # Inheritance
    def __init__(self, model, year, price, availableForSale, militaryBase, countryName, armored = "False"):
        Cars.__init__(self, model, year, price, availableForSale)
        self.militartBase = militaryBase
        self.countryName = countryName
        self.__armored = armored
    # Abstraction
    def forSale(self):
        available = "No"
        if self.availableForSale == False:
            available = " Not"
        else:
            available = '';    
        print("It's" + available + " For Sale.")

    # Encapsulation
    def getArmored(self):
        print(self.__armored)
    def setArmored(self, armored):
        self.__armored = armored
    # Encapsulation   
    def __str__(self):
        # Inheritance
        return super(militaryVehicles, self).__str__() +\
                "\nMilitary Base: "+self.militartBase+\
                "\nCountry of Service: " + self.countryName

f90 = militaryVehicles("F90 Rover", "2020", "189250.99", False, "AO202", "Canada",)
f88 = militaryVehicles("F90 Rover", "2020", "189250.99", True, "AO202", "Canada",)
print("----------------")
print(f90)
f90.setArmored("True")
f90.getArmored()
# Call abstract methods
f90.forSale()
f88.forSale()

