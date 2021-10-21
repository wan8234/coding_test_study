T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    house = []
    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(N):
            if line[j] == 1:
                house.append((i, j))


    #k가 1인 경우 최대 집 1개
    result = 1
    #k 개수 별로
    for k in range(2, N+2):
        # 집이 모두 선택되었을 때의 이득보다 비용이 크면 중단
        if k**2 + (k-1)**2 > M * len(house):
            break
        for r in range(N):
            for c in range(N):
                #r, c : 마름모의 중앙
                cnt = 0
                for x, y in house:
                    dis = abs(r-x) + abs(c-y)
                    # (r, c)에서 집까지의 거리가 k보다 작으면
                    if dis < k:
                        cnt += 1
                # 비용 계산, 비용이 수입보다 큰 경우
                if result < cnt and k**2 + (k-1)**2 <= cnt * M:
                    result = cnt

    print('#', t, " ", result, sep="")
