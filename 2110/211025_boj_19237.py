# 1. 냄새 뿌리기
# 2. 상하좌우 칸 중 이동
# 2-1. 겹칠 경우 번호 작은 상어가 남음

import sys
input = sys.stdin.readline

N, M, k = map(int, input().split())

shark = {}
shark_direct = [[] for _ in range(M + 1)]
smell = {}

dx = [0, -1, 1, 0, 0] # 위, 아래, 왼쪽, 오른쪽
dy = [0, 0, 0, -1, 1]

for i in range(M): # 상어 데이터 저장 목적
    shark[i + 1] = []

for i in range(N):
    temp = list(map(int, input().split()))
    
    for t in range(len(temp)):
        if temp[t]:
            shark[temp[t]].append([i, t]) # 상어 위치 값 저장

directions = list(map(int, input().split()))
for i in range(M):
    shark[i + 1].append(directions[i]) # 상어 방향 저장

for i in range(M):
    shark_direct[i + 1].append([])
    for j in range(4):
        temp = [0]
        temp .extend(list(map(int, input().split())))
        shark_direct[i + 1].append(temp) # 방향 우선 순위 저장

result = -1

for time in range(1, 1001):
    grid = {}

    for key in shark:
        [x, y], direct = shark[key]
        smell[(x, y)] = [key, 0]

    for key in shark: # 전체 상어 순회
        [x, y], direct = shark[key]

        directions = shark_direct[key][direct]

        for i in range(1, 5): # 빈칸 확인
            nx = x + dx[directions[i]]
            ny = y + dy[directions[i]]

            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in smell:
                shark[key][0][0] = nx
                shark[key][0][1] = ny
                shark[key][1] = directions[i]

                if (nx, ny) in grid:
                    grid[(nx, ny)].append(key)
                else:
                    grid[(nx, ny)] = [key]
                
                break
        else:
            for i in range(1, 5): # 냄새 확인
                nx = x + dx[directions[i]]
                ny = y + dy[directions[i]]
                
                if 0 <= nx < N and 0 <= ny < N and (nx, ny) in smell and smell[(nx, ny)][0] == key:
                    shark[key][0][0] = nx
                    shark[key][0][1] = ny
                    shark[key][1] = directions[i]

                    if (nx, ny) in grid:
                        grid[(nx, ny)].append(key)
                    else:
                        grid[(nx, ny)] = [key]
                    
                    break
    
    for key in grid: # 겹치는 상어 제거
        minimum = min(grid[key])

        for s in grid[key]:
            if s != minimum:
                del(shark[s])
        
    if len(shark) == 1: # 상어 전체 수 확인
        result = time
        break
    
    temp = {}
    for key in smell:
        if smell[key][1] + 1 >= k:
            continue
        else:
            temp[key] = [smell[key][0], smell[key][1] + 1]

    smell = temp

print(result)

    
