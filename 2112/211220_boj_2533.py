import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dp = [[0, 0] for _ in range(N + 1)]
visit = [0] * (N + 1)

def dfs(node):
    visit[node] = 1
    dp[node][0] = 1

    for next_node in tree[node]:
        if not visit[next_node]:
            dfs(next_node)
            dp[node][0] += min(dp[next_node][0], dp[next_node][1])
            dp[node][1] += dp[next_node][0]

dfs(1)
result = min(dp[1][0], dp[1][1])
print(result)