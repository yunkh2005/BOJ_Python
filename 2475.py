k = input()
sum = 0

for i in range(0, len(k), 2):
    sum += (int(k[i]) ** 2)
sum %= 10
print(sum)