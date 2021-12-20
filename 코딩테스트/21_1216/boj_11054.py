import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
 
dp = [0 for i in range(N)]
dp2 = [0 for i in range(N)]

answer = 0
 

for i in range(N): #LIS 정방향
    for j in range(i):
         if (arr[i]>arr[j] and dp[i]<dp[j]):
             dp[i] = dp[j]

    dp[i] +=1 
 
 

for i in range(N-1,-1,-1): #LIS 역방향
    for j in range(N-1, i, -1):
         if (arr[i]>arr[j] and dp2[i]<dp2[j]):
             dp2[i] = dp2[j]

    dp2[i] +=1 
 
for i in range(N):

    if dp[i]+dp2[i] > answer:
        answer = dp[i]+dp2[i]

print(answer-1)