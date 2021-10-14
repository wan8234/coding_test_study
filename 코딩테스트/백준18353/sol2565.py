import sys

input = sys.stdin.readline

n = int(input())

wire = []

dp = [1 for i in range(n)]

for _ in range(n):
    wire.append(list(map(int,input().split())))


wire.sort()

for i in range(n):
    for j in range(i):
        if wire[j][1] < wire[i][1]:
            dp[i] = max(dp[i],dp[j]+1)


print(n-max(dp))