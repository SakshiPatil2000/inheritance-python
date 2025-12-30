class Shape:
    def draw(self):
        print("Drawing Shape")

class Rectangle(Shape):
    def area(self,l,b):
        print("Area of rectangle is : \n",l*b)

class Circle(Shape):
    def area(self,r):
        print("Area of circle is : \n",3.14*r*r)
        
r =Rectangle()
r.draw()
r.area(10,8)

c = Circle()
c.draw()
c.area(4)