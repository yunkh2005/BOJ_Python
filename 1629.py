A, B, C = map(int, input().split())

def DandC(A, B):
    if(B % 2 > 0):
        return DandC(A, B-1) * A
    elif(B == 0):
        return 1
    elif(B == 1):
        return A
    else:
        return DandC(A, B//2) ** 2 % C

print(DandC(A, B) % C)



