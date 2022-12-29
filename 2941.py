word = input()
c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in c:
    word = word.replace(i, '0')

print(word)
print(len(word))

