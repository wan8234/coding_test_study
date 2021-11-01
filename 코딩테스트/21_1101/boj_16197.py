import sys

input = sys.stdin.readline

n,m = map(int,input().split())


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = list()
cp = list()
result = float('inf')
visited = list()


for _ in range(n):

    board.append(list(input().rstrip()))

for i in range(n):
    for j in range(m):
        if board[i][j] == 'o':
            cp.append((i, j))


def dfs(coin_pos, dropped, play_cnt):

    global result

    if play_cnt > 10:
        return

    if dropped == 1:
        result = min(result, play_cnt)

    if coin_pos in visited:
        return

    for d in range(4):

        new_coin_pos = []
        new_dropped = dropped

        for x, y in coin_pos:

            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:

                if board[nx][ny] != '#':
                    new_coin_pos.append((nx, ny))
                else:
                    new_coin_pos.append((x, y))
            else:
                new_dropped += 1

        visited.append(coin_pos)
        dfs(new_coin_pos, new_dropped, play_cnt + 1)
        visited.remove(coin_pos)


dfs(cp, 0, 0)

if result > 10:
    print(-1)
    
else:
    print(result)