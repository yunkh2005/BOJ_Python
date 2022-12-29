N = int(input())

def money():
    lst = sorted(list(map(int, input().split())))
    if len(set(lst)) == 1:
        return 50000 + lst[0] * 5000
    elif len(set(lst)) == 2:
        if lst[1] == lst[2]:
            return 10000 + lst[1] * 1000
        else:
            return 2000 + (lst[1] + lst[2]) * 500
    
    for i in range(3):
        if lst[i] == lst[i + 1]:
            return 1000 + lst[i] * 100
    
    return lst[-1] * 100


print(max(money() for i in range(N)))