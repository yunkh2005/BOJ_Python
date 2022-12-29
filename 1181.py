N = int(input())
arr = []

for i in range(N):
    a = input()
    arr.append(a)
arr = list(set(arr))
arr.sort(key = lambda x: (len(x), x))
print(type(arr))
for i in arr:
    print(i)