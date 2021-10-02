import sys
input = sys.stdin.readline
inf = int(1e9)

count = 1

def triangle(graph):
    dp = [[inf]*3 for _ in range(n)]
    dp[0][1] = graph[0][1]
    dp[0][2] = dp[0][1] + graph[0][2]

    for x in range(1, n):
        for y in range(3):            
            if y == 0:
                dp[x][y] = min(dp[x - 1][y], dp[x - 1][y + 1]) + graph[x][y]
            elif y == 1:
                dp[x][y] = min(dp[x][y - 1], dp[x - 1][y - 1], dp[x - 1][y], dp[x - 1][y + 1]) + graph[x][y]
            else:
                dp[x][y] = min(dp[x][y - 1], dp[x - 1][y - 1], dp[x - 1][y]) + graph[x][y]
            if x == n - 1 and y == 1:
                break

    return dp[n - 1][1]

while True:
    n = int(input())
    if not n:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]    
    result = triangle(graph)
    
    print(str(count) + ". " + str(result))
    count += 1
            

# import sys
# input = sys.stdin.readline
# inf = int(1e9)

# dx = [0, 1, 1, 1] # right, right down, down, left down
# dy = [1, 1, 0, -1] # right, right down, down, left down
# count = 1

# def triangle(graph):
#     dp = [[inf]*3 for _ in range(n)]
#     dp[0][1] = graph[0][1]

#     for x in range(n):
#         for y in range(3):
#             if x == 0 and y == 0:
#                 continue
#             if x == n - 1 and y == 1:
#                 break

#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]

#                 if nx >= n or ny >= 3:
#                     continue
#                 else:
#                     value = graph[nx][ny]
#                     dp[nx][ny] = min(dp[nx][ny], dp[x][y] + value)
    
#     return dp[n - 1][1]

# while True:
#     n = int(input())
#     if not n:
#         break
#     graph = [list(map(int, input().split())) for _ in range(n)]    
#     result = triangle(graph)
    
#     print(str(count) + ". " + str(result))
#     count += 1
            

