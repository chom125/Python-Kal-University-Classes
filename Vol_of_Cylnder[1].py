# -*- coding: utf-8 -*-


'''
(Compute the volume of a cylinder) Write a program that 
reads in the radius and length of a cylinder and computes the 
area and volume using the following formulas:
area = radius * radius * π volume = area * length
Here is a sample run:
Enter the radius and length of a cylinder: 5.5, 12
The area is 95.0331 The volume is 1140.4
'''

print("This program prints the volume of a cylinder: ")

radius = float(input("Enter the radius of the cylinder: "))

length = float(input("Enter the length of the cylinder "))

area = 2*radius * radius * length*(2*3.14*radius)

volume = 3.14* radius * radius * length

print("Here is a sample run of the program\n")

print("The conversion to of the radius and legnth to volume is: ", volume)
