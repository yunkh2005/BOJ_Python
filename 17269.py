N, M = map(int, input().split())
A, B = map(str, input().split())
num = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
AB = ''
min_len = min(N, M)

for i in range(min_len):
    AB += A[i] + B[i]
AB += A[min_len:] + B[min_len:]

C = [num[ord(i) - ord('A')] for i in AB]

for i in range(N + M - 2):
    for j in range(N + M - 1 - i):
        C[j] += C[j + 1]
        C[j] %= 10

if C[0] == 0:
    print(C[1] , "%", sep='')
else:
    print(C[0], C[1], "%", sep='')