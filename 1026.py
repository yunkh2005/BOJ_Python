N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sum = 0

A = sorted(A, reverse=True)
B = sorted(B)

for i in range(N):
    sum += A[i] * B[i]

print(sum)