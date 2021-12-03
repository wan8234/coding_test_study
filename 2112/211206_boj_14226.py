from collections import deque
import sys
input = sys.stdin.readline

S = int(input())

dp = [[-1] * (S + 1) for _ in range(S + 1)]
dp[1][0] = 0

def bfs(emo, clip):
	queue = deque()
	queue.append((emo, clip))
	
	while queue:
		e, c = queue.popleft()
		
		if dp[e][e] == -1:
			dp[e][e] = dp[e][c] + 1
			queue.append((e, e))
		if e + c <= S and dp[e + c][c] == -1:
			dp[e + c][c] = dp[e][c] + 1
			queue.append((e + c, c))
		if e - 1 >= 0 and dp[e - 1][c] == -1:
			dp[e - 1][c] = dp[e][c] + 1
			queue.append((e - 1, c))

bfs(1, 0)
answer = int(1e9)
for i in range(S + 1):
	if dp[S][i] != -1:
		answer = min(answer, dp[S][i])
print(answer)