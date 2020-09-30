#1030A

n=int(input())
s=input()
a=s.split()
for i in a:
    if i=="1":
        print("HARD")
        break   
else:
    print("EASY")
