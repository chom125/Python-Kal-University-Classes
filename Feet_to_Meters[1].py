# -*- coding: utf-8 -*-
'''
Lawrence Woods
'''

'''
(Convert feet into meters) Write a program that reads 
a number in feet, converts it to meters, and displays the result. 
One foot is 0.305 meters. Here is a sample run:
Enter a value for feet: 16.5
16.5 feet is 5.0325 meters 
'''

print("This program converts feet to meters: ")

feet = float(input("Enter the number of feet: "))

meters = feet * 0.305

print("The number of meters is: ", meters)
