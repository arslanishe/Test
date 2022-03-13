import string


def Oportunity(a,b,c):
    return list(set(a)&set(b)&set(c))

print(Oportunity([1,2,3,5,4,10],[4,5,6,7],[8,4,9]))


def BigOportunity(a,b,c):
    y = 0
    for i in a:
        for x in b:
            if i == x:
                y = i
    for w in c:
        if y == w:
            return y

print(BigOportunity([1,2,3,4,10],[4,5,6,7],[8,4,9]))

def BiOportunity(a,b,c):
    return (a+b+c)
        

print(BiOportunity([1,2,3,4,10],[4,5,6,7],[4,8,9]))