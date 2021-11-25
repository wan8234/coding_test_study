import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = []
for _ in range(r):
    board.append(input().rstrip())

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move(x, y):
    global res
    q = set([(x, y, board[x][y])])

    while q:
        x, y, s = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #이미 있는 알파벳일 경우 무시
            if 0 <= nx < r and 0 <= ny < c:
                if board[nx][ny] not in s:
                    q.add((nx,ny,s + board[nx][ny]))
                    res = max(res, len(s)+1)

res = 1
move(0, 0)
print(res)
