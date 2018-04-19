'''
Lawrence Woods
3/2/2018
Algebraic Equation

(Algebra: quadratic equations) Design a class named QuadraticEquation for a quadratic equation The class contains:

The private data fields a, b, and c that represent three coefficients.

A constructor for the arguments for a, b, and c.

Three get methods for a, b, and c.

A method named getDiscriminant() that returns the discriminant, which is b^2 - 4ac.

The methods named getRoot1()and getRoot2()for returning the two roots of the equation using these formulas:

2a b+V2-4ac and r2= 2a ri

These methods are useful only if the discriminant is nonnegative. Let these methods return 0 if the
discriminant is negative.

Draw the UML diagram for the class, and then implement the class. Write a test program that prompts the user
to enter values for a, b, and c and displays the result based on the discriminant. If the discriminant is positive,
display the two roots. If the discriminant is 0, display the one root. Otherwise, display “The equation has no roots.”
'''

import math
a = input("Enter a: ")
b = input("Enter b: ")
c = input("Enter c: ")
a = float(a)
b = float(b)
c = float(c)
def getRoot1():
root = 0
d = b*b - 4 *a*c
root = (-b + math.sqrt(d))/(2.0*a)
return root
def getRoot2():
root = 0
d = b*b - 4 *a*c
root = (-b - math.sqrt(d))/(2.0*a)
return root
d = b*b - 4 *a*c
if(d < 0):
print("the equation has no roots")
elif(d==0):
print("the equation has only one root: "+str(getRoot1()))
else:
print("first root: "+str(getRoot1()))
print("first root: "+str(getRoot2()))