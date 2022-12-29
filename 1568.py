N = int(input())
K = 1
result = 0

while N != 0:
    if K > N:
        K = 1
    
    N -= K
    K += 1
    result += 1

print(result)