import sys
input = sys.stdin.readline

n = int(input())
dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i - 2]
for i in range(3, 10001):
    dp[i] += dp[i - 3]
for _ in range(n):
    num = int(input())
    print(dp[num])

# import sys
# input = sys.stdin.readline

# n = int(input())
# dp = [0] * 10001
# dp[1] = 1
# dp[2] = 2
# dp[3] = 3
# dp[4] = 4

# for i in range(5, 10001):
#     dp[i] = dp[i - 1] + (dp[i - 2] - dp[i - 3])
#     if i % 3 == 0:
#         dp[i] += 1

# for _ in range(n):
#     num = int(input())
#     print(dp[num])
