import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

visited = [0] * (n+1)
dp = [[0] * 2 for _ in range(n+1)]

def dfs(x):
    visited[x] = 1
    dp[x][0] = 1
    for i in tree[x]:
        if visited[i] == 0:
            dfs(i)
                
            dp[x][0] += min(dp[i])
            dp[x][1] += dp[i][0]

dfs(1)
print(min(dp[1]))
