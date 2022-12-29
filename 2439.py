N = int(input())

for i in range(N + 1, 1, -1):
    print(str(" " * (i-2)) + str( "*" * (N+2-i)))