#263A

for i in range(5):
    l=[int(x) for x in input().split()]
    for j in range(5):
        if l[j]==1:
            print(abs(2 - i) + abs(2 - j))
            break
