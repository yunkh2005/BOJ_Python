N, K = map(int, input().split())
aliquot = []

for i in range(1, N+1):
    if N % i == 0:
        aliquot.append(i)

if len(aliquot) < K:
    print(0)
else:
    print(aliquot[K-1])