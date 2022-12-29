n = int(input())
memo = {
    0: 0,
    1: 1,
    2: 1
}

def fibo(n):
    if n in memo:
        return memo[n]
    else:
        output = fibo(n - 1) + fibo(n - 2)
        memo[n] = output
        return output

print(fibo(n))