import sys

input = sys.stdin.readline

n = int(input()) 
k = int(input()) 

board = [[0]*(n+1) for i in range(n+1)]

snake = [(1,1)]

for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1

L = [input().split() for _ in range(int(input()))]

d = [(0,1),(1,0),(0,-1),(-1,0)] 
d_f = 0
time = 0
x,y = 1,1

while True:

    time+=1

    x+=d[d_f][0]
    y+=d[d_f][1]

    if 1<=x<=n and 1<=y<=n:
        snake.append((x,y)) 
        for i in snake[:-1]: 
            if (x,y)==i:
                print(time)
                exit(0)
        if board[x][y]==0: 
            snake.pop(0)
        if board[x][y]==1:
            board[x][y]=0
    else:  
        print(time)
        break

    if L and time == int(L[0][0]):
        if L[0][1]=='D': 
            d_f = d_f+1 if d_f<3 else 0
            L.pop(0)
        elif L[0][1]=='L':
            d_f = d_f - 1 if d_f > 0 else 3
            L.pop(0)