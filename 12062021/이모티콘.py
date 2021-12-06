# 복사 붙여넣기 삭제
from collections import deque

N = int(input())
time = [[-1]*(N+1) for _ in range(N+1)]

q = deque()
q.append((1,0)) # 화면, 클립보드
time[1][0] = 0
res = 100

while q:
    s, c = q.popleft()  #screen, clipboard
    # 복사
    if time[s][s] == -1:
        time[s][s] = time[s][c] + 1
        q.append((s,s))
    # 붙여넣기
    if s+c <= N and time[s+c][c] == -1:
        time[s+c][c] = time[s][c] + 1
        q.append((s+c, c))
    # 삭제
    if s-1 >= 0 and time[s-1][c] == -1:
        time[s-1][c] = time[s][c] + 1
        q.append((s-1,c))

for i in range(N+1):
    if time[N][i] != -1:
        res = min(res, time[N][i])

print(res)
