N = int(input())

for i in range(1, N + 1):
    blank = 2 * N - i * 2
    print("*" * i + " " * blank + "*" * i)
for i in range(N-1, 0, -1):
    blank = 2 * N - i * 2
    print("*" * i + " " * blank + "*" * i)
