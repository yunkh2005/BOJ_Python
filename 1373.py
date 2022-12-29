A = input()
A = int(A, 2)
n = str(oct(A))

for i in range(2, len(n)):
    print(n[i], end='')