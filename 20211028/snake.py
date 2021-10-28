#종료 조건 : 벽 충돌, 자기자신 충돌

# 보드의 크기, 사과의 갯수
N = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]
arr[1][1] = 1   # 뱀이 있는 위치 :1

# 사과 입력
for _ in range(int(input())):
    row, col = map(int, input().split())
    arr[row][col] = 9   # 사과가 있는 위치 :9

# 뱀의 방향 변환 정보 갯수
# L:왼쪽   D:오른쪽
info = []
L = int(input())
for _ in range(L):
    X, C = input().split()
    info.append((int(X), C))

# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = 0

def dnsb(dir, C):
    if C == 'L':
        dir = (dir - 1) % 4
    if C == 'D':
        dir = (dir + 1) % 4
    return dir

time = 0    # 처음 시간
x = 1   # 첫 뱀 위치, 행
y = 1   # 첫 뱀 위치, 열
snake = [(x,y)] # 뱀 좌표
idx = 0
while True:
    nx = x + dx[dir]
    ny = y + dy[dir]

    #행렬 안에 있어야함, 이동한 위치가 뱀이 아님
    if 1<= nx <= N and 1 <= ny <= N and arr[nx][ny] != 1:
        #사과 o
        if arr[nx][ny] == 9:
            arr[nx][ny] = 1
            snake.append((nx,ny))
        #사과 x
        if arr[nx][ny] == 0:
            arr[nx][ny] = 1
            snake.append((nx, ny))
            a, b = snake.pop(0)
            arr[a][b] = 0 
    else:
        time += 1
        break
    
    time += 1
    x, y = nx, ny
    
    if idx < L and time == info[idx][0]:
        dir = dnsb(dir, info[idx][1])
        idx += 1
    
print(time)

