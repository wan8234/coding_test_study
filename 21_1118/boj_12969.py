import sys


input = sys.stdin.readline

N,K = map(int,input().split())

dp = [[[[False for _ in range(436)] for _ in range(31)] for _ in range(31)] for _ in range(31)]
ans = [0] * 31

A, B, C = 1, 2, 3

def solve(n,a,b,k):

    if n == N:
        if k == K:
            return True

        else:
            return False

    if dp[n][a][b][k]:
        return False


    dp[n][a][b][k] = True

    ans[n] = 'A'

    if solve(n + 1, a + 1, b, k): 
        return True
    
    ans[n] = 'B'

    if solve(n + 1, a , b + 1, (k + a)): 
        return True

    ans[n] = 'C'

    if solve(n + 1, a , b , (k + a + b)): 
        return True

    return False


if solve(0, 0, 0, 0) == True:
    print(*ans[0:N],sep='')
else:
    print(-1)    