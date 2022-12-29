T = int(input())
arr = []

for _ in range(T):
    N = int(input())
    for _ in range(N):
        S, L = map(str, input().split())
        L = int(L)
        arr.append((S, L))

    arr = sorted(arr, key = lambda x: x[1])
    print(arr[-1][0])

