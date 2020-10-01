#1064A

def sticklen(a,b,c):
    while a+b<=c:
        if a<b:
            a+=1
        else:
            b+=1
    while b+c<=a:
        if b<c:
            b+=1
        else:
            c+=1
    while a+c<=b:
        if a<c:
            a+=1
        else:
            c+=1
    return(a,b,c)
s=input()
l=s.split()
a=int(l[0])
b=int(l[1])
c=int(l[2])
x,y,z=sticklen(a,b,c)
print(abs(a-x)+abs(b-y)+abs(c-z))
