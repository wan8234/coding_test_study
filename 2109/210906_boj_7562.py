from collections import deque

n = int(input())
result = []

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for i in range(n):
    l = int(input())    

    cur_x, cur_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    
    queue = deque()
    queue.append([cur_x, cur_y, 0])
    chess = [[0] * l for _ in range(l)]
    chess[cur_x][cur_y] = 1

    while queue:
        next_x, next_y, count = queue.popleft()
        
        if next_x == goal_x and next_y == goal_y:
            result.append(count)
            queue = []
            break

        for k in range(8):
            new_x, new_y = next_x + dx[k], next_y + dy[k]
            if new_x >= l or new_y >= l or new_x < 0 or new_y < 0:
                continue
            elif chess[new_x][new_y] == 1:
                continue
            else:     
                chess[new_x][new_y] = 1         
                queue.append([new_x, new_y, count + 1])

for i in result:
    print(i)

# problem 1 : if I don't check the visit info, it takes too much time. -> make chess list for check the visit