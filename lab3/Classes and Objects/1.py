import math
class MyShape:
    def __init__(self, color="DefaultColor", is_filled=False):
        self.color = color
        self.is_filled = is_filled

    def __str__(self):
        return f"Color: {self.color}, Filled: {self.is_filled}"

    def getArea(self):
        return 0


class Rectangle(MyShape):
    def __init__(self, color="DefaultColor", is_filled=False, x_top_left=0, y_top_left=0, length=1, width=1):
        super().__init__(color, is_filled)
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle - {super().__str__()}, X Top Left: {self.x_top_left}, Y Top Left: {self.y_top_left}, Length: {self.length}, Width: {self.width}"

class Circle(MyShape):
    def __init__(self, color="DefaultColor", is_filled=False, x_center=0, y_center=0, radius=1):
        super().__init__(color, is_filled)
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def getArea(self):
        return math.pi * (self.radius ** 2)


    def __str__(self):
        return f"Circle - {super().__str__()}, X Center: {self.x_center}, Y Center: {self.y_center}, Radius: {self.radius}"

def create_rectangle_from_console():
    color = input("Enter color for rectangle (default is DefaultColor): ")
    is_filled = input("Is the rectangle filled? (True/False, default is False): ").lower() == 'true'
    x_top_left = float(input("Enter X coordinate of the top-left corner: "))
    y_top_left = float(input("Enter Y coordinate of the top-left corner: "))
    length = float(input("Enter length of the rectangle: "))
    width = float(input("Enter width of the rectangle: "))
    return Rectangle(color, is_filled, x_top_left, y_top_left, length, width)

if __name__ == "__main__":
    rectangle = create_rectangle_from_console()
    print(f"Rectangle Details: {rectangle}")
    print(f"Area of Rectangle: {rectangle.getArea()}")