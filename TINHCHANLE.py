def ChanLe(a,b,c):
    if a%2==0 and b%2==0 and c%2==0:
        return True
    if a%2!=0 and b%2!=0 and c%2!=0:
        return True
    else :
        return False


A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
if(ChanLe(A,B,C) == True):
    print("Cung tinh chan le")
else:
    print("Khac tinh chan le")
