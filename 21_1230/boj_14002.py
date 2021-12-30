import sys

input = sys.stdin.readline

N = int(input())


arr = list(map(int,input().split()))


dp = [1] * N


for i in range(1, N):
    for j in range(i):

        if arr[i]>arr[j]:
            dp[i] = max(dp[i], dp[j]+1)


print(max(dp))
length = max(dp)
parr = []

for i in range(N-1, -1, -1):
    
    if dp[i]==length:
        parr.append(arr[i])
        length-=1
        
parr.reverse()
print(*parr)