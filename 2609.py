def gcd(A, B):
    return gcd(B, A % B) if B else A        #최대 공약수

def lcm(A, B):
    return A * B // gcd(A, B)               #최소 공배수

A, B = map(int, input().split())
print(gcd(A, B))
print(lcm(A, B))