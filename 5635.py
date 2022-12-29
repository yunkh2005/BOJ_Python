n = int(input())
birthDay = []

for _ in range(n):
    inform = list(map(str, input().split()))
    birthDay.append(inform)
    birthDay.sort(key=lambda x: (int(x[3]), int(x[2]), int(x[1])))
    
print(birthDay[-1][0])
print(birthDay[0][0])