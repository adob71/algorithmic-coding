import sys

linei = sys.stdin.readline()
n=int(linei)

for i in range(1,n+1):
    linei=sys.stdin.readline()
    linei=linei.rstrip()
    wordi=linei.split(" ")
    l=len(wordi)
    wordo=[None] * l
    for w in range(0,l):
        wordo[l-1-w]=wordi[w]
    lineo=' '.join(wordo)+"\n"
    sys.stdout.writelines(lineo)
