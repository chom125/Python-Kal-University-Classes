'''
Lawrence Woods
3/1/2018
Class Stock

(The Stock class) Design a class named Stock to represent a company’s stock that contains:
A private string data field named symbol for the stock’s symbol.
A private string data field named name for the stock’s name.
A private float data field named previousClosingPrice that stores the stock price for the previous day.
A private float data field named currentPrice that stores the stock price for the current time.
A constructor that creates a stock with the specified symbol, name, previous price, and current price.
A get method for returning the stock name.
A get method for returning the stock symbol.
Get and set methods for getting/setting the stock’s previous price.
Get and set methods for getting/setting the stock’s current price.
A method named getChangePercent() that returns the percentage changed from previousClosingPrice to currentPrice.
Draw the UML diagram for the class, and then implement the class. Write a test program that creates a Stock object
with the stock symbol INTC, the name Intel Corporation, the previous closing price of 20.5, and the new current
price of 20.35, and display the price-change percentage.
'''


class Stock:

    #contructor
    def __init__(self, Name, Symbol, prev, curr):
        self.__symbol = Symbol
        self.__name = Name
        self.__prevClosingPrice = prev
        self.__currentPrice = curr

    #returns the name of the stock
    def getName(self):
        print(self.__name)

    #returns the symbol
    def getSymbol(self):
        print(self.__symbol)

    #returns the previous closing price
    def getPrev(self):
        print(self.__prevClosingPrice)

    #return the current price
    def getCurr(selfelf):
        print(self.__currentPrice)

    #updates the previous closing price
    def setPrev(self, val):
        self.__prevClosingPrice = val

    #updates the previous closing price
    def setPrev(self, val):
        self.__prevClosingPrice = val

    #updates the current price
    def setCurr(self, val):
        self.__currentPrice = Val

    #gets the percentage change in price
    def getPercentChange(self):
        ans = (self.__currentPrice - self.__prevClosingPrice) *100/self.__prevClosingPrice
        print("Percentage change is %.2f percent" % ans)

    #Test Funciton
def main():
    obj = Stock("Intel Corporation", "INTL", 20.5, 20.35)
    obj.getPercentChange()

main()
