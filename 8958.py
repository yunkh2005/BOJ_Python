N = int(input())
a = []

for i in range(1, N + 1):
    sum = cnt = 0
    a = list(map(str, input()))

    for j in range(len(a)):
        if (a[j-1] == "O") and (a[j] == "O"):
            cnt += 1
            sum += cnt
        elif (a[j-1] != "O") and (a[j] == "O"):
            cnt = 1
            sum += 1
    print(sum)