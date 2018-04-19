'''
Lawrence Woods
Assignment #7
3/27/2018
'''

#problem1.py

fname = input("Enter a file name:")
word = input("Enter the string to be removed:")
lt = []
f= open(fname,'r')
for l in f.readlines():
l = l.replace(word,"")
lt.append(l)
f.close()
f= open(fname,'w')
for l in lt:
f.write(l)
f.close()

#problem2.py

filename = input("Enter file name: ");

totalChars = totalWords = totalLines = 0

with open(filename, 'r') as inputFile:

for line in inputFile:

totalLines += 1

totalWords += len(line.split())

totalChars += len(line)

print(totalChars, "characters")

print(totalWords, "words")

print(totalLines, "lines")

#problem3.py

import random

from pathlib import Path

#main function

def main():

filename=input("Enter filename: ")

my_file = Path(filename)

check=True

while check:

if my_file.is_file():

print("file already exists")

check=True

filename=input("Enter filename: ")

my_file = Path(filename)

else:

outfile=open(filename,'w')

#loop to genertate random numbers and write it in file

count=100

while count!=0:

num=random.randint(1,100)

#write random generated number into text file

outfile.write(str(num)+"\n")

count= count - 1

check=False

outfile.close()

infile=open(filename,'r')

inf=infile.read().split("\n")

inf=list(map(str.strip,inf))

inf = list(filter(None, inf))

inf = [x.strip('') for x in inf]

inf = list(map(int, inf))

inf.sort()

print("After Sorting")

print(inf)

main()

#problem4.py

import math
import random
rank=["assistant" , "associate", "full"]
with open("Salary.txt","w") as f:
s=0
i=0
while i<1000:
first="Firstname"+str(i)
last="LastName"+str(i)
r= ((int)(random.random()*3))%3;
if r==0:
s = 50000.0 + (random.random() * (80000-50000))
elif r==1:
s = 60000.0 + (random.random() * (100000-60000))
elif r==2:
s = 75000.0 + (random.random() * (130000-75000))
f.write(first+" "+last+" "+rank[r]+" "+str(round(s,2))+"\n")
i=i+1
f.close()

