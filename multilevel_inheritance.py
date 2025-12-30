class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
class Puppy(Dog):
    def weep(self):
        print("Puppy is weeping")

p = Puppy()
p.eat()
p.bark()
p.weep()