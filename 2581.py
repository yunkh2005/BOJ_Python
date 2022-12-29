M = int(input())
N = int(input())
arr = list(range(M, N+1))
result = [1]

for i in range(len(arr)):
    for j in range(2, arr[i]):
        if arr[i] % j == 0:
            result.append(arr[i])
            break

result = list(set(arr) - set(result))
if len(result) == 0:
    print("-1")
else:
    print(sum(result))
    print(min(result))

#참고: https://calssess.tistory.com/91