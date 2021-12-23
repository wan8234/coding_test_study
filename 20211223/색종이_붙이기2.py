import sys
input = sys.stdin.readline

matrix = []
for _ in range(10):
    matrix.append(list(map(int, input().split())))

remained = [0] * 6
answer = 1e9

def dfs(x, y):
    global answer
    if matrix[x][y] == 1:
        for k in range(5, 0, -1):
            # 색종이 붙일 수 있는지 체크
            if remained[k] < 5 and x+k <= 10 and y+k <= 10:
                b = False
                #0이 있는지 확인 있으면 break
                for i in range(k):
                    for j in range(k):
                        if matrix[x+i][y+j] == 0:
                            b = True
                            break
                    if b:
                        break
                else:
                    #전부 1이면 색종이 붙이기
                    remained[k] += 1
                    for i in range(k):
                        for j in range(k):
                            matrix[x+i][y+j] = 0
                    
                    #다음 칸으로 이동
                    if y < 9:
                        dfs(x, y+1)
                    elif x < 9:
                        dfs(x+1, 0)
                    #끝난 경우
                    else:
                        answer = min(answer, sum(remained))
                        return

                    #재귀 후 처리
                    remained[k] -= 1
                    for i in range(k):
                        for j in range(k):
                            matrix[x+i][y+j] = 1
    #0인 경우
    else:
        #다음 칸으로 이동
        if y < 9:
            dfs(x, y+1)
        elif x < 9:
            dfs(x+1, 0)
        #끝난 경우
        else:
            #?
            answer = min(answer, sum(remained))
            return

dfs(0, 0)
if answer == 1e9:
    print(-1)
else:
    print(answer)
