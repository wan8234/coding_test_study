import sys
input = sys.stdin.readline

T, W = map(int, input().split())
plum = [0]
for _ in range(T):
    x = int(input())
    plum.append(x)

dp = [[0] * (W+1) for _ in range(T+1)]

#0번 움직인 경우 : 1번에 있는 나무만 먹을 수 있음
for i in range(1, T+1):
    if plum[i] == 1:
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]

    for j in range(1, W+1):
        #나무 i번째보다 점프한 횟수 j가 큰 경우 없음
        if j > i:
            break

        #나무 1에서 떨어졌을 때는 움직인 횟수가 짝수여야 먹을 수 있음
        if plum[i] == 1 and j%2 == 0:
            #움직여서 먹기 or 그 자리에서 먹기(이전에 움직임)
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
        
        elif plum[i] == 2 and j%2 == 1:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1

        #못먹는 경우 
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[-1]))