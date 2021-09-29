import sys
input = sys.stdin.readline

n, m = map(int, input().split())

flag = [0] * n

def back(count, result):
    if count >= m:
        print(*result)
        return
    for i in range(n):
        if flag[i] == 1:
            continue
        flag[i] = 1
        result.append(i + 1)
        back(count + 1, result)
        flag[i] = 0
        result.pop()
back(0, [])