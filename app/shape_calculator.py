class Shape:
    def __init__ (self,color):
        self.color = color

    
    # --- THE ABSTRACT METHOD DEFINITION ---
    def calculate_area(self):
        raise NotImplementedError("Architectural Rule Violation: You must implement calculate_area() in the child class!")

    
    def display_method(self):
        area = self.calculate_area()
        print(f"Shape Aesthetics : Color is {self.color}")
        print(f"The area is {area}")

class Rectangle(Shape):
    def __init__(self,color,length,width):
        super().__init__(color)
        self.length=length
        self.width=width

    def calculate_area(self):
        return self.width*self.length

class Square(Rectangle):
    def __init__ (self,color,side):
        super().__init__(color,side,side)
        self.side=side


def polymorphic_calculate_area(shape_lis):
    total_area=0
    for shape in shape_lis:

        try:
            area = shape.calculate_area()
            total_area+=area
        except NotImplementedError as err:
            print(f"Skipping a shape: {err}")
        except Exception as err:
            print(f"Unexpected error: {err}")

    print(f"The total area of all the shape is {total_area}")




if __name__ == "__main__":

    rectan = Rectangle("green",10,12)
    squar = Square("blue",5)
    shapes=[rectan,squar]
    polymorphic_calculate_area(shapes)



        
