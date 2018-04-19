

'''
Lawrence Woods
2/13/2018
Homework #3

1.	Write a function that accepts the name of a file and returns a tuple containing the number of
lines, words, and characters that are in the file. (Hint: Use the split function of the string module
to help you count the words in the file.)  '
'''
def getPentagonalNumber(n):
   return n*(3*n-1)/2;
for x in range(1,101):
    if (x)%10==0:
        print('%6d' % (getPentagonalNumber(x)))
    else:
        print('%6d' % (getPentagonalNumber(x)),end=' ')

##################################################################################################################

'''
2.	(Palindrome integer) Write the functions with the following headers:
# Return the reversal of an integer, e.g. reverse(456) returns # 654 
def reverse(number):

# Return true if number is a palindrome 
def isPalindrome(number):

Use the reverse function to implement isPalindrome. A number is a palindrome if its 
reversal is the same as itself. Write a test program that prompts the user to enter an integer and 
reports whether the integer is a palindrome. 
'''


def reverse(number):
   temp = number
   ans = 0
   while temp>0:
       ans = ans*10 + temp%10
       temp = temp/10
   return ans

def isPalindrome(number):
   if number == reverse(number):
       return True
   else:
       return False
n = int(raw_input("Please enter a number:"))
if isPalindrome(n):
   print("The number is a palindrome.")
else:
   print("The number is not a palindrome.")

###################################################################################################################
'''
3.	(Math: approximate the square root) There are several techniques for implementing the sqrt function in 
the math module. One such technique is known as the Babylonian function. It approximates the square root of a 
number, n, by repeatedly performing a calculation using the following formula:
nextGuess = (lastGuess + (n / lastGuess)) / 2	
When nextGuess and lastGuess are almost identical, nextGuess is the approximated square root. The initial guess 
can be any positive value (e.g., 1). This value will be the starting value for lastGuess. If the difference between 
nextGuess and lastGuess is less than a very small number, such as 0.0001, you can claim that nextGuess is the 
approximated square root of n. If not, nextGuess becomes lastGuess and the approximation process continues. 
Implement the following function that returns the square root of n.
def sqrt(n):
'''


def sqrt(n):
    n = n*1.0
    lastGuess = 1.0

    while True:
        nextGuess = (lastGuess + (n/lastGuess))/2.0
        if abs(nextGuess-lastGuess)<=0.0001:
            break
        else:
            lastGuess = nextGuess
    return nextGuess

print("Square of 2 is : " + str(sqrt(2)))
print("Square of 25 is : " + str(sqrt(25)))
print("Square of 36 is : " + str(sqrt(36)))

##################################################################################################################
'''

4.	(Turtle: two chessboards) Write a program that displays two chessboards, 
as shown in Figure. Your program should define at least the following function:
# Draw one chessboard whose upper-left corner is at # (startx, starty) and bottom-right 
corner is at (endx, endy) 
def drawChessboard(startx, endx, starty, endy):
'''


import turtle

# Draw chess board borders
turtle.pensize(3) # Set pen thickness to 3 pixels
turtle.penup() # Pull the pen up
turtle.goto(-120, -120)
turtle.pendown() # Pull the pen down
turtle.color("red")

for i in range(4):
    turtle.forward(240) # Draw a line
    turtle.left(90) # Turn left 90 degrees

# Draw chess board inside

turtle.color("black")
for j in range(-120, 90, 60):
    for i in range(-120, 120, 60):
        turtle.penup()
        turtle.goto(i, j)
        turtle.pendown()

       # Draw a small rectangle
        turtle.begin_fill()
        for k in range(4):
            turtle.forward(30) # Draw a line
            turtle.left(90) # Turn left 90 degrees
        turtle.end_fill()

for j in range(-90, 120, 60):
    for i in range(-90, 120, 60):
        turtle.penup()
        turtle.goto(i, j)
        turtle.pendown()

       # Draw a small rectangle
        turtle.begin_fill()
        for k in range(4):
            turtle.forward(30) # Draw a line
            turtle.left(90) # Turn left 90 degrees
        turtle.end_fill()

turtle.hideturtle()

turtle.done()

