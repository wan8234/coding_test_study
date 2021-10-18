import sys
input = sys.stdin.readline

N, M = map(int, input().split())

chicken = []
house = []

#
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 1:
            house.append((i, j))
        elif line[j] == 2:
            chicken.append((i, j))


answer = int(1e9)
def dfs(x, chosen):
    global answer
    #치킨집 M개 선택
    if len(chosen) == M:
        total = 0
        #집 각각에서 가장 가까운 치킨집과의 거리 mini
        for hx, hy in house:
            mini = 100
            for x, y in chosen:
                dis = abs(x-hx) + abs(y-hy)
                if dis < mini:
                    mini = dis
            total += mini
        if total < answer:
            answer = total
        return
    if x >= len(chicken):
        return
    else:
        chosen.append(chicken[x])
        dfs(x+1, chosen)
        chosen.pop()
        dfs(x+1, chosen)

dfs(0, [])

print(answer)