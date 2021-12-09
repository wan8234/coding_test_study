import sys

input = sys.stdin.readline

n,m = map(int,(input().split()))

mem = list(map(int, input().split()))
cost = list(map(int, input().split()))

total_cost = sum(cost)

dp = [[0 for _ in range(n+1)] for _ in range(total_cost+1)]

for i in range(1,total_cost+1):
    for j in range(1,n+1):

        if i >= cost[j-1]:
            dp[i][j] = max(dp[i][j-1], dp[i-cost[j-1]][j-1] + mem[j-1])

        else:
            dp[i][j] = dp[i][j-1]

    if max(dp[i]) >= m:
        print(i)
        break