def gcd(A, B):
    return gcd(B, A % B) if B else A        #최대 공약수

def lcm(A, B):
    return A * B // gcd(A, B)               #최소 공배수

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(lcm(A, B))
    
    