import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

dp = []

for i in range(n):
    if i == 0:
        dp.append(1)
    else:
        cnt = 0
        for j in range(i):
            if numbers[j] > numbers[i] and cnt < dp[j]:
                cnt = dp[j]
        dp.append(cnt+1)

print(n - max(dp))