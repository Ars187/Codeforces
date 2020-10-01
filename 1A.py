#1A

s=input()
l=s.split()
n=int(l[0])
m=int(l[1])
a=int(l[2])
if m%a==0: 
    p=m//a 
else: 
    p=m//a+1 
 
if n%a==0: 
    q=n//a 
else: 
    q=n//a+1 
print(p*q) 
