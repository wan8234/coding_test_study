import sys
from collections import defaultdict


input = sys.stdin.readline


n = int(input())


army = list(map(int,input().split()))
army.reverse()

#dp = defaultdict(lambda:1)
dp = [1 for i in range(n)]


for i in range(n):
    for j in range(i):
        if army[j] < army[i]:
            dp[i] = max(dp[i],dp[j]+1)


print(n-max(dp))