T = int(input())
prime_num = [0 for _ in range(10001)]
prime_num[1] = 1

for i in range(2, 98):
    for j in range(i * 2, 10001, i):
        prime_num[j] = 1

for i in range(T):
    n = int(input())
    m = n // 2
    for j in range(m, 1, -1):
        if prime_num[n - j] == 0 and prime_num[j] == 0:
            print(j, n - j)
            break
