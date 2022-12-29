def is_prime(m, n):
    n += 1
    prime = [True] * n
    cnt = 0
    
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(2 * i, n, i):
                prime[j] = False
    
    for i in range(m, n):
        if i > 1 and prime[i] == True:
            cnt += 1
    
    return cnt

while True:
    n = int(input())
    if n == 0:
        break
    print(is_prime(n + 1, 2 * n))