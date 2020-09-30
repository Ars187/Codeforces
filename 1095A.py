#1095A

l=int(input())
t=input()
s=""
n=0
for i in range(l//3+1):
    n+=i
    if n>=l:
        break
    s+=t[n]
print(s)
