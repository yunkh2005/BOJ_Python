N, A, B = map(int, input().split())
meet = 0

while A != B:
    A -= A//2
    B -= B//2
    meet += 1
print(meet)