n = int(input("N = "))
m = [1]
for i in range(n+100000):
    m.append(2*m[i]+1)
    m.append(3*m[i]+1)
print(n,"so dau tien cua N23:",*sorted(set(m))[:n])
