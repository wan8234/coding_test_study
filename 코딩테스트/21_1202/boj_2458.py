import sys

input = sys.stdin.readline

N, M = map(int, input().split())
key_list = [[0]*N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    key_list[a-1][b-1] = 1

for k in range(N):
    for a in range(N):
        for b in range(N):
            if key_list[a][k] == 1 and key_list[k][b] == 1:
                key_list[a][b] = 1
res = 0
for i in range(N):
    t = 0
    for j in range(N):
        t += key_list[i][j] + key_list[j][i]
    if t == N-1:
        res += 1
        
print(res)