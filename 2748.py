n = int(input())
memo = { 1: 1,
         2: 1}
count = 0

def fib(n):
    global count
    if n == 0:
        count += 1
        print("count1:", count)
        return 0
    elif n in memo:
        print("n2: ", n)
        count += 1
        print("count2:",count)
        return memo[n]
    else:
        print("n3: ", n)
        count += 1
        print("count3:",count)
        output = fib(n-1) + fib(n-2)
        print("output: ", output)
        memo[n] = output          
        return output

print(fib(n))