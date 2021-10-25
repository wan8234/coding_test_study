import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
direction = list(map(int, input().split()))

shark = {}  

for i in range(n):
    for j in range(n):

        if graph[i][j] != 0:
            shark[graph[i][j]] = [i, j, direction[graph[i][j] - 1]]  
        graph[i][j] = None


shark_dir = [list(map(int, input().split())) for _ in range(m * 4)] 


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = -1

while time <= 1000:

    if len(shark) == 1:
        print(time)
        exit(0)

    keys = list(shark.keys())
    keys.sort()  

    for index in keys:
        if graph[shark[index][0]][shark[index][1]] is None:  
            graph[shark[index][0]][shark[index][1]] = [index, k]  
        elif graph[shark[index][0]][shark[index][1]][0] == index:  
            graph[shark[index][0]][shark[index][1]] = [index, k]
        else:  
            del shark[index]


    keys = list(shark.keys())
    keys.sort()  

    for index in keys :
        x, y, d = shark[index]  

        flag_blank = False

        for i in shark_dir[(index - 1) * 4 + (d - 1)]:

            nx = x + dx[i-1]
            ny = y + dx[i-1]
            nd = i

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] is None:  
                    flag_blank = True  
                    shark[index] = [nx, ny, nd]
                    break

        flag_same = False

        if not flag_blank:  

            for i in shark_dir[(index - 1) * 4 + (d - 1)]:

                nx = x + dx[i-1]
                ny = y + dx[i-1]
                nd = i

                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny][0] == index:  
                        flag_same = True  
                        shark[index] = [nx, ny, nd]
                        break
        else:
            continue
        if not flag_same:  
            del shark[index]  

    for i in range(n):  
        for j in range(n):
            if graph[i][j] is not None:
                graph[i][j][1] -= 1
                if graph[i][j][1] == 0:  
                    graph[i][j] = None

    time += 1

print(-1)