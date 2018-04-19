# -*- coding: utf-8 -*-
'''
Lawrence Woods
'''

'''    
(Find the number of years and days) Write a program that 
prompts the user to enter the minutes (e.g., 1 billion), 
and displays the number of years and days for the minutes. For simplicity, 
assume a year has 365 days. Here is a sample run:
Enter the number of minutes: 1000000000
1000000000 minutes is approximately 1902 years and 214 days 
''' 

def main():
    min = int(input('Enter the number of minutes: '))
    days = int(min / 1440)
    years = int(days / 365)
    days -= (365 * years)
    print(str(min) + ' minutes is approximately ' + str(years) + 'years and ' + str(days) + ' days')
   
    
    main()