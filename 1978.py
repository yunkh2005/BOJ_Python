N = int(input())
arr = list(map(int, input().split()))

for i in range(N):
    if arr[i] == 1:
            N -= 1
            continue

    for j in range(2, arr[i]):
        if arr[i] % j == 0:
            N -= 1
            break

print(N)