N = int(input())
S = list(input())
score, bonus, result = 0, 0, 0

if S[0] == 'O':
    score += 1

for i in range(1, N):
    if S[i] == 'O':
        score += (i + 1)
        if S[i - 1] == 'O':
            bonus += 1        
        result += bonus
    else:
        bonus = 0

print(result + score)