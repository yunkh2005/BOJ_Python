N = int(input())
A = list(map(int, input().split()))

def bubble(N, data):
    count = 0
    for i in range(N - 1):
        for j in range(1, N - i):
            check, swap = 0, 0
            if data[j-1] > data[j]:
                data[j-1], data[j] = data[j], data[j-1]
                check += 1
                count += 1
            else:
                continue

            if check == 0:
                break
        
    
    return count

print(bubble(N, A))