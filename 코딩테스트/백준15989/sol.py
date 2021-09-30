import sys
from collections import defaultdict

input = sys.stdin.readline

dp = defaultdict(lambda: 1)

n = int(input())

answer = list()

for i in range(2, 10001):
    dp[i] += dp[i - 2]
    
for i in range(3, 10001):
    dp[i] += dp[i - 3]

for _ in range(n):
    answer.append(dp[int(input())])

for i in range(len(answer)):
    print(answer[i])
