import sys

input = sys.stdin.readline

graph = []
answer = []
count = 0

while True:

    n = int(input())
    m = 3

    graph.clear()

    if n != 0:

        graph = [list(map(int,input().split())) for _ in range(n)]

        dp = [[0]*m for _ in range(n)]

        dp[1][0] = graph[1][0] + graph[0][1]
        dp[1][1] = graph[1][1] + min(dp[1][0], graph[0][1], graph[0][2] + graph[0][1])
        dp[1][2] = graph[1][2] + min(dp[1][1], graph[0][1], graph[0][1] + graph[0][2])


        for x in range(2,n):
            for y in range(m):
                if y == 0:
                    dp[x][y] = graph[x][y] + min(dp[x-1][y], dp[x-1][y + 1])
                elif y == 1:
                    dp[x][y] = graph[x][y] + min(dp[x-1][y-1], dp[x-1][y], dp[x-1][y+1], dp[x][y-1])
                else:
                    dp[x][y] = graph[x][y] + min(dp[x-1][y-1], dp[x-1][y], dp[x][y-1])

        
        count += 1
        print(str(count)+'. '+str(dp[n-1][1]))
        
    else:
        break
