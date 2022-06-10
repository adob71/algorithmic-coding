#  __5__
#  |   |
#  3   10
# | |  ||
#20 21 1
#|| || ||
#
#(5, (3, (20, None, None), (21, None, None)), (10, (1, None, None), None))
#
#class TreeExample(object):
#  x = 0
#  l = None
#  r = None
#
#driver code
#t=TreeExample()
#print(t.x,t.l,t.r)

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
