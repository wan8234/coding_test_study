import sys

input = sys.stdin.readline



R, C = map(int,input().split())


graph = [list(map(str,input().rstrip())) for _ in range(R)]

dx = 1 
dy = [-1,0,1] # 우상 우 우하

answer = 0

def dfs(y,x):
       
    graph[y][x] = 'x' #visited 배열 대신 맵 자체에 파이프를 표시 (집과 같이 x로)

    if x == C-1: #마지막 열에 도달하면 성공
        return True

    for i in range(len(dy)):

        nx = x + dx
        ny = y + dy[i]

        if 0 <= nx < C and 0 <= ny < R and graph[ny][nx] == '.':

            if dfs(ny,nx): #
                return True

    return False


for i in range(R):

    if dfs(i,0):
        answer += 1

print(answer)
