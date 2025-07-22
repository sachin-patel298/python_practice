import math
def circle_stats(radius):
    area =  math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area,circumference
a , c = circle_stats(2)
print("Area : - ",round(a,2) , "circumference : - ",round(c,2))

#Assignment is How to Handle Precision using Rounding Method for only two values
