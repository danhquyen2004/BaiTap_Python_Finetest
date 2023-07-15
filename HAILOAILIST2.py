a = []
b = []
n = int(input("Nhap N: "))
for i in range(1,n+1):
    s = input(f"Nhap gia tri thu {i}: ")
    if(s.startswith('-')):
        s2 = s.replace('-','')
        if(s2.isdigit()):
            a.append(int(s))
        elif(s2.replace('.','').isdigit()):
            a.append(float(s))
        else:
            b.append(s)
    else:
        if(s.isdigit()):
            a.append(int(s))
        elif(s.replace('.','').isdigit()):
            a.append(float(s))
        else:
            b.append(s)
if(a!=[]):
    tong=0
    for i in a:
        tong+=i
    print(f"TBC cua A = {tong/len(a)}")
print(f"B = {b}")
