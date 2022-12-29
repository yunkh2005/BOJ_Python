n = int(input())

for _ in range(n):
    athlete = []
    p = int(input())
    for _ in range(p):
        inform = list(map(str, input().split()))
        athlete.append(inform)
    athlete.sort(key=lambda x : int(x[0]), reverse=True)

    print(athlete[0][1])