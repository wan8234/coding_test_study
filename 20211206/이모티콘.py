import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
dp = [[-1] * (n+1) for _ in range(n+1)]
# dp[x][y] x: 입력한 임티 개수, y: 클립보드에 저장된 임티 개수

dq = deque([[1, 0]])
dp[1][0] = 0

while dq:
    x, y = dq.popleft()
    #저장
    if dp[x][x] == -1:
        dp[x][x] = dp[x][y] + 1
        dq.append([x, x])
    #붙여넣기
    if x+y <= n and dp[x+y][y] == -1:
        dp[x+y][y] = dp[x][y] + 1
        dq.append([x+y, y])
    #지우기
    if x-1 >= 0 and dp[x-1][y] == -1:
        dp[x-1][y] = dp[x][y] + 1
        dq.append([x-1, y])

answer = n+1
for i in range(1, n+1):
    if dp[n][i] != -1:
        answer = min(answer, dp[n][i])

print(answer)