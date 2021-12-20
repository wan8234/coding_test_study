import sys
input = sys.stdin.readline

matrix = []
n, m = map(int, input().split())
camera = []
blind = 0
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if 0 < line[j] < 6:
            camera.append((i, j))
        elif line[j] == 0:
            blind += 1
    matrix.append(line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#d : 0상 1하 2좌 3우
def monitor(x, y, temp, d, safe):
    x += dx[d]
    y += dy[d]
    while 0 <= x < n and 0 <= y < m:
        if temp[x][y] != 6:
            if temp[x][y] == 0:
                safe -= 1
                temp[x][y] = -1
        else:
            break
        x += dx[d]
        y += dy[d]
    return temp, safe

direction = [[[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 3], [0, 2], [2, 1], [3, 1]], [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], [[0, 1, 2, 3]]]

answer = n*m
def dfs(no, temp, safe):
    global answer
    if no == len(camera):
        answer = min(answer, safe)
        return
    x, y = camera[no]
    camera_no = matrix[x][y]
    for f in direction[camera_no-1]:
        nsafe = safe
        ntemp = [temp[i][:] for i in range(n)]
        for s in f:
            ntemp, nsafe = monitor(x, y, ntemp, s, nsafe)
        dfs(no+1, ntemp, nsafe)


dfs(0, matrix, blind)
print(answer)
    
