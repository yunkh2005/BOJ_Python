now = list(map(int, input().split(':')))
target = list(map(int, input().split(':')))

now_time = now[0]*3600 + now[1]*60 + now[2]
target_time = target[0]*3600 + target[1]*60 + target[2]

result = target_time - now_time
if result < 0:
    result += 60 * 60 * 24
h = result // 3600
m = (result % 3600) // 60
s = result % 60
print("%02d:%02d:%02d" % (h,m,s))