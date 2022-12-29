T = int(input())

for _ in range(T):
    s = int(input())
    n = int(input())
    car = []

    for _ in range(n):
        qp = list(map(int, input().split()))
        car.append(qp)
    
    for i in range(n):
        s += car[i][0] * car[i][1]
    
    print(s)