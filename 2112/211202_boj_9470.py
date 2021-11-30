from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(1, T + 1):
    K, M, P = map(int, input().split())
    tree = [[] for _ in range(M + 1)]
    come = [0] * (M + 1)
    strahler = [[] for _ in range(M + 1)]
    answer = 1

    for _ in range(P):
        a, b = map(int, input().split())
        tree[a].append(b)
        come[b] += 1
        
    queue = deque()

    for i in range(1, M + 1):
        if come[i] == 0:
            queue.append(i)
            strahler[i].append(1)

    while queue:
        current = queue.popleft()
        
        for value in tree[current]:
            come[value] -= 1
            strahler[value].append(strahler[current][0])

            if come[value] == 0:
                temp = list(set(strahler[value]))
                maximum = max(temp)
                
                if strahler[value].count(maximum) > 1:
                    strahler[value] = [maximum + 1]
                else:
                    strahler[value] = [maximum]

                answer = max(answer, strahler[value][0])
                queue.append(value)

    print(test_case, answer)
