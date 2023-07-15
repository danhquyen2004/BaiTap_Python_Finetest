def is_fibonacci(n):
    a = 0
    b = 1
    while b < n:
        a,b=b,a+b
    if b == n:
        return True
    return False
N = int(input("N = "))

if is_fibonacci(N) and N % 2 == 0:
    print("N la so fibonacci chan")
else:
    print("N khong phai la so fibonacci chan")
    
