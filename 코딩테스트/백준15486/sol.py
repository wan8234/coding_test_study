import sys
import collections

input = sys.stdin.readline


n = int(input())

dp = collections.defaultdict(lambda:0)

t = collections.defaultdict(int) #걸리는시간
p = collections.defaultdict(int) #수익


for i in range(n):
    t[i],p[i] = map(int,input().split())

M = 0 


for j in range(n):

    M = max(M,dp[j])  
    
    if t[j]+j > n :  
        continue 

    dp[t[j]+j] = max(p[j]+M,dp[t[j]+j])

print(max(dp.values()))