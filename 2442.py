N = int(input())

for i in range(1, N+1):
    star = 2 * i - 1
    blank = N - i
    print(" " * blank + '*' * star)