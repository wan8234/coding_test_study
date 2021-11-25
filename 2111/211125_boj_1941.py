import sys
input = sys.stdin.readline

seat = [input().rstrip() for _ in range(5)]
visit = [[0 for _ in range(5)] for _ in range(5)]
result = 0
group = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check(num):
    global connect
    x = num // 5
    y = num % 5

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5 and visit[nx][ny] == 0:
            next_num = nx * 5 + ny
            if next_num in group:
                visit[nx][ny] = 1
                connect += 1
                check(next_num)

def dfs(count, idx, y_num):
    global result
    global visit
    global connect

    if y_num >= 4 or 25 - idx < 7 - count:
        return
    
    if count == 7:
        connect = 1
        visit = [[0 for _ in range(5)] for _ in range(5)]
        cx, cy = group[0] // 5, group[0] % 5
        visit[cx][cy] = 1
        check(group[0])
        if connect == 7:
            result += 1

        return

    x = idx // 5
    y = idx % 5

    if seat[x][y] == "Y":
        group.append(idx)
        dfs(count + 1, idx + 1, y_num + 1)
        group.pop()
    else:
        group.append(idx)
        dfs(count + 1, idx + 1, y_num)
        group.pop()
    dfs(count, idx + 1, y_num)

dfs(0, 0, 0)
print(result)