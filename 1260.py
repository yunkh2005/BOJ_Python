N, M, V = map(int, input().split())

matrix = [[0] * (N + 1) for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
visit_list = [0]*(N+1)

def dfs(V):
    visit_list[V] = 1
    print(V, end=' ')
    for i in range(1,N + 1):
        if(visit_list[i] == 0 and matrix[V][i] == 1):
            dfs(i)

def bfs(V):
    queue = [V]
    visit_list[V] = 0
    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if(visit_list[i] == 1 and matrix[V][i] == 1):
                queue.append(i)
                visit_list[i] = 0

dfs(V)
print()
bfs(V)

#https://velog.io/@i-zro/%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EC%BD%94%ED%85%8C-%EB%8C%80%EB%B9%84-DFSBFS-%EB%B0%B1%EC%A4%80-1260%EB%B2%88-DFS%EC%99%80-BFS