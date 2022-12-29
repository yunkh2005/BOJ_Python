N = int(input())

for i in range(N+1, 1, -1):
    star = 2 * i - 3
    blank = N + 1 - i
    print(" " * blank + '*' * star)
for i in range(2, N+1):
    star = 2 * i - 1
    blank = N - i
    print(" " * blank + '*' * star)