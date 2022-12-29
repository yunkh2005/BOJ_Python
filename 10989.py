import sys

N = int(sys.stdin.readline())
arr = [0] * N
s = ''

for i in range(N):
    arr[i] = int(sys.stdin.readline())

arr.sort()

for i in arr:
    s += (str(i) + '\n')
print(s)