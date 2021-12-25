import sys
input = sys.stdin.readline

dx = [-1, 0, 1]

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
visit = [[False] * C for _ in range(R)]

result = 0

def pipe(x, y):
    if y >= C - 1:
        return True
    
    for d in dx:
        if 0 <= x + d < R and board[x + d][y + 1] == '.' and not visit[x + d][y + 1]:
            visit[x + d][y + 1] = True
            if pipe(x + d, y + 1):
                return True
    return False
    
for r in range(R):
    if board[r][0] == '.':
        if pipe(r, 0):
            result += 1
            
print(result)