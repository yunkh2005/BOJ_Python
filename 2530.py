A, B, C = map(int, input().split())
D = int(input())
C += D

while True:
    if C >= 60:
        C -= 60
        B += 1

    if B >= 60:
        B -= 60
        A += 1

    if A >= 24:
            A -= 24
    
    
    if A < 24 and B < 60 and C < 60:
        break

print(A, B, C)