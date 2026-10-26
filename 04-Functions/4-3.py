###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math

a = int(input('podaj cyfre a'))
b = int(input('podaj cyfre b'))
c = int(input('podaj cyfre c'))

def triangle_area(a,b,c):
    s = (a+b+c)/2
    result = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return result

pole = triangle_area(a,b,c)

print(f'The area of ​​a triangle with sides {a},{b},{c} is {pole}')
