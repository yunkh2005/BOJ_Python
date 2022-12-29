N = input()
F = int(input())
arr = int(N[:-2] + '00')

while arr % F != 0:
    arr += 1
print(str(arr)[-2:])