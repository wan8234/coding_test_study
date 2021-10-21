for tc in range(1, int(input())+1):

    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    k_value = [k**2 + (k-1)**2 for k in range(26)]

    house = list()

    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                house.append((i, j))


    result = 1 

    for k in range(2, n + 2):
        for r in range(n):
            for c in range(n):

                cnt = 0

                for y, x in house:
                    
                    if abs(r - y) + abs(c - x) < k:
                        cnt += 1

                if cnt > result and cnt * m >= k_value[k]:
                    result = cnt

    print('#{} {}'.format(tc, result))