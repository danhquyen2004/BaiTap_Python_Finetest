print("NHAP BANG GIA:")

ds = {}
while True:
	s = input("  Ten mat hang: ")
	if s == '':
		break
	n = input("  Gia ban hang: ")
	try:
		val = int(n)
		ds[s] = val
	except ValueError:
		val = float(n)
		ds[s] = val
dic = {}

print("NHAP HANG TON:")
while True:
	s = input("  Ten mat hang: ")
	if s == '':
		break
	n = int(input("  So luong ton kho: "))
	dic[s] = ds[s] * n 

for x in ds:
	try:
		ds[x] = dic[x]
	except KeyError:
		ds[x] = 0;

m = max(len(i) for i in ds)
# thong_ke = sorted(thong_ke.items(), key = lambda x:(x[1], x[0]))

print("THONG KE HANG TON:")

def sort_thong_ke(thong_ke):
    sorted_thong_ke = sorted(thong_ke.items(), key=lambda x:x[1], reverse=True)
    for i in range(len(sorted_thong_ke)):
        for j in range(i+1, len(sorted_thong_ke)):
            if sorted_thong_ke[i][1] == sorted_thong_ke[j][1] and sorted_thong_ke[i][0] > sorted_thong_ke[j][0]:
                sorted_thong_ke[i], sorted_thong_ke[j] = sorted_thong_ke[j], sorted_thong_ke[i]
    return sorted_thong_ke

thong_ke = sort_thong_ke(ds)

for key, value in thong_ke:
    a = '{:<2}'.format(' ') + key.ljust(m) + ' ' + '{:.2f}'.format(value).rjust(6)
    print(a)