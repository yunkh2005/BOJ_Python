N = int(input())
M = list(map(int, input().split()))
Max = max(M)
Sum = Avg = 0

#점수를 새로 계산하는 for문
for i in range(N):
    M[i] = M[i] / Max * 100
    Sum += M[i]

Avg = Sum / N
print(Avg)

