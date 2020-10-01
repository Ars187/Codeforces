#112A

a=input()
b=input()
p=a.lower()
q=b.lower()
x=0
for i in range(len(p)):
    if ord(p[i])>ord(q[i]):
        x=1
        break
    elif ord(p[i])<ord(q[i]):
        x=-1
        break
    else:
        continue
print(x)
