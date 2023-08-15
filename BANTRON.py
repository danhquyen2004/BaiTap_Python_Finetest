
n = int(input("So nguoi ngoi quanh ban: "))
a = 0
for i in range(1,n+1):
    a = (a+2)%i+1
print("Nguoi o lai cuoi cung la nguoi thu",a)