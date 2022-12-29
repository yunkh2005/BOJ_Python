T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    dist = y - x
    cnt = 0
    move = 1
    move_sum = 0

    while move_sum < dist:
        cnt += 1
        move_sum += move
        if cnt % 2 == 0:
            move +=1

    print(cnt)

# https://ooyoung.tistory.com/91