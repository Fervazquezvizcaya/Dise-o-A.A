def Rec(n):
    if n<2:
        return n
    else:
        return Rec(n-1)+ Rec(n-2)

print(Rec(8))
