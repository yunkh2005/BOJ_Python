A = input()
A = int(A, 8)
n = str(bin(A))

for i in range(2, len(n)):
    print(n[i], end='')
