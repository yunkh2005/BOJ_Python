K, N, M = map(int, input().split())
dongsu = K * N - M
if dongsu <= 0:
    print(0)
else:
    print(dongsu)