def TestCode(a):
    q = 0
    for i in range(len(a) - 1):
        for x in range(len(a)-1 -i):
            print(f"сравниваем {a[x]} c {a[x+1]}")
            q += 1
            if a[x] > a[x + 1]:
                a[x],a[x+1] = a[x+1],a[x]
    return a, q

print(TestCode([1,4,2,10,3,6,8,4,9,5]))