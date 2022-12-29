T = int(input())

for _ in range(T):
    arr = list(map(str, input().split()))
    answer = float(arr[0])

    for i in range(1, len(arr)):
        if arr[i] == "#":
            answer -= 7
        elif arr[i] == "%":
             answer += 5
        elif arr[i] == "@":
            answer *= 3
                
    print("%0.2f" % answer)