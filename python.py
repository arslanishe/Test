def TestCode(a):
    for i in range(len(a) - 1):
        for x in range(len(a)-1 -i):
            if a[x] > a[x + 1]:
                a[x],a[x+1] = a[x+1],a[x]
    return a

print(*TestCode([1,4,2,10,3,6,8,4,9,5]))