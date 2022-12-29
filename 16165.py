N, M = map(int, input().split())
group = {}
member = []

# 걸그룹 정보 저장
for i in range(N):
    # 걸그룹 팀 이름 저장(group 딕셔너리 키)
    team_name = input()

    # 걸그룹 멤버 저장(group 딕셔너리 값으로 리스트)
    num = int(input())
    member = [input() for i in range(num)]
    group[team_name] = member

# 걸그룹 멤버 알파벳 순 정렬
for i in group:
    group[i].sort()

# 퀴즈 풀기
for i in range(M):
    name = input()
    number = int(input())

    # 0이면 해당 팀에 속한 멤버 이름 알파벳 순 출력
    if number == 0:
        print_mem = group[name]
        for j in print_mem:
            print(j)
    # 1이면 해당 멤버가 속한 팀 이름 출력
    else:
        for k, v in group.items():
            if name in v:
                print(k)