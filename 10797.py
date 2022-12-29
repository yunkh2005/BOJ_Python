day = input()
carNums = list(map(int, input().split()))
violation = 0

for i in range(5):
    if carNums[i]  == int(day[-1]):
        violation += 1
print(violation)