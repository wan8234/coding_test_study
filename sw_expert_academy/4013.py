# 자석이 회전 될 때 붙어 있는 자석은 서로 붙어 있는 날의 자성이 다를 경우에만 반대 방향으로 1칸 회전
# 시계 방향 1, 반시계 방향 -1
# N극이 0, S극이 1

right = 2
left = 6

def bfs(magnet, turn):
    queue = []

    for t in turn:
        t[0] -= 1
        queue.append(t)
        visit = [0] * 4
        
        while queue:
            idx, direct = queue.pop(0)
            visit[idx] = 1
            if idx > 0 and visit[idx - 1] == 0:
                if magnet[idx][left] != magnet[idx - 1][right]:
                    queue.append([idx - 1, direct * -1])
            if idx < 3 and visit[idx + 1] == 0:
                if magnet[idx][right] != magnet[idx + 1][left]:
                    queue.append([idx + 1, direct * -1])

            if direct == 1:
                magnet[idx].insert(0, magnet[idx].pop())
            elif direct == -1:
                magnet[idx].append(magnet[idx].pop(0))
                    
    return magnet

T = int(input())

for test_case in range(1, T + 1):
    K = int(input())
    magnet = [list(map(int, input().split())) for _ in range(4)]
    turn = [list(map(int, input().split())) for _ in range(K)]
    result = 0

    magnet = bfs(magnet, turn)

    for i in range(4):
        if magnet[i][0] == 1:
            result += 2**i
    print('#{} {}'.format(test_case, result))

# 10
# 2
# 0 0 1 0 0 1 0 0
# 1 0 0 1 1 1 0 1
# 0 0 1 0 1 1 0 0
# 0 0 1 0 1 1 0 1
# 1 1
# 3 -1
# 2
# 1 0 0 1 0 0 0 0
# 0 1 1 1 1 1 1 1
# 0 1 0 1 0 0 1 0
# 0 1 0 0 1 1 0 1
# 3 1
# 1 1
# 5
# 0 0 1 1 1 1 1 1
# 1 1 1 1 1 0 1 0
# 0 0 0 0 1 0 0 1
# 0 1 0 1 0 1 0 1
# 4 -1
# 3 1
# 4 -1
# 3 -1
# 1 -1
# 2
# 1 0 1 0 0 1 0 1
# 0 0 1 0 1 1 1 1
# 0 0 1 1 0 0 0 1
# 0 1 0 1 1 0 0 0
# 2 -1
# 1 1
# 7
# 0 0 1 1 0 1 1 1
# 0 1 0 1 1 0 0 0
# 1 1 1 0 0 0 0 1
# 1 1 1 0 0 1 0 0
# 4 1
# 2 1
# 2 -1
# 3 1
# 2 1
# 4 1
# 2 -1
# 10
# 1 0 0 0 0 0 0 1
# 1 0 1 0 1 1 0 1
# 1 0 0 1 0 0 0 1
# 1 1 0 1 0 1 1 1
# 2 1
# 1 1
# 2 -1
# 3 1
# 3 -1
# 2 -1
# 2 -1
# 1 1
# 4 1
# 4 1
# 10
# 0 1 0 0 1 1 0 0
# 0 1 1 0 1 0 1 1
# 0 0 0 0 0 1 1 0
# 0 0 1 0 1 0 1 1
# 3 1
# 1 -1
# 2 1
# 4 -1
# 3 1
# 3 -1
# 4 -1
# 2 -1
# 1 -1
# 3 -1
# 10
# 0 1 0 1 0 1 0 0
# 0 1 1 1 1 1 0 1
# 1 0 0 0 0 1 1 0
# 1 0 0 0 0 0 0 1
# 1 1
# 4 -1
# 4 -1
# 2 -1
# 2 -1
# 2 -1
# 3 -1
# 2 1
# 3 1
# 3 -1
# 20
# 1 0 0 0 1 1 0 0
# 1 0 0 1 1 1 0 0
# 0 1 1 1 0 1 1 1
# 1 1 1 1 0 1 1 1
# 1 1
# 4 -1
# 4 -1
# 2 -1
# 3 -1
# 1 1
# 4 1
# 4 -1
# 4 -1
# 4 -1
# 3 -1
# 3 -1
# 4 -1
# 4 -1
# 2 -1
# 1 1
# 3 -1
# 3 -1
# 2 1
# 1 1
# 20
# 0 0 1 1 1 0 1 0
# 0 1 0 0 1 0 1 0
# 1 1 1 0 1 0 1 0
# 0 0 1 0 0 1 1 1
# 1 -1
# 4 -1
# 3 -1
# 1 1
# 4 1
# 2 1
# 1 -1
# 4 1
# 2 -1
# 4 -1
# 1 1
# 4 -1
# 1 1
# 2 -1
# 1 -1
# 3 -1
# 1 1
# 2 1
# 3 1
# 3 -1
