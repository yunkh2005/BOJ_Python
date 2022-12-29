jury = int(input())
vote = input()
score_A = score_B = 0

for i in vote:
    if i == "A":
        score_A += 1
    else:
        score_B += 1

if score_A > score_B:
    print("A")
elif score_B > score_A:
    print("B")
else:
    print("Tie")