####################################################################################################################
'''
5. (Financial: credit card number validation) Credit card numbers follow certain patterns: It must have between 
13 and 16 digits, and the number must start with: 
■ 4 for Visa cards 
■ 5 for MasterCard credit cards 
■ 37 for American Express cards 
■ 6 for Discover cards 

In 1954, Hans Luhn of IBM proposed an algorithm for validating credit card numbers. The algorithm is useful to 
determine whether a card number is entered correctly or whether a credit card is scanned correctly by a scanner. 
Credit card numbers are generated following this validity check, commonly known as the Luhn check or the Mod 10 check, 
which can be described as follows (for illustration, consider the card number 4388576018402626): 

a.	Double every second digit from right to left. If doubling of a digit results in a two-digit number, add up the 
two digits to get a single-digit number.

b.	Now add all single-digit numbers from Step 1.

4 + 4 + 8 + 2 + 3 + 1 + 7 + 8 = 37

c.	Add all digits in the odd places from right to left in the card number.

6 + 6 + 0 + 8 + 0 + 7 + 8 + 3 = 38

d.	Sum the results from Steps 2 and 3.
37 + 38 = 75

e.	If the result from Step 4 is divisible by 10, the card number is valid; otherwise, it is invalid. 
For example, the number 4388576018402626 is invalid, but the number 4388576018410707 is valid. 
Write a program that prompts the user to enter a credit card number as an  integer. Display whether the number 
is valid or invalid. Design your program to use the following functions:
# Return true if the card number is valid 
def isValid(number):
# Get the result from Step 2 
def sumOfDoubleEvenPlace(number):
# Return this number if it is a single digit, otherwise, return # the sum of the two digits 
def getDigit(number):
# Return sum of odd place digits in number 
def sumOfOddPlace(number):
'''


# Return true if the card number is valid
def isValid(number):
    valid = False
    if prefixMatched(4, getPrefix(number, 1)):  # visa check
        valid |= True  # actually its an OR operator used as statement. so True | False => True, boolean OR
        # logic similar to you might have read V(v symbol) in discrete mathematics or related field.
    if prefixMatched(5, getPrefix(number, 1)):  # master check
        valid |= True
    if prefixMatched(6, getPrefix(number, 1)):  # discovery check
        valid |= True
    if prefixMatched(37, getPrefix(number, 2)):  # american express check
        valid |= True

    if getSize(number) < 13 or getSize(number) > 16:
        valid &= False

    result = sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)
    if result % 10 != 0:
        valid &= False

    return valid


# Get the result from Step 2
def sumOfDoubleEvenPlace(number):
    summation = 0
    even = 0
    while number > 0:
        if even == 1:
            summation += getDigit(number % 10)
        even ^= 1  # it's a xor operaotr so basically 1 will become 0 and 0 will become 1 what I actually doing
        # here is making an alternate turn so suppose number is 1213 then so i am traversing from right
        # side (digit 3) its odd place and even = 0, then even = 1 and we are 1 then even = 0 and we are at 2 then
        # even = 1 we are at 1. Now over. So when even = 1 then it is at even place.
        number //= 10
    return summation


# Return this number if it is a single digit, otherwise, return
# the sum of the two digits
def getDigit(number):
    number *= 2
    return (number % 10) + (
    number // 10);  # suppose number = 8, then number *= 2 will make number = 16, so number % 10 will give 6 and
    # number // 10 will give 1 and we have to return the sum of digits so 1 + 6 = 7. Now suppose number = 3,
    # so number *= 2 will make number = 6, so number % 10 will give 6 and number // 10 will give 0 = 0 + 6 = 6, //
    # it is integer division in python.


# Return sum of odd place digits in number
def sumOfOddPlace(number):
    summation = 0
    odd = 1
    while number > 0:
        if odd == 1:
            summation += number % 10
        odd ^= 1
        number //= 10
    return summation


# Return true if the digit d is a prefix for number
def prefixMatched(number, d):
    return True if str(number).startswith(d) else False


# Return the number of digits in d
def getSize(d):
    return len(str(d))


# Return the first k number of digits from number. If the
# number of digits in number is less than k, return number.
def getPrefix(number, k):
    return str(number) if getSize(number) <= k else str(number)[0:k]
#ternary operator so if condition is true then str(number) will execute else str(number)[0:k] will execute.
# str(number) just typecasting number to string. getSize(number) returns the no of digits in number. so
# if its <= k return the number otherwise return its prefix so for example number= 12345, and k = 2 it will return
# 12, but if k = 5 or more it will return 12345 as string. so "12345"


print("Enter the credit card number")
number = int(input())

print("valid" if isValid(number) else "invalid")








