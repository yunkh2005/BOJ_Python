T = int(input())

for _ in range(T):
    N = int(input())
    score =[]
    for _ in range(N):
        score.append(list(map(float, input().split())))

    grade, total = [], []
    for i in range(N):
        grade.append(int(score[i][0]))
        total.append(score[i][1])
    
    for i in range(N):
        total[i] *= grade[i]

    print(sum(grade), round(sum(total)/sum(grade), 1))
    