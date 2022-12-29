while True:
    arr = list(map(int, input().split()))
    
    if sum(arr) == 0:
        break

    mx = max(arr)   #최대값
    arr.remove(mx)
    mn = min(arr)   #최소값
    arr.remove(mn)

    if mn**2 + arr[0]**2 == mx**2:
        print("right")
    else:
        print("wrong")