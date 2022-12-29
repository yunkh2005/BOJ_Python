T = int(input())

def wordReverse():
    word = list(map(str, input().split()))
    for i in range(len(word)):
        word[i] = ''.join(reversed(word[i]))
    
    print(' '.join(word))

for _ in range(T):
    wordReverse()