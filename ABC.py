arr = []
a = int(input("A = "))
arr.append(a)
b = int(input("B = "))
if(b!=a):
    arr.append(b)
c = int(input("C = "))
if(c!=a and c!=b):
    arr.append(c)
arr.sort(reverse=False)
s="Xep tang dan:"
for i in arr:
    s += f" {i}"
print(s)
