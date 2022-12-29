import copy, heapq

K, N = map(int, input().split())
prime = list(map(int, input().split()))

lst, ck = copy.deepcopy(prime), set()
heapq.heapify(lst)
ith = 0

while ith < N:
    mn = heapq.heappop(lst)
    if mn in ck:
        continue
    ith += 1
    ck.add(mn)
    for i in prime:
        if mn * i < 2 ** 32:
            heapq.heappush(lst, mn * i)

print(mn)