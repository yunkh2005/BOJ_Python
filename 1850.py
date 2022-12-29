def gcd(A, B):
    return gcd(B, A % B) if B else A        #최대 공약수

A, B = map(int, input().split())
A = int("1" * A)
B = int("1" * B)

print(gcd(A, B))