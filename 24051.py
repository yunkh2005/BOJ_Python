def insert(N, K, data):
    answer = 0
    count = 0
    for i in range(N - 1):
        for j in range(i+1, 0,-1):
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]
                count += 1
            else:
                break

            if count == K:
                return


N, K = map(int, input().split())
data = list(map(int, input().split()))

print(insert(N, K, data))