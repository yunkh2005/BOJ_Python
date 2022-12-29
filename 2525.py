A, B = map(int, input().split())
C = int(input())
B += C

while True:
    if B >= 60:
        B -= 60
        A += 1

    if A >= 24:
            A -= 24
    
    if A < 24 and B < 60:
        break

print(A, B)