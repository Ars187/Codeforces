#71A

n=int(input())
l=[]
for i in range(n):
    s=input()
    l.append(s)
for i in range(n):
    n=l[i]
    s1=""
    if len(n)>10:
        s1+=n[0]+str(len(n)-2)+n[len(n)-1]
    else:
        print(n,end='')
    print(s1)
