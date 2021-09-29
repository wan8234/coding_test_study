import sys
input = sys.stdin.readline

n = int(input())
consult = [list(map(int, input().split())) for _  in range(n)]
dp = [0] * (n + 1)

maximum = 0
for i in range(n):
    maximum = max(maximum, dp[i])
    if i + consult[i][0] > n:
        continue
    dp[i + consult[i][0]] = max(maximum + consult[i][1], dp[i + consult[i][0]])

print(max(dp))