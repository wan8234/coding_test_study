import sys
input = sys.stdin.readline

T, W = map(int, input().split())
tree = [0]
dp = [[0] * (W + 1) for _ in range(T + 1)]

for _ in range(T):
    tree.append(int(input()))

for i in range(1, T + 1):
    for j in range(W + 1):
        if j == 0:
            if tree[i] == 1:
                dp[i][0] = dp[i - 1][0] + 1
            else:
                dp[i][0] = dp[i - 1][0]
        else:
            if (tree[i] == 1 and j % 2 == 0) or (tree[i] == 2 and j % 2 == 1):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])

print(max(dp[-1]))
