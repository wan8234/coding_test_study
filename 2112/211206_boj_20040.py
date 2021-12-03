import sys
input = sys.stdin.readline

def find_parent(x):
	if x != parent[x]:
		parent[x] = find_parent(parent[x])
		
	return parent[x]
	
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