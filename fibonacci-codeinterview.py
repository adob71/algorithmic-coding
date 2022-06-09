# This is Python 2
import sys

line = sys.stdin.readline()
#print line
line=line.rstrip()
arg=line.split(" ")
#print(arg)
e1=int(arg[0])
e2=int(arg[1])
n=int(arg[2])
#print(e1,e2,n)

for i in range(1,n-1):
  e3=e1+e2
  e1=e2
  e2=e3
  #print(e3,end=" ")

print(e3)
