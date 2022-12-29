T = int(input())
dices = []

for i in range(T):
    dices.append(list(map(int, input().split())))
    print("Case {0}: {1}".format(i+1, sum(dices[i])))