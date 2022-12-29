N = int(input())
A = list(map(int, input().split()))
B = A.copy()
A.sort()
C = []

for i in range(N):
    C.append(A.index(B[i]))

for i in range(N):
    print(C[i], end=' ')
