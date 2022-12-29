M = int(input())
N = int(input())
multiplication = [i ** 2 for i in range(1, 100 + 1)]
perfect_num = []


for i in range(M, N+1):
    if i in multiplication:
        perfect_num.append(i)

if len(perfect_num) != 0:
    print(sum(perfect_num))
    print(min(perfect_num))
else:
    print(-1)


