import math
def Fn(n):
    S=0
    T=0
    for i in range(1,n+1):
        T=T+i
        S+= math.sqrt(T)
    return S
n = int(input("N = "))
x = "{:.7f}".format(Fn(n))
print("F(%d) = " %n + x)
    