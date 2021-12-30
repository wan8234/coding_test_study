import sys

input = sys.stdin.readline


N = int(input())

numbers = list(map(int,input().split()))

M = int(input())


dp = [[0 for _ in range(N)]for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(N-1):

    if numbers[i] == numbers[i+1]:
        dp[i][i+1] = 1

for i in range(2, N):
    for j in range(N-i):

        if numbers[j] == numbers[i+j] and dp[j+1][i+j-1] == 1:
            dp[j][i+j] = 1


for _ in range(M):

    S,E = map(int,input().split())

    if S == E:
        print(1)
    else:
        print(dp[S-1][E-1])