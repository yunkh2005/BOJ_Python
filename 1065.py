N = int(input())
hansu = 0

for i in range(1, N+1):
    if i < 100:
        hansu += 1
    elif int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]):
        hansu += 1

print(hansu)