import sys
from collections import deque

input = sys.stdin.readline


n,m = 12,6

boom = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


maps = [list(input().strip()) for _ in range (n)]


def bfs(x, y, color):

    same_color = set()

    queue = deque()
    queue.append((x,y))
    
    while queue:

        x,y = queue.popleft()

        if (x,y) in same_color: 
            continue

        same_color.add((x,y))

        for i in range(4):

            nx = x+dx[i]
            ny = y+dy[i]

            if not ( 0 <= nx < n and 0 <= ny < m): 
                continue

            if maps[nx][ny] == color:
                queue.append((nx, ny))

    return same_color

def fall():

    for y in range(m):
        for x in range(n-1, -1, -1):

            if maps[x][y] == '.': 
                continue
            
            for k in range(n-1, x, -1):

                if maps[k][y] == '.':
                    maps[k][y] = maps[x][y]
                    maps[x][y] = '.'


while True:

        check = 0
        
        for i in range(n-1, -1, -1):
            for j in range(m):

                if maps[i][j] == '.': 
                    continue

                array = bfs(i, j, maps[i][j])

                if len(array) >= 4:

                    if check == 0: 
                        check = 1

                    for x, y in array:
                        maps[x][y] = '.'
        fall()

        if check == 1:  
            boom += 1

        elif check == 0: 
            break


print(boom)
