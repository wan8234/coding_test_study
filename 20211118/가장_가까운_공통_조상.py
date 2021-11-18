import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    parent = [0] * (N+1)
    for _ in range(N-1):
        x, y = map(int, input().split())
        #인덱스: 자식 / 값: 부모
        parent[y] = x
    A, B = map(int, input().split())

    pA, pB = [A], [B]

    #부모 계속 찾기
    while A != 0:
        pA.append(parent[A])
        A = parent[A]
    
    while B != 0:
        pB.append(parent[B])
        B = parent[B]

    b = False
    #부모 집합 돌면서 같으면 출력하고 break
    for x in pA:
        if b:
            break
        for y in pB:
            if x == y:
                print(x)
                b = True
                break
