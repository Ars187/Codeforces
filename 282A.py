#282A

n=int(input())
c=0
for i in range(n):
    s=input()
    l=s.split("X")
    for i in l:
        if i!='':
            if i=="++":
                c+=1
            elif i=="--":
                c-=1
print(c)
