N, M, K = map(int, input().split())
matrix = []
shark = dict()

#matrix는 냄새 남길 빈 배열
#상어 딕셔너리에 좌표, 방향 저장
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] != 0:
            shark[line[j] - 1] = [i, j]
            line[j] = 0
    matrix.append(line)

line = list(map(int, input().split()))
for i in range(M):
    shark[i].append(line[i])

#방향은 [상어:현재방향:우선순위] 식으로 3차원 배열로 저장
direction = [[] for _ in range(M)]
for i in range(M*4):
    line = list(map(int, input().split()))
    direction[i//4].append(line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def poo():
    #냄새 시간 -1
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0:
                matrix[i][j][1] -= 1
                if matrix[i][j][1] == 0:
                    matrix[i][j] = 0
    #냄새 남기기
    for i in shark:
        x, y, d = shark[i]
        matrix[x][y] = [i, K]

    

def move():
    for i in shark:
        x, y, d = shark[i]
        #사방에 빈칸이 없을 때 내 냄새 좌표, 방향
        mx, my, md = x, y, d
        m = False
        for k in direction[i][d-1]:
            nx = x + dx[k-1]
            ny = y + dy[k-1]
            if 0 <= nx < N and 0 <= ny < N:
                #빈칸이면 바로 고
                if matrix[nx][ny] == 0:
                    shark[i] = [nx, ny, k]
                    break
                #내 냄새인 방향 중 가장 첫번째 것만 저장
                elif m == False and matrix[nx][ny][0] == i:
                    m = True
                    mx, my, md = nx, ny, k
        #사방에 빈칸 없는 경우
        else:
            shark[i] = [mx, my, md]

    #상어 좌표가 키인 딕셔너리 만들어서
    temp = dict()
    for i in shark:
        loc = (shark[i][0], shark[i][1])
        if loc in temp:
            temp[loc].append(i)
        else:
            temp[loc] = [i]
    
    #길이가 1이 아닌 경우 가장 작은 번호의 상어만 남기고 다 삭제
    for i in temp:
        if len(temp[i]) != 1:
            temp[i].sort()
            for x in temp[i][1:]:
                shark.pop(x)

poo()
sec = 0
while len(shark) > 1:
    sec += 1
    move()
    poo()
    if sec > 1000:
        print(-1)
        break
else:
    print(sec)