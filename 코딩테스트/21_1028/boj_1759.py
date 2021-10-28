import sys

input = sys.stdin.readline


L, C = map(int, input().split())

pws = input().split()

v_list = ['a', 'e', 'i', 'o', 'u']
check = [0 for i in range(C)]

arr = []
pws.sort()

def dfs(len, idx):

    if len == L:
        vo = 0
        co = 0
        for i in range(L):

            if arr[i] in v_list: 
                vo += 1
            else: 
                co += 1
        if vo >= 1 and co >= 2:
            print(''.join(arr))
        return

    for i in range(idx, C):

        if check[i] == 0:

            arr.append(pws[i])

            check[i] = 1
            dfs(len + 1, i + 1)
            check[i] = 0

            arr.pop(-1)

dfs(0, 0)