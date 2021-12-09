import sys
from collections import deque

input = sys.stdin.readline

s = int(input())

check = [[-1]*(s+1) for _ in range(s+1)]


def bfs():

    q = deque()
    q.append([1,0])

    check[1][0] = 0

    while q:

        x,y = q.popleft()

        if check[x][x] == -1: # operation 1
            check[x][x] = check[x][y]+1
            q.append([x,x])

        if x+y <= s and check[x+y][y] == -1:
            check[x+y][y] = check[x][y]+1
            q.append([x+y,y])
        
        if x-1 >= 0 and check[x-1][y] == -1:
            check[x-1][y] = check[x][y] +1
            q.append([x-1,y])

bfs()

answer = check[s][1]

for i in range(1,s):

    if check[s][i] != -1:
        answer = min(answer,check[s][i])

print(answer)
