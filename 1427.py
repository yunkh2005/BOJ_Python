word = input()
arr = []

for i in word:
    arr.append(i)
arr = sorted(arr, reverse=True)

for i in arr:
    print(i, end='')