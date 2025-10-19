#Create functions to calculate the area of a circle, square, triangle, and 
#hexagon. Each function must have default parameter values, so that if the user 
#omits any argument, the program uses the default ones. 
#Additionally, the program should display a message indicating that the default 
#arguments were used. 

import math

def area_circle(radius=4):
    if radius == 4:
        print("Using default radius of 4")
    return math.pi * radius ** 2
def area_square(side=7):
    if side == 7:
        print("Using default side length of 7")
    return side ** 2
def area_triangle(base=4, height=13):
    if base == 4 and height == 13:
        print("Using default base of 4 and height of 13")
    return 0.5 * base * height
def area_hexagon(side=8):
    if side == 8:
        print("Using default side length of 8")
    return (3 * math.sqrt(3) / 2) * side ** 2
# Example usage:
print("Area of Circle:", area_circle())
print("Area of Square:", area_square())
print("Area of Triangle:", area_triangle())
print("Area of Hexagon:", area_hexagon())
print("Area of Circle with radius 5:", area_circle(5))
print("Area of Square with side 10:", area_square(10))
print("Area of Triangle with base 6 and height 9:", area_triangle(6, 9))
print("Area of Hexagon with side 12:", area_hexagon(12))


#Using default side length of 7
#Area of Square: 49
#Using default base of 4 and height of 13
#Area of Triangle: 26.0
#Using default side length of 8
#Area of Hexagon: 166.27687752661222
#Area of Circle with radius 5: 78.53981633974483
#Area of Square with side 10: 100
#Area of Triangle with base 6 and height 9: 27.0
#Area of Hexagon with side 12: 374.1229744348775