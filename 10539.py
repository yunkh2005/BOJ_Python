N = int(input())
B = list(map(int, input().split()))
A = [0 for _ in range(len(B))]

A[0] = B[0]

for i in range(1, N):
    A[i] = B[i] * (i + 1) - sum(A)

for i in A:
    print(i, end=' ')