class Rectangle:
    def CalculateArea(self):
        print("Enter length:")
        self.1=float(input())
        print("Enter breadth:")
        self.b=float(input())
        area=self.1*self.b
        print("Area of rectangle",(area))

    def Calculateperimeter(self):
        Perimeter=2*(self.1+self.2)
        print(Perimeter)


c=Rectangle()
x=c.CalculateArea()
y=c.CalculatePerimeter()              
