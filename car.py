class Car:
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        if self.price > 10000:
          self.tax = '15%'
        else: self.tax = '12%'
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.display_all()
    def display_all(self):
        print("Price:",self.price)
        print("Speed:",self.speed)
        print("Fuel:",self.fuel)
        print("Mileage:",self.mileage)
        print("Tax:",self.tax)
        print(" ")


car1 = Car(2000,'35mph','Full','15mpg')
car2 = Car(2000,'5mph','Not Full','105mpg')
car3 = Car(2000,'15mph','Kind of Full','95mpg')
car4 = Car(4500,'25mph','Full','30mpg')
car5 = Car(20000000,'35mph','Empty','15mpg')
car6 = Car(3200,'15mph','Kind of Full','50mpg')

