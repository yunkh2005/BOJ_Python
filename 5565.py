books = [0 for _ in range(9)]

result = int(input())

for i in range(9):
    books[i] = int(input())

print(result - sum(books))