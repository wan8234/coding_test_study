import sys
input = sys.stdin.readline

n, d = map(int, input().split())
short = []
dp = [i for i in range(d + 1)]

for _ in range(n):
    short.append(list(map(int, input().split())))

short.sort()

for start, end, length in short:
    if end <= d:
        dp[end] = min(dp[start] + length, dp[end])
        for i in range(end + 1, d + 1):
            dp[i] = min(dp[end] + i - end, dp[i])

print(dp[d])