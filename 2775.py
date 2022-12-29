T = int(input())

for _ in range(T):
    k = int(input())    #층
    n = int(input())    #호수

    num = [i for i in range(1, n+1)]
    print(num)
    for _ in range(k):
        for j in range(1,n):
            num[j] += num[j-1]
        print(num)
    print(num[-1])