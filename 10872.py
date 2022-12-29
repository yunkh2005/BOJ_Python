N = int(input())
f = 1

def factorial(N):
    if N == 0 or N == 1:
        return 1
    else:
        global f 
        f *= N
        if N == 2:
            return f
        else:
            return factorial(N-1)


print(factorial(N))