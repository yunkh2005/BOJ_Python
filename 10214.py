T = int(input())

for _ in range(T):
    yonsei = korea = 0
    arr = []
    for _ in range(9):
        y, k = map(int, input().split())
        yonsei += y
        korea += k

    if yonsei > korea:
        print("Yonsei")
    elif yonsei < korea:
        print("Korea")
    else:
        print("Draw")



