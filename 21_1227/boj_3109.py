import sys

input = sys.stdin.readline



R, C = map(int,input().split())


graph = [list(map(str,input().rstrip())) for _ in range(R)]

dx = [-1,0,1] # 우상 우 우하
dy = 1

answer = 0


def dfs(x,y):
    
    
    graph[x][y] = 'x' #visited 배열 대신 맵 자체에 파이프를 표시 (집과 같이 x로)

    if y == C-1: #마지막 열에 도달하면 성공
        return True


    for i in range(len(dx)):

        nx = x + dx[i]
        ny = y + dy

        if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == '.':

            if dfs(nx,ny): # 마지막 열까지 파이프 설치시 True 반환
                return True

    return False


for i in range(R):

    if dfs(i,0):
        answer += 1

print(answer)