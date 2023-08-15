N=int(input("Nhap N duong: "))
s=1
m=0
for i in range(1,N+1):
    s=s*i
    m+=s
print(f"F({N}) = {m}")