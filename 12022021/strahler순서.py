from collections import deque

T = int(input())

for case in range(1, T+1):
    # 테케, 노드, 간선
    K, M, P = map(int, input().split())
    arr = [[] for _ in range(M + 1)]
    indegree = [0] * (M + 1)
    count = [[0, 0]] * (M + 1) # [값, 갯수]
    order = [0] * (M + 1)
    q = deque()

    for i in range(P):
        first, second = map(int, input().split())
        arr[first].append(second)
        indegree[second] += 1

    for i in range(1, M + 1):
        if indegree[i] == 0:
            count[i] = [1, 1]
            q.append(i)

    while q:
        tmp = q.popleft()

        if count[tmp][1] >= 2: # 개수를 비교해서 값을 갱신한다.
            order[tmp] = count[tmp][0] + 1
        else:
            order[tmp] = count[tmp][0]

        for second in arr[tmp]:
            indegree[second] -= 1
            # 같으면 개수를 증가
            if count[second][0] == order[tmp]:
                count[second][1] += 1
            # 더 크면 갱신
            elif count[second][0] < order[tmp]:
                count[second] = [order[tmp], 1]
            #0이 되면 처리 완료 -> q에 넣는다
            if indegree[second] == 0:
                q.append(second)

    print(case, max(order))
