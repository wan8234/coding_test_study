n, m, k = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

firstDir = list(map(int, input().split()))  # 처음 방향 정보
dirInfo = [[] for _ in range(m)]    # 회전 우선순위 정보
smell = [[[0, 0]] * n for _ in range(n)]

for i in range(m):
    for j in range(4):
        dirInfo[i].append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 냄새 업데이트
def updateInfo():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if arr[i][j] != 0:
                smell[i][j] = [arr[i][j], k]


def move():

    arr_moved = [[0] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):

            if arr[x][y] != 0:
                nowDir = firstDir[arr[x][y] - 1] # 현재 상어의 방향
                found = False
                # 냄새 확인
                for index in range(4):
                    nx = x + dx[dirInfo[arr[x][y] - 1][nowDir - 1][index] - 1]
                    ny = y + dy[dirInfo[arr[x][y] - 1][nowDir - 1][index] - 1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell[nx][ny][1] == 0: # 냄새 없음 확인
                            firstDir[arr[x][y] - 1] = dirInfo[arr[x][y] - 1][nowDir - 1][index]
                            if arr_moved[nx][ny] == 0:
                                arr_moved[nx][ny] = arr[x][y]
                            else:
                                arr_moved[nx][ny] = min(arr_moved[nx][ny], arr[x][y])
                            found = True
                            break
                if found:
                    continue
                # 냄새 있을경우 되돌아가기
                for index in range(4):
                    nx = x + dx[dirInfo[arr[x][y] - 1][nowDir - 1][index] - 1]
                    ny = y + dy[dirInfo[arr[x][y] - 1][nowDir - 1][index] - 1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell[nx][ny][0] == arr[x][y]:
                            firstDir[arr[x][y] - 1] = dirInfo[arr[x][y] - 1][nowDir - 1][index]
                            arr_moved[nx][ny] = arr[x][y]
                            break
    return arr_moved

t = 0
while True:
    updateInfo()
    arr = move()
    t += 1


    timeout = True
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                timeout = False

    if timeout:
        print(t)
        break

    if t >= 500:
        print(-1)
        break
