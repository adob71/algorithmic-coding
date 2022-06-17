#usage
#python3 binary-tree-height.py
#output
#python3 binary-tree-height.py
#(1, None, None)
#0
#(5, (3, (20, None, None), (21, None, None)), (10, (1, None, None), None))
#2
#(5, (3, (20, None, None), (21, None, None)), (10, (1, (71, (77, (17, None, None), None), None), None), None))
#5

#functions

class binaryTree:

    def __init__(self, x, l, r):

        self.x = x
        self.l = l
        self.r = r

def binaryTreeHeight(t):

    lh=0
    if (t.l!=None):
        lh=1+binaryTreeHeight(t.l)

    rh=0
    if (t.r!=None):
        rh=1+binaryTreeHeight(t.r)

    return max(lh,rh)

def createBinaryTree(s):

    tup=tuple(s)

    x=tup[0]

    l=tup[1]
    if (l!=None):
        l=createBinaryTree(l)

    r=tup[2]
    if (r!=None):
        r=createBinaryTree(r)

    t=binaryTree(x,l,r)

    #print(tup)

    return t

#driver code

s=(1, None, None)
tup=tuple(s)
print(tup)
#print(tup[0])
#print(tup[1])
#print(tup[2])
t=createBinaryTree(s)
#print(t)
print(binaryTreeHeight(t))

s=(5, (3, (20, None, None), (21, None, None)), (10, (1, None, None), None))
tup=tuple(s)
print(tup)
#print(tup[0])
#print(tup[1])
#print(tup[2])
t=createBinaryTree(s)
#print(t)
print(binaryTreeHeight(t))

s=(5, (3, (20, None, None), (21, None, None)), (10, (1, (71, (77, (17, None, None), None), None), None), None))
tup=tuple(s)
print(tup)
#print(tup[0])
#print(tup[1])
#print(tup[2])
t=createBinaryTree(s)
#print(t)
print(binaryTreeHeight(t))
