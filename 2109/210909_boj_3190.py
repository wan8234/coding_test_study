from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

apple = [[0] * n for _ in range(n)]

for i in range(k):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    apple[x][y] = 1

l = int(input())
move = deque()

for i in range(l):
    t, d = input().split()
    move.append([int(t), d])

snake = deque()
snake.append([0, 0])
head = [0, 0]
direction = 0
count = 0

def turn(direct, heading): # change direction function
    if heading == 'D':
        direct = (direct + 1) % 4
    else:
        direct = (direct - 1) % 4
    return direct

while True:
    count += 1
        
    new_x = head[0] + dx[direction] # new head_x
    new_y = head[1] + dy[direction] # new head_y

    if new_x < 0 or new_y < 0 or new_x >= n or new_y >= n: # hit wall
        break
    
    if [new_x, new_y] in snake: # hit body
        break

    head = [new_x, new_y]

    if apple[new_x][new_y] == 1: # meet apple
        apple[new_x][new_y] = 0
        snake.append([new_x, new_y])
    else:
        snake.append([new_x, new_y])
        snake.popleft()

    if move and count == move[0][0]: # check the direction
        time, heading = move.popleft()
        direction = turn(direction, heading)
    
print(count)


