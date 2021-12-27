N = int(input())    # 숫자 범위
price = list(map(int, input().split())) #각 숫자의 가격
M = int(input())    # 자본

dp = [0 for _ in range(M+1)]

for i in range(N-1, -1, -1):
    cost = price[i]
    for j in range(cost, M+1):
        dp[j] = max(dp[j-cost]*10 + i, i, dp[j])

print(dp[M])

