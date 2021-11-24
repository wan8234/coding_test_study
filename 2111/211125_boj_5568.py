import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
cards = list(int(input()) for _ in range(N))
num = []
visit = [0] * N
s = set()

def dfs(count):
    if count == K:
        s.add(''.join(map(str, num)))
        return
    
    for i in range(N):
        if visit[i]:
            continue
            
        num.append(cards[i])
        visit[i] = 1
        dfs(count + 1)
        num.pop()
        visit[i] = 0

dfs(0)
print(len(s))