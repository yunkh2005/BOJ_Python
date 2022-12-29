score = []

for i in range(5):
    j = int(input())
    if j < 40:
        score.append(40)
    else:
        score.append(j)
avg = sum(score) // 5
print(avg)
