N = int(input())
weight = sorted(list(map(int, input().split())))
ans = 0

for i in weight:
    if i <= ans + 1:
        ans += i
    else:
        break
print(ans + 1)