T = int(input())

for i in range(T):
    R = list(map(str, input()))
    for j in range(len(R)-2):
        print(R[j+2] * int(R[0]), end='')
    
    print()


