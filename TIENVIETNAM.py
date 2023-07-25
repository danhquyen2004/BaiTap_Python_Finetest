def count_coin_combinations(N, M, coins):
    if N == 0:
        return 1

    if M == 0 or N < 0:
        return 0

    total_combinations = 0
    for coin in coins:
        total_combinations += count_coin_combinations(N - coin, M - 1, coins)

    return total_combinations
coins = [5000, 2000, 1000, 500, 200]

n = int(input("N = "))
m = int(input("M = "))
result = count_coin_combinations(n, m, coins)
print("Số phương án đổi tiền:", result)
