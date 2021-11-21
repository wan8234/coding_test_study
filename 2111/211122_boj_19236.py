# 4*4 크기 공간
# 칸에 물고기 한 마리
# 각각의 물고기는 번호와 방향, 방향은 상하좌우 대각선
# 청소년 상어는 (0,0)에 위치, 들어가서 물고기 먹고 해당 물고기의 방향 가짐
# 이후 물고기 이동
# 물고기는 번호순으로 이동
# 한칸 이동, 빈칸과 물고기 있는 칸으로만 이동 가능, 물고기가 겹치면 서로 위치를 바꿈
# 상어는 방향에 있는 칸으로 이동 가능, 한번에 여러 칸 이동 가능, 빈칸은 이동 불가능
# 상어가 이동 불가할 경우 집으로 감
# 상어가 먹을 수 있는 물고기 번호 최대합 구하기

import copy
import sys
input = sys.stdin.readline

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

fishes = {}
water = []
answer = 0

for i in range(4):
    temp = list(map(int, input().split()))
    position = []

    for j in range(0, 8, 2):
        fishes[temp[j]] = [i, j // 2, temp[j + 1]]
        position.append(temp[j])
    
    water.append(position)

fishes = dict(sorted(fishes.items()))

def dfs(shark, ori_fishes, ori_water, eat):
    fishes = copy.deepcopy(ori_fishes)
    water = copy.deepcopy(ori_water)

    number = water[shark[0]][shark[1]] # 현재 물고기 번호    
    cx, cy, cd = fishes[number] # 물고기 위치, 방향 정보
    
    water[shark[0]][shark[1]] = 0 # 물고기 잡아 먹힘
    del(fishes[number]) # 물고기 잡아 먹힘

    eat += number # 물고기 먹음
    
    for key in fishes.keys(): # 물고기 이동
        fx, fy, fd = fishes[key]
        for i in range(8): # 가능한 방향 모두 따짐
            nd = fd + i
            if nd > 8:
                nd %= 8
            
            nx = fx + dx[nd]
            ny = fy + dy[nd]

            if 0 <= nx < 4 and 0 <= ny < 4: # 범위 안 일 경우
                if nx == cx and ny == cy: # 상어와 겹칠 경우
                    continue
                elif water[nx][ny] == 0: # 빈 공간
                    water[fx][fy] = 0
                    water[nx][ny] = key
                    fishes[key] = [nx, ny, nd]
                    break
                elif water[nx][ny] != 0: # 물고기 겹칠 경우
                    overlay = water[nx][ny]
                    water[fx][fy], water[nx][ny] = overlay, key
                    
                    fishes[key] = [nx, ny, nd]
                    fishes[overlay] = [fx, fy, fishes[overlay][2]]            
                    break
            else:
                continue

    flag = 0    
    while True: # 상어가 이동하는 경우의 수
        cx = cx + dx[cd]
        cy = cy + dy[cd]

        if 0 <= cx < 4 and 0 <= cy < 4: # 범위 안에 있는 경우
            if water[cx][cy] != 0: # 물고기 존재
                flag = 1
                dfs([cx, cy], fishes, water, eat)                
            else: # 물고기 없음
                continue
        else: # 범위 벗어난 경우
            break
    
    if flag == 0: # 더 이상 상어가 이동할 수 없는 경우
        global answer
        answer = max(answer, eat)
        return

dfs([0, 0], fishes, water, 0)

print(answer)