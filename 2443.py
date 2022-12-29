N = int(input())

for i in range(N+1, 1, -1):
    star = 2 * i - 3
    blank = N + 1 - i
    print(" " * blank + '*' * star)