t = int(input())

for case in range(1, 1 + t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    partner = []  # 만나는 원자들 저장

    for i in range(n - 1):
        x1, y1, d1, k1 = arr[i]
        for j in range(i + 1, n):
            x2, y2, d2, k2 = arr[j]

            # 충돌 가능성 확인
            if d1 == 0:  # 상
                # 하
                if d2 == 1 and x1 == x2 and y2 > y1:
                    partner.append((i, j, y2 - y1))
                # 직각,거리 같음
                elif (d2 == 3 and 0 < y2 - y1 == x1 - x2) or (d2 == 2 and 0 < y2 - y1 == x2 - x1):
                    partner.append((i, j, (y2 - y1) * 2))
            elif d1 == 1:  # 하
                if d2 == 0 and x1 == x2 and y1 > y2:
                    partner.append((i, j, y1 - y2))
                elif (d2 == 3 and 0 < y1 - y2 == x1 - x2) or (d2 == 2 and 0 < y1 - y2 == x2 - x1):
                    partner.append((i, j, (y1 - y2) * 2))
            elif d1 == 2:  # 좌
                if d2 == 3 and y1 == y2 and x1 > x2:
                    partner.append((i, j, x1 - x2))
                elif (d2 == 0 and 0 < x1 - x2 == y1 - y2) or (d2 == 1 and 0 < x1 - x2 == y2 - y1):
                    partner.append((i, j, (x1 - x2) * 2))
            elif d1 == 3:  # 우
                if d2 == 2 and y1 == y2 and x2 > x1:
                    partner.append((i, j, x2 - x1))
                elif (d2 == 0 and 0 < x2 - x1 == y1 - y2) or (d2 == 1 and 0 < x2 - x1 == y2 - y1):
                    partner.append((i, j, (x2 - x1) * 2))

    partner.sort(key=lambda a: a[2])  # 시간순 정렬
    val = 0
    crash = set()  #충돌 전
    crashed = []  # 충돌 후

    for i, j, time in partner:

        # 동시간대 끝나면 리셋
        if time > val:
            val = time
            crashed.extend(crash)
            crash = set()

        for atom in crashed:
            if atom == i or atom == j:
                break
        else:   # 충돌하지 않은 원자들만 충돌
            crash.add(i)
            crash.add(j)

    crashed.extend(crash)

    res = 0
    for i in crashed:
        res += arr[i][3]

    print(f'#{case} {res}')

