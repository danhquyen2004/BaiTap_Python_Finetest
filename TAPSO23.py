def in_tap_hop_N23(N):
    # Khởi tạo tập N23 và danh sách kết quả
    tap_hop_N23 = {1}
    ket_qua = [1]

    while len(ket_qua) < N:
        i = 0
        while True:
            so_moi_1 = 2 * ket_qua[i] + 1
            so_moi_2 = 3 * ket_qua[i] + 1

            if so_moi_1 not in tap_hop_N23:
                tap_hop_N23.add(so_moi_1)
                ket_qua.append(so_moi_1)
                break
            elif so_moi_2 not in tap_hop_N23:
                tap_hop_N23.add(so_moi_2)
                ket_qua.append(so_moi_2)
                break
            i += 1

    return ket_qua[:N]

# Nhập số N từ người dùng
N = int(input("N = "))

# In ra N số đầu tiên của tập N23
ket_qua = in_tap_hop_N23(N)
print(f"{N} so dau tien cua N23:",end='')
ket_qua.sort()
for i in ket_qua:
    print(f" {i}",end='')


        