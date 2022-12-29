T = int(input())
candys = []

for i in range(T):
    candys.append(list(map(int, input().split())))
    print("You get {0} piece(s) and your dad gets {1} piece(s).".format(candys[i][0] // candys[i][1], candys[i][0] % candys[i][1]))