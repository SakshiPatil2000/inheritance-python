class Person:
    def __init__(self,name):
        self.name = name
        
class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id= emp_id
        
class Manager(Employee):
    def __init__(self, name, emp_id,department):
        super().__init__(name, emp_id)
        self.department = department
    def display(self):
        print(self.name, self.emp_id,self.department)

obj = Manager("Sakshi",1722,"Engineering")
obj.display()