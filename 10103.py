n = int(input())
c = s = 100

for _ in range(n):
    C, S = map(int, input().split())

    if C > S:
        s -= C
    elif C < S:
        c -= S

print(c)
print(s)