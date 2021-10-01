import sys
input = sys.stdin.readline

n = int(input())

table = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for x in range(n):
    for y in range(n):
        if x == n - 1 and y == n - 1:
            break
        if dp[x][y] != 0:
            value = table[x][y]

            for i in range(2):
                if i == 0:
                    nx = x
                    ny = y + value
                elif i == 1:
                    nx = x + value
                    ny = y
                
                if nx >= n or ny >= n:
                    continue
                else:
                    dp[nx][ny] += dp[x][y]

print(dp[n - 1][n - 1])                