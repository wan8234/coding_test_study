import sys
input = sys.stdin.readline

R, C = map(int, input().split())
matrix = [input().strip('\n') for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 1

def bfs():
    global answer

    #대기열에 중복이 없도록 집합 이용
    q = set([(0, 0, matrix[0][0])])

    while q:
        #value에 지나온 알파벳들을 넣을 거임 - 문자열 형태로
        x, y, value = q.pop()

        #알파벳 26개 다 지났으면 어차피 최대 값임
        if answer == 26:
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #value에 중복되는 값이 없으면 추가
            if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] not in value:
                q.add((nx, ny, value + matrix[nx][ny]))
                #value의 길이 + 1이 지나온 칸 수
                answer = max(answer, len(value) + 1)
            
bfs()
print(answer)