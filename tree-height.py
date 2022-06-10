#usage
#python3 tree-height.py
#output
#(5, (3, (20, None, None), (21, None, None)), (10, (1, None, None), None))
#2
#(5, (3, (20, None, None), (21, None, None)), (10, (1, (71, (77, (17, None, None), None), None), None), None))
#5

#functions

class Tree:

    def __init__(self, x, l, r):

        self.x = x
        self.l = l
        self.r = r

def treeHeight(t):

    lh=0
    if (t.l!=None):
        lh=1+treeHeight(t.l)

    rh=0
    if (t.r!=None):
        rh=1+treeHeight(t.r)

    return max(lh,rh)

def createTree(s):

    tup=tuple(s)

    x=tup[0]

    l=tup[1]
    if (l!=None):
        l=createTree(l)

    r=tup[2]
    if (r!=None):
        r=createTree(r)

    t=Tree(x,l,r)

    return t

#drive code

s=(5, (3, (20, None, None), (21, None, None)), (10, (1, None, None), None))
tup=tuple(s)
print(tup)
#print(tup[0])
#print(tup[1])
#print(tup[2])
t=createTree(s)
#print(t)
print(treeHeight(t))

s=(5, (3, (20, None, None), (21, None, None)), (10, (1, (71, (77, (17, None, None), None), None), None), None))
tup=tuple(s)
print(tup)
#print(tup[0])
#print(tup[1])
#print(tup[2])
t=createTree(s)
#print(t)
print(treeHeight(t))
