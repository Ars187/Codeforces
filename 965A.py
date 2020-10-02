#965A

import math
s=input()
l=s.split()
k=int(l[0])
n=int(l[1])
s=int(l[2])
p=int(l[3])
ans=math.ceil((math.ceil(n/s)*k)/p)
print(ans)
