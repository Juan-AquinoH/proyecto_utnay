# area_functions.py
import math

def area_hexagon(side=8):
    if side == 8:
        print("Using default side length of 8")
    return (3 * math.sqrt(3) / 2) * side ** 2
