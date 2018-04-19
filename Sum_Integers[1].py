# -*- coding: utf-8 -*-
'''
Lawrence Woods
'''

'''
(Sum the digits in an integer) Write a program that reads an integer 
between 0 and 1000 and adds all the digits in the integer. For example, 
if an integer is 932, the sum of all its digits is 14. 
(Hint: Use the % operator to extract digits, and use the // operator 
to remove the extracted digit. For instance, 932 % 10 = 2 and 932 // 10 = 93.) 
Here is a sample run:
Enter a number between 0 and 1000: 999
The sum of the digits is 27
'''

n = eval (input ("Enter a number between 0 and 1000:"))

(quotient, remainder,) = divmod(n, 10)

sumOfDigits = remainder

while quotient:   # same as  while quotient != 0:
    (quotient, remainder,) = divmod(quotient, 10)
    sumOfDigits += remainder

print ("The sum of the digits is" ,sumOfDigits )