N = int(input())
prize = 0

for _ in range(N):
    A, B, C = map(int, input().split())

    if A == B == C:
        prize = max(prize, 10000 + A * 1000)
    elif A == B:
        prize = max(prize, 1000 + A * 100)
    elif A == C:
        prize = max(prize, 1000 + A * 100)
    elif B == C:
        prize = max(prize, 1000 + B * 100)
    else:
        prize = max(prize, 100 * max(A, B, C))

print(prize)
