A, B, C = map(int, input().split())
arr = []
arr.append(A)
arr.append(B)
arr.append(C)

arr.remove(max(arr))
print(max(arr))