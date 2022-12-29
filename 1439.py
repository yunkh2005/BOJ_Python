S = input()
switch = 0
for i in range(1, len(S)):
    if S[i] != S[i-1]:
        switch += 1

print((switch+1) // 2)