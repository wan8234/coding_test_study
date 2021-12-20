import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

N = int(sys.stdin.readline())

tree = [[] for _ in range(N+1)]

visited = [True for _ in range(N+1)]

dp = [[0,0] for _ in range(N+1)]

for _ in range(N-1):
    u,v = map(int,sys.stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

def dfs(now):

    visited[now]=False 

    dp[now][0]=1
    dp[now][1]=0

    for i in tree[now]:

        if visited[i]:

            dfs(i)

            dp[now][0] += dp[i][1]
            dp[now][1] += max(dp[i][0],dp[i][1])

dfs(1)
print(N-max(dp[1][0],dp[1][1]))