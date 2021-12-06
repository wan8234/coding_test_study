import sys
input = sys.stdin.readline

S1 = input().strip('\n')
S2 = input().strip('\n')

dp = [0] * (len(S2)+1)
answer = 0

for i in range(len(S1)):
    for j in range(len(S2)-1, -1, -1):
        if S1[i] == S2[j]:
            dp[j] = dp[j-1] + 1
            if answer < dp[j]:
                answer = dp[j]
        else:
            dp[j] = 0

print(answer)
