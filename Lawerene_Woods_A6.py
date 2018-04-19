'''
Lawrence Woods
Assigement # 6 Working with Data Bases
3/19/2018
'''

def replaceText(filename, word):
    linetext = ""


inputFile = open(filename)
for line in inputFile:
    linetext += line.replace(word, "")
inputFile.close()
# print(linetext)
outfile = open(filename, "w+")
outfile.write(linetext)
outfile.flush()
outfile.close


# inputFile = open(filename, "w+")
# inputFile.write(linetext)
# inputFile.close()


def main():
    filename = input("Enter file name: ")


if os.path.exists(filename):
    word = input("Enter word to replace: ")
replaceText(filename, word)
else:
print("File doesn't exist")

main()  # to call main() method

2) count
all
occurences
of
words, characters and lines

import os.path


def countOccurences(filename):
    lines = 0


words = 0
chars = 0

with open(filename, 'r') as fileToRead:
    for line in fileToRead:
        wordsInLine = line.split()
lines += 1
words += len(wordsInLine)
chars += len(line)
print("%s characters" % (chars))
print("%s words" % (words))
print("%s lines" % (lines))


def main():
    filename = input("Enter file name: ")


if os.path.exists(filename):
    countOccurences(filename)
else:
    print("File doesn't exist")

main()

3) create
random
integers

import os.path
import random


def writeRandomNumbers(filename):
    numbers = ""


randNumber = []
sortedNumber = ""
with open(filename, 'w+') as fileToWrite:
    for num in range(1, 101):
        numbers = numbers + " " + str(random.randint(1, 100))
# print(numbers)
fileToWrite.write(numbers)
fileToWrite.flush()
fileToWrite.close()

with open(filename, "r") as fileToRead:
    for line in fileToRead:
# print(line.split(" "))
randNumber = [int(x) for x in line.split(" ") if len(x) > 0]
# print(randNumber)

with open(filename, 'w+') as fileToWrite:
    for elem in sorted(randNumber, key=int):
        sortedNumber = sortedNumber + " " + str(elem)
fileToWrite.write(sortedNumber)
fileToWrite.flush()
fileToWrite.close()


def main():
    filename = input("Enter file name: ")


if os.path.exists(filename):
    print("The file already exist")
else:
    writeRandomNumbers(filename)

main()