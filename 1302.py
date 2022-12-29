N = int(input())
best = {}

for _ in range(N):
    book = input()
    if book in best:
        best[book] += 1
    else:
        best[book] = 1

target = max(best.values())
arr =[]

for book, count in best.items():
    if count == target:
        arr.append(book)

print(sorted(arr)[0])