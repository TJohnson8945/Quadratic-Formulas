"""
Author: Tyler Johnson

standard form of quadratic equation
f(x)=ax^2+bx+c

find the vertex
-b/2a

input a, b, and c
input x to get y
"""
#initialize variables
a = 0
b = 0
c = 0
xVertex = 0
vertex = 0

print("Let's find the vertex and min/max of a parabola")

#Input a, b, and c
a = float(input("What is the leading coefficient? (a) = "))
b = float(input("What is the second coefficient?  (b) = "))
c = float(input("What is the final digit?         (c) = "))

#find the x and y coordinate
xVertex = - (b) / 2 * (a)
vertex = (a) * xVertex ** 2 + (b) * (xVertex) + (c)
print("The vertex is " + "(" + str(xVertex) + ', ' + str(vertex) + ")")

#determine the min and max of the parabola
if (a) > 0:
    print("The minimum is " + str(vertex))
elif (a) < 0:
    print("The maximum is " + str(vertex))
