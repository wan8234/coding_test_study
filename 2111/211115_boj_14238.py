import sys
input = sys.stdin.readline

S = list(input().rstrip())

length = len(S)
answer = [''] * length
A, B, C = 0, 1, 2

number = [S.count(alpha) for alpha in ('A', 'B', 'C')]
dp = [[[[[False for _ in range(3)] for _ in range(3)] for _ in range(length)] for _ in range(length)] for _ in range(length)]

def dfs(a, b, c, prev):
    if [a, b, c] == number:
        print(''.join(answer))
        exit(0)
    
    if dp[a][b][c][prev[0]][prev[1]]:
        return False
    
    dp[a][b][c][prev[0]][prev[1]] = True

    if a + 1 <= number[A]:
        answer[a + b + c] = 'A'
        if dfs(a + 1, b, c, [prev[1], A]):
            return True
    
    if b + 1 <= number[B]:
        answer[a + b + c] = 'B'
        if prev[1] != B:
            if dfs(a, b + 1, c, [prev[1], B]):
                return True
    
    if c + 1 <= number[C]:
        answer[a + b + c] = 'C'
        if prev[0] != C and prev[1] != C:
            if dfs(a, b, c + 1, [prev[1], C]):
                return True
    
    return False

dfs(0, 0, 0, [0, 0])
print(-1)