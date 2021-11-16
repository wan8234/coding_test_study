import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    N = int(input())
    root = {}

    for _ in range(N - 1):
        a, b = map(int, input().split())
        
        root[b] = a

    nodes = list(map(int, input().split()))

    first_root = [nodes[0]]
    second_root = [nodes[1]]

    start = nodes[0]
    while True:
        if start in root:
            first_root.append(root[start])
        else:
            break

        start = root[start]

    start = nodes[1]
    while True:
        if start in root:
            second_root.append(root[start])
        else:
            break
        
        start = root[start]

    for i in first_root:
        if i in second_root:
            print(i)
            break