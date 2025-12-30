class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print(self.name,'is barking')
        
d = Dog("Tommy")
d.speak()
d.bark()
