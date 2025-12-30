class Animal:
    def __init__(self,name):
        self.name =name
    def speak(self):
        print('Animal makes a sound')
class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed
    def show(self):
        print(self.name,self.breed)
        
        
d = Dog('Tommy','labrador')
d.speak()
d.show()
print(isinstance(d,Dog))
print(isinstance(d,Animal))
print(issubclass(Dog,Animal))
print(issubclass(Animal,Dog))