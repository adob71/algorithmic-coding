filei = open("reverse-sentences.input","r")
fileo = open("reverse-sentences.output","w")
n=int(filei.readline())
for i in range(1,n+1):
  linei=filei.readline()
  linei = linei.rstrip()
  wordi=linei.split(" ")
#  print(wordi)
  l=len(wordi)
  wordo=[None] * l
  for w in range(0,l):
    wordo[l-1-w]=wordi[w] 
#  print(wordo)
  lineo=' '.join(wordo)+"\n" 
  fileo.write(lineo)
