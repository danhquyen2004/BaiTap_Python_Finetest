a = []
b = []
c = []
n = int(input("Nhap N: "))
for i in range(1,n+1):
    s = input(f"Nhap gia tri thu {i}: ")
    if(s.startswith('-')):
        s2 = s.replace('-','')
        if(s2.isdigit()):
            a.append(int(s))
        elif(s2.replace('.','').isdigit()):
            b.append(float(s))
        else:
            c.append(s)
    else:
        if(s.isdigit()):
            a.append(int(s))
        elif(s.replace('.','').isdigit()):
            b.append(float(s))
        else:
            c.append(s)
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
print(f"A = {a}")
print(f"B = {b}")
print(f"C = {c}")
