# -*- coding: utf-8 -*-
'''
Lawrence Woods
'''

'''    
(Science: calculate energy) Write a program that calculates the energy 
needed to heat water from an initial temperature to a final temperature. 
Your program should prompt the user to enter the amount of water in kilograms 
and the initial and final temperatures of the water. The formula to compute 
the energy is Q = M * (finalTemperature – initialTemperature) * 4184
where M is the weight of water in kilograms, temperatures are in degrees 
Celsius, and energy Q is measured in joules. Here is a sample run:
Enter the amount of water in kilograms: 55.5 Enter the initial 
temperature: 3.5 Enter the final temperature: 10.5 The energy needed 
is 1625484.0 
''' 

M = float(input("Enter the amount of water in kilograms: "))

initialTemparature = float(input("Enter the initial temparature: "))

finalTemparature = float(input("Enter the final temparature: "))

Q = M * (finalTemparature-initialTemparature) * 4184

print("The energy needed is",Q)