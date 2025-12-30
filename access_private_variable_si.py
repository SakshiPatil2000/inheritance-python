class Parent:
    def __init__(self):
        self.__name= "Sakshi"
    def getName(self):
        return self.__name

class Child(Parent):
    def show(self):
        print(self.getName())
        
c = Child()
c.show()