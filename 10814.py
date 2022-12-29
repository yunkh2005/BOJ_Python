N = int(input())
member = []

for _ in range(N):
    member.append(list(map(str, input().split())))

member.sort(key=lambda x: int(x[0]))

for age, name in member:
    print(age, name)