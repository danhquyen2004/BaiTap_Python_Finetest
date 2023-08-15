def TongUoc(n):
    sum = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            sum += i
            if i != n // i:  
                sum += n // i
        i += 1
    return sum
n = int(input("N = "))
print("Tong cac uoc so cua %d" %n+" la %d" %TongUoc(n))

