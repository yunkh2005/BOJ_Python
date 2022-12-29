N = int(input())
arr = []

def asc(arr):
    now = arr[0]
    result = 1

    for i in  range(1, len(arr)):
        if now < arr[i]:
            result += 1
            now = arr[i]
    return result

for _ in range(N):
    arr.append(int(input()))
print(asc(arr))
arr.reverse()
print(asc(arr))