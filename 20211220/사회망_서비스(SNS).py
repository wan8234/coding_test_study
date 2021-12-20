import sys
input = sys.stdin.readline

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
    #0일때는 내가 얼리어답터일때, 1일때는 내가 얼리어답터가 아닐때
    #나 자신 1 넣어줌
    dp[x][0] = 1
    for i in tree[x]:
        if visited[i] == 0:
            dfs(i)
            #내가 얼리어답터니까 그냥 dp[i] 중에 작은거
            dp[x][0] += min(dp[i])
            #내가 얼리어답터가 아니니까 i는 무조건 얼리어답터
            dp[x][1] += dp[i][0]

dfs(1)
print(min(dp[1]))