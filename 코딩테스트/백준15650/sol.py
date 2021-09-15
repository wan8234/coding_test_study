import sys

input = sys.stdin.readline


n,m = map(int, input().split()) # 1~n으로 만든 수열 중 길이가 m

visited = [False for i in range(n+1)]
answer = list()

def dfs(depth):

    if depth == m:
        #print(*answer)
        return

    for i in range(1,n+1):

        if visited[i]:
            continue       

        visited[i]  = True
        answer.append(i)
        dfs(depth+1)
        answer.pop() #탐사내용 제거
        for j in range(i+1,n+1):
            visited[j] = False


dfs(0)