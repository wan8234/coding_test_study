import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = []
R = []
B = []

for i in range(N):
    line = list(input().strip('\n'))
    for j in range(M):
        if line[j] == 'R':
            R = [i, j]
            line[j] = "."
        elif line[j] == 'B':
            B = [i, j]
            line[j] = "."
    matrix.append(line)


def move(d, nR, nB):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    tR = nR[:]
    tB = nB[:]

    nRx, nRy = nR
    nBx, nBy = nB

    fin = False
    while True:
        nRx += dx[d]
        nRy += dy[d]
        nBx += dx[d]
        nBy += dy[d]
        if 0 <= nRx < N and 0 <= nBx < N and 0 <= nRy < M and 0 <= nBy < M:

            #파란색이 빠짐 - 초기화
            if matrix[nBx][nBy] == "O":
                nR, nB = tR[:], tB[:]
                fin = False
                break

            #둘 다 움직이지 않음
            if matrix[nRx][nRy] == "#" and matrix[nBx][nBy] == "#":
                break
            
            #하나가 움직이지 않음
            if matrix[nRx][nRy] == "#":
                nRx -= dx[d]
                nRy -= dy[d]
                # 구슬 두 개가 겹치는 경우
                if nRx == nBx and nRy == nBy:
                    break
            if matrix[nBx][nBy] == "#":
                nBx -= dx[d]
                nBy -= dy[d]
                if nRx == nBx and nRy == nBy:
                    break

            nR = [nRx, nRy]
            nB = [nBx, nBy]

            if matrix[nRx][nRy] == "O":
                fin = True
        else:
            break

    return fin, nR, nB


answer = 0
def dfs(R, B, cnt):
    global answer
    if cnt == 10:
        return
    for i in range(4):
        f, tR, tB = move(i, R, B)
        if f == True:
            answer = 1
            return
        #움직임이 있었던 경우에만 계속 진행
        if R != tR or B != tB:
            dfs(tR, tB, cnt+1)

dfs(R, B, 0)
print(answer)



# 5 6
# ######
# #..O.#
# #B...#
# #.R..#
# ######

# 7 7
# #######
# #...O.#
# #.....#
# #.....#
# #.B...#
# #..R..#
# #######