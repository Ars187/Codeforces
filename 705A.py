#705A

n=int(input())
a="I hate"
b="I love"
l=[]
for i in range(n):
    if i%2==0:
        l.append(a)
        if i==n-1:
            l.append(" it")
        else:
            l.append(" that ")
    else:
        l.append(b)
        if i==n-1:
            l.append(" it")
        else:
            l.append(" that ")
for i in l:
    print(i,end="")
