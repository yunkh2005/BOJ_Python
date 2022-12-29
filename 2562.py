arr = []

#배열 입력 for문
for i in range(9):
    arr.append(int(input()))

print(max(arr))
print(arr.index(max(arr)) + 1)

