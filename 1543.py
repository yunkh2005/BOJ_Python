import sys
input = sys.stdin.readline

document = input().rstrip()         # 문서
word = input().rstrip()             # 검색 단어
index = 0
result = 0

while len(document) - index >= len(word):
    if document[index:index + len(word)] == word:
        result += 1
        index += len(word)
    else:
        index += 1

print(result)