import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([y, x])

arr = sorted(arr)

for y, x in arr:
    print(x, y)