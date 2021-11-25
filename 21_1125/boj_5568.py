import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

card_list = list()
tmp_list = list()
res_list = list()
visited = [0]*n

for _ in range(n):
    card_list.append(int(input()))

def bt(depth,res_list):

    if depth == k:
        res_list.append(''.join(tmp_list))
        return

    for i in range(n):

        if visited[i] == 0:

            visited[i] = 1

            tmp_list.append(str(card_list[i]))
            bt(depth+1,res_list)
            
            visited[i] = 0
            tmp_list.pop()


bt(0,res_list)

res_list = list(set(res_list))

print(len(res_list))
