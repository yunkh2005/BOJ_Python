a, b = map(int, input().split())

#b의 값이 45보다 작을 때만
if(b < 45):
    b += 60
    a -= 1

#a의 값이 음수가 될 경우
if(a < 0):
    a += 24

print(a, b-45)