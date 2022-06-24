#usage
#python3 prime-numbers.py number
#example
#python3 prime-numbers.py 10
#2 3 5 7
#python3 prime-numbers.py 20
#2* 3* 5* 7* 11 13 17 19

#functions

import sys

def isPrime(n):
    if(n<2):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

def readArg():
    try:
        return int(sys.argv[1])
    except:
        return 0

def readMax():
    try:
        f=open("prime-numbers.ini","r")
        return int(f.read())
    except:
        return 0

def writeMax(n):
    try:
        f=open("prime-numbers.ini","w")
        f.write(str(n))
    except:
        return 0

#driver code

n=readArg()

m=readMax()

for i in range(1,n+1):
    if(isPrime(i)):
        print(i,end="")
        if(i<=m):
            print("*",end="")
        print(end=" ")
print()

if (n>m):
    writeMax(n)
