class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health = self.health - 1
        return self
    def run(self):
        self.health = self.health - 5
        return self
    def displayHealth(self):
        print(self.health)
        return self

animal1 = Animal("bear",100)
print(animal1.walk().walk().walk().run().run().displayHealth())

class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__(name, 150)
        # self.health = 150
    def pet(self):
        self.health += 5
        return self

dog1 = Dog("Fido")
print(dog1.walk().walk().walk().run().run().pet().displayHealth())


class Dragon(Animal):
    def __init__(self,name):
        super(Dragon,self).__init__(name,170)
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        print("I am a dragon")
        return self


dragon1 = Dragon("Charmander")
print(dragon1.fly().displayHealth())


print(dog1.displayHealth())

