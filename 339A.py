#339A

s=input()
l=s.split("+")
l.sort()
t=""
for i in range(len(l)):
    t+=l[i]
    if i!=len(l)-1:
        t+="+"
print(t)
