N = int(input())
A = list(map(int, input().split()))
DP = [A[0]]

for i in range(1, N):
    if A[i] > A[i - 1]:
        DP.append(A[i])

print(len(DP))
for i in DP:
    print(i, end=' ')