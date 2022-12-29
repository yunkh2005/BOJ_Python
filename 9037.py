T = int(input())

def check(N, C):
    for i in range(N):
        if C[i] % 2 == 1:
            C[i] += 1

    return len(set(C)) == 1

def teacher(N, C):
    tmp_lst = [0 for _ in range(N)]
    for idx in range(N):
        if C[idx] % 2:
            C[idx] += 1
        C[idx] //= 2
        tmp_lst[(idx + 1) % N] = C[idx]
        
    for idx in range(N):
        C[idx] += tmp_lst[idx]
    
    return C

def candy_war():
    N = int(input())
    C = list(map(int, input().split()))
    cnt = 0

    while not check(N, C):
        cnt += 1
        C = teacher(N, C)
    print(cnt)

for _ in range(T):
    candy_war()