N, M = map(int, input().split())
castle = []
row = [0] * N
col = [0] * M
row_count = 0
col_count = 0

for _ in range(N):
    castle.append(input())

for i in range(N):
    for j in range(M):
        if castle[i][j] == 'X':
            row[i] = 1
            col[j] = 1

for i in range(N):
    if row[i] == 0:
        row_count += 1

for j in range(M):
    if col[j] == 0:
        col_count += 1

print(max(row_count, col_count))