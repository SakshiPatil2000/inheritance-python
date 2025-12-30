class Father:
    def skill(self):
        print("Driving","Cooking")
class Mother:
    def skill(self):
        print("Business","Painting")
class Child(Father,Mother):
    pass

c = Child()
c.skill()