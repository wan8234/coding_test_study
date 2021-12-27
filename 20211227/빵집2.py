import sys
input = sys.stdin.readline

R, C = map(int, input().split())
matrix = []
for _ in range(R):
    line = list(input().strip('\n'))
    matrix.append(line)

d = [(-1, 1), (0, 1), (1, 1)]

answer = 0

def dfs(r, c):
    matrix[r][c] = 'x'

    if c == C-1:
        return True
    
    for i in range(3):
        nr = r + d[i][0]
        nc = c + d[i][1]
        if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] == '.':
            if dfs(nr, nc):
                return True

    return False

for i in range(R):
    if dfs(i, 0):
        answer += 1

print(answer)