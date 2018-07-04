class Product:
    def __init__(self,price,item_name,weight,brand):
        self.price = price
        self.item = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self
    def addTax(self,decimal):
        self.price = self.price * decimal + self.price
        return self
    def returnItem(self,reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
        if reason_for_return == "like_new":
            self.status = "for sale"
        if reason_for_return == "used":
            self.status = "opened"
            self.price = self.price - self.price * 0.2
        return self
    def displayInfo(self):
        print("Price:",self.price)
        print("Item:",self.item)
        print("Weight:",self.weight)
        print("Brand:",self.brand)
        print("Status:",self.status)
        return self


product1 = Product(50,"foundation",1.0,"Too Faced")
print(product1.displayInfo().addTax(.1).displayInfo())
print(product1.sell().returnItem("defective").displayInfo())


