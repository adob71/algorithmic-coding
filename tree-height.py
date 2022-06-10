#  __5__
#  |   |
#  3   10
# | |  ||
#20 21 1
#|| || ||
#
#(5, (3, (20, None, None), (21, None, None)), (10, (1, None, None), None))

#functions

class Tree:

    def __init__(self, x, l, r):

        self.x = x
        self.l = l
        self.r = r

def TreeHeight(t):

    lh=0
    if (t.l!=None):
        lh=1+TreeHeight(t.l)

    rh=0
    if (t.r!=None):
        rh=1+TreeHeight(t.r)

    return max(lh,rh)

def CreateTree(s):
#(5, (3, (20, None, None), (21, None, None)), (10, (1, None, None), None))

    x=extractString(s,1)

    l=extractString(s,2)
    if (l!=None):
        l=CreateTree(l)

    r=extractString(s,3)
    if (r!=None):
        r=CreateTree(r)

    t=Tree(x,l,r)

    return t

def extractString(s,i):
#(5, (3, (20, None, None), (21, None, None)), (10, (1, None, None), None))

    if (i==1):
        return 0

    if (i==2):
        return None

    if (i==3):
        return None

#drive code

t1=Tree(0,None,None)
print(t1)
print(TreeHeight(t1))

t2=Tree(0,t1,None)
print(t2)
print(TreeHeight(t2))

t3=Tree(0,t2,None)
print(t3)
print(TreeHeight(t3))

t4=Tree(0,None,t3)
print(t4)
print(TreeHeight(t4))

s="(5, (3, (20, None, None), (21, None, None)), (10, (1, None, None), None))"
t=CreateTree(s)
print(t)
print(TreeHeight(t))
