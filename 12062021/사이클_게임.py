import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합 찾기
def find_parent(a):
    # 루트 노드가 아니면, 찾을때 까지 호출
    if a != parent[a]:
        parent[a] = find_parent(parent[a])
    return parent[a]


def union_find(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a == b:
        return
    elif a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [i for i in range(N)]


for i in range(M):
    a, b = map(int, input().split())
    if find_parent(a) == find_parent(b):
        print(i + 1)       
        break
    union_find(a, b)
else:
    print(0)
