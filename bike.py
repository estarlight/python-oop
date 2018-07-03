class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print(self.price, self.max_speed, self.miles)
        return self
    def ride(self):
        print("Riding")
        self.miles += 10
        return self
    def reverse(self):
        print("Reversing")
        self.miles -= 5
        if self.miles <0:
          self.miles = 0
        return self


bike1 = Bike(200,"25mph")
print(bike1.displayInfo())
print(bike1.ride())
print(bike1.ride())
print(bike1.ride())
print(bike1.reverse())
print(bike1.displayInfo())

bike2 = Bike (150,"20mph")
print(bike2.displayInfo().ride().ride().reverse().reverse().displayInfo())

bike3 = Bike(300,"30mph")
print(bike3.displayInfo().reverse().reverse().reverse().displayInfo())