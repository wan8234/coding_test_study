import sys
input = sys.stdin.readline

N, K = map(int, input().split())

A, B, C = 1, 2, 3
dp = [[[[False for _ in range(436)] for _ in range(31)] for _ in range(31)] for _ in range(31)]
answer = [0] * 31

def dfs(a, b, index, count):
    if index == N:
        if count == K:
            print(''.join(answer[0:N]))
            exit(0)
        else:
            return False
    
    if dp[a][b][index][count]:
        return False
    
    dp[a][b][index][count] = True

    answer[index] = 'A'
    if dfs(a + 1, b, index + 1, count):
        return True
    
    answer[index] = 'B'
    if dfs(a, b + 1, index + 1, count + a):
        return True
    
    answer[index] = 'C'
    if dfs(a, b, index + 1, count + a + b):
        return True
    
    return False

dfs(0, 0, 0, 0)
print(-1)