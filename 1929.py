import sys
input = sys.stdin.readline

M, N = map(int, input().split())

def is_prime(M, N):
    N += 1
    prime_number = [True] * N

    for i in range(2, int(N ** 0.5) + 1): 
       if prime_number[i]:                    
           for j in range(2 * i, N, i):    
               prime_number[j] = False
    
    for i in range(M, N):
        if i > 1 and prime_number[i] == True:
            print(i)

is_prime(M, N)