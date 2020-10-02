#82A

a=['Sheldon','Leonard','Penny','Rajesh','Howard']
n=int(input())
i=1
while n>=i*5:
    n-=i*5
    i*=2
n=n-1
n=n//i
print(a[n])
