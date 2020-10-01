#1102A

n=int(input())
l=[]
if n%2==0:
    l=[n-1,n]
    if n>2:
        if l[1]%4==0:
            print(0)
        else:
            print(1)
    else:
        print(1)
else:
    l=[n,n+1]
    if l[1]%4==0:
        print(0)
    else:
        print(1)
    
