#1061A

s=input()
l=s.split()
n=int(l[0])
S=int(l[1])
c=S//n
x=c*n
if x<S:
    c+=1
print(c)
