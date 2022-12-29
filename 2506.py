import sys
N = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))
count = 1
score = 0

for i in range(len(check)):
    if check[i] == 1:
        if count == 1:
            score += count
        else:
            score += count

        count += 1
    else:
        count = 1

print(score)
