import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

pan = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dp[0][0] = 1


for x in range(n):
    for y in range(n):

        if pan[x][y] == 0:
            break

        go_right = x + pan[x][y]
        go_down = y + pan[x][y]

        if go_right < n:
            dp[go_right][y] += dp[x][y] 
        if go_down < n:
            dp[x][go_down] += dp[x][y]


print(dp[n-1][n-1])