n = int(input("N = "))
mau = 0
fn = 0
for i in range(1,n+1):
    mau += i*i
    fn += n/mau
print(f"F({n}) = {fn:.7f}")