import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())

dp = [[0] * N for _ in range(N)]

for i in range(N):
    for start in range(N - i):
        end = start + i

        if start == end:
            dp[start][end] = 1

        elif numbers[start] == numbers[end]:
            if start + 1 == end:
                dp[start][end] = 1
            elif dp[start + 1][end - 1] == 1:
                dp[start][end] = 1

for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S - 1][E - 1])
