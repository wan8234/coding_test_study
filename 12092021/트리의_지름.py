import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N-1):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])
    graph[b].append([a, w])


def dfs(x):
    for i in graph[x]:
        a, w = i
        if d[a] == -1:
            d[a] = d[x] + w
            dfs(a)


d = [-1] * (N+1)
d[1] = 0

#제일 긴 길이 찾기
dfs(1)
#시작점 찾기
start = d.index(max(d))
#d 초기화
d = [-1] * (N +1)
d[start] = 0
#지름 찾기
dfs(start)

answer = max(d)

print(answer)

