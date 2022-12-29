import sys

n = int(sys.stdin.readline())
num = list(int(input()) for _ in range(n))
stack_num = [i for i in range(n)]

print(num)
