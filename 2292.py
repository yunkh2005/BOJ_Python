N = int(input())
room, result = 1, 1

while N > room:
    room += (6 * result)
    result += 1

print(result)