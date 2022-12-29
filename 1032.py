N = int(input())
file_name = []

for _ in range(N):
    file_name.append(input())

pattern = list(file_name[0])
for i in range(N):
    for j in range(len(pattern)):
        if pattern[j] == file_name[i][j]:
            continue
        else:
            pattern[j] = "?"

print(''.join(pattern))