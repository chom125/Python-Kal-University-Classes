'''
Lawrence Woods
3/3/2018
4.	(The Rectangle class) Design a class named Rectangle to represent a rectangle. The class contains:
■ Two data fields named width and height.
■ A constructor that creates a rectangle with the specified width and height. The default values are 1 and 2
for the width and height, respectively.
■ A method named getArea() that returns the area of this rectangle.
■ A method named getPerimeter() that returns the perimeter.
Draw the UML diagram for the class, and then implement the class. Write a test program that creates two Rectangle
objects—one with width 4 and height 40 and the other with width 3.5 and height 35.7. Display the width, height, area,
and perimeter of each rectangle in this order.

'''
#Rectangle class

class Rectangle:

   #Default constructor.

   def __init__(self,w=1,h=2):

       self.width = w;

       self.height = h;

   #getArea method.

   def getArea(self):

       return self.width*self.height

   #getperimeter method.

   def getPerimeter(self):

       return 2*(self.width+self.height)

w = 4

print ("The width of the rectangle is "+str(w))

h = 40

print ("The width of the rectangle is "+str(h))

#Call the method by passing the width and height.

r = Rectangle(w,h);

#Print the area and perimeter.

print('The area of the rectangle is', r.getArea())

print('The perimeter of the rectangle is', r.getPerimeter())

w = 3.5

print("The width of the rectangle is "+str(w))

h = 35.7

print("The width of the rectangle is "+str(h))

#Call the method by passing the width and height.

r = Rectangle(w,h);

#Print the area and perimeter.

print("The area of the rectangle is", (r.getArea()))

print("The perimeter of the rectangle is", (r.getPerimeter()))