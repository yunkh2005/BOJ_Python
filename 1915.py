n, m = map(int, input().split())
arr = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
DP = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(n):
    for idx, j in enumerate(list(map(int, list(input())))):
        arr[i+1][idx+1] = j

mx = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if arr[i][j]:
            DP[i][j] = min(DP[i-1][j], DP[i-1][j-1], DP[i][j-1]) + 1
            mx = max(DP[i][j], mx)

print(mx ** 2)
# DP[i][j]: i, j까지 왔을 때 가장 큰 정사각형 한 변의 길이
# DP[i][j] = min(DP[i-1][j], DP[i-1][j-1], DP[i][j-1]) + 1