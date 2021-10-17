#### USING DFS(CORRECT) ####
import sys
input = sys.stdin.readline

n = int(input())
fee = [list(map(int, input().split())) for _ in range(n)]
visit = [0] * n

def dfs(start, next, cost, count):
    global answer
    if cost > answer: # reduce time
        return

    if count == n:
        if fee[next][start] != 0:
            cost += fee[next][start]
            answer = min(answer, cost)
        return

    for i in range(n):
        if fee[next][i] != 0 and i != start and visit[i] == 0:
            visit[i] = 1
            dfs(start, i, cost + fee[next][i], count + 1)
            visit[i] = 0

answer = int(1e9)

for i in range(n):
    visit[i] = 1
    dfs(i, i, 0, 1)
    visit[i] = 0

print(answer)


#### USING BITMASK(CORRECT) ####
# import sys
# input = sys.stdin.readline

# n = int(input())
# path = [list(map(int, input().split())) for _ in range(n)]
# dp = [[0] * (1 << n) for _ in range(n)]

# def find(now, before):
#     if dp[now][before]:
#         return dp[now][before]
    
#     if before == (1 << n) - 1:
#         return path[now][0] if path[now][0] > 0 else sys.maxsize
    
#     cost = sys.maxsize

#     for i in range(1, n):
#         if not (before >> i) % 2 and path[now][i]:
#             temp = find(i, before|(1 << i))
#             cost = min(cost, temp + path[now][i])

#     dp[now][before] = cost
#     return cost

# print(find(0, 1))


#### TIME OVER && FAIL ####
# import sys
# input = sys.stdin.readline

# n = int(input())
# fee = [list(map(int, input().split())) for _ in range(n)]

# visit = [0] * n
# answer = int(1e9)

# def travel(fee, visit, start, city, cost, count):
#     global answer
#     if count == n:
#         if fee[city][start] != 0:
#             cost += fee[city][start]
#             answer = min(cost, answer)
#         return

#     for i in range(n):
#         if visit[i] == 0:
#             visit[i] = 1
#             travel(fee, visit, start, i, cost + fee[city][i], count + 1)
#             visit[i] = 0

# for i in range(n):    
#     visit[i] = 1
#     for j in range(n):
#         if i != j:
#             travel(fee, visit, i, j, fee[i][j], 1)
#     visit[i] = 0

# print(answer)