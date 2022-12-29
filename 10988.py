def solution(s):
    mid = len(s) // 2

    # 홀수
    if len(s) % 2 != 0:         
        if s[:mid] == s[:mid:-1]:
            return 1
        else:
            return 0
    # 짝수
    else:
        if s[:mid] == s[:(mid-1):-1]:
            return 1
        else:   
            return 0

s = input()
print(solution(s))  # ''