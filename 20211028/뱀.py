import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
apple = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    apple.append((x, y))
turn = []
for _ in range(int(input())):
    x, y = map(str, input().split())
    turn.append((int(x), y))

snake = [(1, 1)]

turn = deque(turn)
snake = deque(snake)

direction = 1 #상0 우1 하2 좌3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

time = 0

while True:
    x, y = snake[-1]
    x += dx[direction]
    y += dy[direction]
    time += 1

    if x <= 0 or x > n or y <= 0 or y > n:
        break
    if (x, y) in snake:
        break
    if (x, y) in apple:
        apple.remove((x, y))
    else:
        snake.popleft()
    
    
    snake.append((x, y))

    if turn and turn[0][0] == time:
        if turn[0][1] == 'L':
            direction -= 1
            if direction == -1:
                direction = 3
        else:
            direction += 1
            if direction == 4:
                direction = 0
        turn.popleft()

print(time)
    