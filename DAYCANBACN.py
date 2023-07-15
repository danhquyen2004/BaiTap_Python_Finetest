import math
fn=0
t=0
n = int(input("N = "))
for i in range(1,n+1):
    t+=i
    fn+= t**(1/i)
print(f"F({n}) = {fn:.7f}")