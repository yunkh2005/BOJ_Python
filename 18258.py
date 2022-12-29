import sys

N = int(sys.stdin.readline().rstrip())
queue = []
cnt = 0

for _ in range(N):
    S = sys.stdin.readline().rstrip().split()

    order = S[0]
    if order == "push":
        queue.append(S[1])
    elif order == "pop":
        if len(queue) > cnt:
            print(queue[cnt])
            cnt += 1
        else:
            print("-1")
    elif order == "size":
        print(len(queue)-cnt)
    elif order == "empty":
        if len(queue) == cnt :
            print("1")
            cnt = 0
            queue = []
        else: 
            print(0)
    elif order == "front":
        if len(queue) > cnt: 
            print(queue[cnt])
        else: 
            print(-1)
    elif order == "back":
        if len(queue) > cnt: 
            print(queue[-1])
        else: 
            print(-1)


# https://chancoding.tistory.com/35