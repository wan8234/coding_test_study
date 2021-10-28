import sys
input = sys.stdin.readline

N, L = map(int, input().split())

alp = list(map(str, input().split()))
alp = sorted(alp)
aeiou = ['a', 'e', 'i', 'o', 'u']

password = []

def dfs(temp, i):
    if len(temp) == N:
        cnt = 0
        for x in temp:
            if x in aeiou:
                cnt += 1
        if 1 <= cnt <= N - 2:
            print(''.join(temp))
        return
    
    if i == L:
        return

    temp.append(alp[i])
    dfs(temp, i+1)
    temp.pop()
    dfs(temp, i+1)

dfs([], 0)