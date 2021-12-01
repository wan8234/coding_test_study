from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(rx, ry, bx, by):
    queue = deque()
    queue.append((rx, ry, bx, by, 0))
    visit = set()
    visit.add((rx, ry, bx, by))

    while queue:
        rx, ry, bx, by, count = queue.popleft()

        for i in range(4):
            r_goal, b_goal = False, False
            r_move, b_move = 0, 0
            new_rx, new_ry = rx, ry
            new_bx, new_by = bx, by

            # RED
            while board[new_rx + dx[i]][new_ry + dy[i]] != '#':
                if board[new_rx + dx[i]][new_ry + dy[i]] == 'O':
                    r_goal = True
                    break
                else:
                    new_rx += dx[i]
                    new_ry += dy[i]
                r_move += 1

            # BLUE
            while board[new_bx + dx[i]][new_by + dy[i]] != '#':
                if board[new_bx + dx[i]][new_by + dy[i]] == 'O':
                    b_goal = True
                    break
                else:
                    new_bx += dx[i]
                    new_by += dy[i]
                b_move += 1

            if r_goal and b_goal:
                continue
            elif r_goal:
                return True
            elif count <= 8 and not b_goal:
                if new_rx == new_bx and new_ry == new_by:
                    if r_move > b_move:
                        new_rx -= dx[i]
                        new_ry -= dy[i]
                    else:
                        new_bx -= dx[i]
                        new_by -= dy[i]
                
                if (new_rx, new_ry, new_bx, new_by) not in visit:
                    queue.append((new_rx, new_ry, new_bx, new_by, count + 1))
                    visit.add((new_rx, new_ry, new_bx,new_by))
    return False


N, M = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(N)]

red = []
blue = []

for i in range(1, N - 1):
    for j in range(1, M - 1):
        if board[i][j] == 'R':
            red = [i, j]
        if board[i][j] == 'B':
            blue = [i, j]
        if red != [] and blue != []:
            break

result = bfs(red[0], red[1], blue[0], blue[1])

if result:
    print(1)
else:
    print(0)