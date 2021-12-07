import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [0]
A.extend(list(map(int, input().split())))
C = [0]
C.extend(list(map(int, input().split())))
C_total = sum(C)
dp = [[0 for _ in range(C_total + 1)] for _ in range(N + 1)]
result = int(1e9)

for i in range(1, N + 1):
    current = A[i]
    cost = C[i]

    for j in range(1, C_total + 1):
        if j < cost:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(current + dp[i - 1][j - cost], dp[i - 1][j])
        
        if dp[i][j] >= M:
            result = min(result, j)

if M != 0:
    print(result)
else:
    print(0)