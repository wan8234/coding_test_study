import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i], dp[j] + 1)

maximum = max(dp)
print(maximum)

idx = dp.index(maximum)
result = []

while idx >= 0:
    if dp[idx] == maximum:
        result.append(numbers[idx])
        maximum -= 1
    idx -= 1

result.reverse()
print(*result)