import sys
input = sys.stdin.readline

T = int(input())

def union(K, size):
    S = [0 for _ in range(K + 1)]
    for i in range(1, K + 1):
        S[i] = S[i-1] + size[i]
    
    DP = [[0 for _ in range(K + 1)] for _ in range(K + 1)]
    for i in range(2, K+1):
        for j in range(1, K+2-i):
            DP[j][j+i-1] = min([DP[j][j+k] + DP[j+k+1][j+i-1] for k in range(i-1)]) + S[j+i-1] - S[j-1]
    
    return DP[1][K]

for _ in range(T):
    K = int(input())
    size = [0] + list(map(int, input().split()))
    
    print(union(K, size))


# DP[i][j]: i에서 j까자ㅣ 합치는데 필요한 최소 비용
# DP[i][k] = DP[k+1][j] + sum(size[i:j+1])
# S는 1번부터 i 번까지 누적 합