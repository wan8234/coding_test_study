import sys

t=int(sys.stdin.readline())

for case in range(t):

    n=int(sys.stdin.readline())
    
    parents=[0 for x in range(n+1)]

    for i in range(n-1):
        a,b=map(int, sys.stdin.readline().split())
        parents[b]=a

    target_a,target_b=map(int, sys.stdin.readline().split())

    a_parents=[target_a]
    b_parents=[target_b]

    while parents[target_a]:
        a_parents.append(parents[target_a])
        target_a = parents[target_a]

    while parents[target_b]:
        b_parents.append(parents[target_b])
        target_b = parents[target_b]
    
    for p in a_parents:
        if p in b_parents:
            print(p)
            break