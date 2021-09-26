import sys
input = sys.stdin.readline

n = int(input())
planet = [i for i in range(n)]
data = []
edge = []
result = 0

def find(x):
    if x != planet[x]:
        planet[x] = find(planet[x])
    return planet[x] 

# def union_find(a, b):
#     a = find(a)
#     b = find(b)

#     if a > b:
#         planet[a] = b
#     else:
#         planet[b] = a

for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(n):
    for j in range(i + 1, n):
        edge.append((data[i][j], i, j))

edge.sort()

for cost, a, b in edge:
    a_root = find(a)
    b_root = find(b)

    if a_root != b_root:
        if a_root > b_root:
            planet[a_root] = b_root
        else:
            planet[b_root] = a_root
        result += cost
    
print(result)
