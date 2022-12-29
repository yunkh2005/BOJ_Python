N, L, K = map(int, input().split())
question = [0 for _ in range(N)]    # 문제 sub1, 2의 역량 저장 리스트
easy, hard = 0, 0
result = 0

for i in range(N):
    sub1, sub2 = map(int, input().split())
    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1
# hard 문제
result += min(hard, K) * 140

# easy 문제
if hard < K:
    result += min(K - hard, easy) * 100

print(result)