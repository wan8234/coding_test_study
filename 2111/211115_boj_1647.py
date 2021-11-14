import sys
input = sys.stdin.readline

N, M = map(int, input().split())
routes = []

for _ in range(M):
    routes.append(list(map(int, input().split())))

routes.sort(key = lambda x : x[2])

parent = [i for i in range(N + 1)]
maximum = 0
answer = []

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

for f, s, w in routes:
    f_parent = find(f)
    s_parent = find(s)

    if f_parent != s_parent:
        if f_parent > s_parent:
            parent[f_parent] = s_parent
        else:
            parent[s_parent] = f_parent
        answer.append(w)
        
answer.pop()
print(sum(answer))