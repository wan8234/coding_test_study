import sys
input = sys.stdin.readline

T = int(input())

for case in range(T):
    N = int(input())
    parents = [0 for x in range(N+1)]

    for _ in range(N-1):
        a, b = map(int, input().split())
        parents[b] = a

    target_a,target_b = map(int, input().split())
    a_parents = [target_a]
    b_parents = [target_b]

    # 부모 탐색
    while parents[target_a]:
        a_parents.append(parents[target_a])
        target_a = parents[target_a]
    
    # 부모 탐색
    while parents[target_b]:
        b_parents.append(parents[target_b])
        target_b = parents[target_b]
    
    for res in a_parents:
        if res in b_parents:
            print(res)
            break
