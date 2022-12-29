N = temp = int(input())
count = 0

while 1:
    first = N % 10
    second = N // 10
    total = first + second
    count += 1
    N = int(str(first) + str(total % 10))
    if(temp == N):
        break
print(count)