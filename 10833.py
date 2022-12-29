N = int(input())
apples, result = [], []

for _ in range(N):
    apples.append(list(map(int, input().split())))

for i in range(N):
    result.append(apples[i][1] % apples[i][0])

print(sum(result))