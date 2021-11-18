from collections import deque
import sys
input = sys.stdin.readline

k = int(input())

def bfs(start):
    arr[start] = 1
    q = deque()
    q.append(start)

    while q:
        a = q.popleft()
        for i in s[a]:
            if arr[i] == 0:
                arr[i] = -arr[a]
                q.append(i)
            else:
                if arr[i] == arr[a]:
                    return False
    return True

for case in range(k):
    v, e = map(int, input().split())
    isCorrect = True
    s = [[] for i in range(v + 1)]
    arr = [0 for i in range(v + 1)]
    for j in range(e):
        a, b = map(int, input().split())
        s[a].append(b)
        s[b].append(a)
    for y in range(1, v + 1):
        if arr[y] == 0:
            if not bfs(y):
                isCorrect = False
                break
    if isCorrect:
        print("YES")
    else:
        print("NO")
