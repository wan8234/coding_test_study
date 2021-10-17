# 세로방향 셀 K개 이상 이어야 검사 통과
# 약품 투여 시 가로줄 모두 변함
# 두께 D, 가로크기 W, 합격기준 K

def check(cells, D, W, K):
    for j in range(W):
        count = 1
        before = cells[0][j]
        for i in range(1, D):
            if before == cells[i][j]:
                count += 1
            else:
                count = 1
                before = cells[i][j]

            if count >= K:
                break
        else:
            return False
    return True

def inject(cells, D, W, K, current, count):
    global result
    if current == D:
        temp = check(cells, D, W, K)
        if temp:            
            result = min(result, count)        
        return

    if count >= result:
        return

    temp_row = cells[current]

    cells[current] = [0] * W    
    inject(cells, D, W, K, current + 1, count + 1)

    cells[current] = [1] * W
    inject(cells, D, W, K, current + 1, count + 1)

    cells[current] = temp_row
    inject(cells, D, W, K, current + 1, count)


T = int(input())

for test_case in range(1, T + 1):
    D, W, K = map(int, input().split())
    cells = []
    result = int(1e9)
    for _ in range(D):
        cells.append(list(map(int, input().split())))
    
    if K == 1:
        result = 0
        print('#{} {}'.format(test_case, result))
        continue

    value = check(cells, D, W, K)

    if not value:
        inject(cells, D, W, K, 0, 0)
    else:
        result = 0

    print('#{} {}'.format(test_case, result))

# 10
# 6 8 3
# 0 0 1 0 1 0 0 1
# 0 1 0 0 0 1 1 1
# 0 1 1 1 0 0 0 0
# 1 1 1 1 0 0 0 1
# 0 1 1 0 1 0 0 1
# 1 0 1 0 1 1 0 1
# 6 8 3
# 1 1 1 1 0 0 1 0
# 0 0 1 1 0 1 0 1
# 1 1 1 1 0 0 1 0
# 1 1 1 0 0 1 1 0
# 1 1 0 1 1 1 1 0
# 1 1 1 0 0 1 1 0
# 6 8 4
# 1 1 0 0 0 1 1 0
# 1 0 1 0 0 1 1 1
# 0 1 0 0 1 1 0 0
# 1 0 1 0 0 0 0 0
# 1 1 0 0 0 0 0 0
# 1 0 0 0 1 1 1 1
# 6 4 4
# 1 1 0 0
# 0 1 0 1
# 0 0 0 1
# 1 1 1 1
# 1 1 0 1
# 1 0 1 0
# 6 10 3
# 0 1 0 0 0 1 0 0 1 1
# 0 1 1 0 0 1 0 0 1 0
# 0 1 0 0 1 0 1 1 1 1
# 0 0 0 0 0 1 1 1 1 0
# 0 1 0 0 1 1 1 1 1 1
# 1 0 0 0 1 1 0 0 1 1
# 6 6 5
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 6 6 4
# 1 1 1 1 1 1
# 0 0 0 0 0 1
# 0 1 1 1 0 1
# 0 1 0 1 0 1
# 0 1 0 0 0 1
# 0 1 1 1 1 1
# 8 15 3
# 0 1 1 0 0 1 1 0 1 1 0 0 0 0 0
# 1 0 0 0 1 1 0 0 0 0 0 1 0 1 1
# 1 1 0 1 0 1 0 1 0 1 0 1 0 0 0
# 0 1 1 1 0 0 1 0 0 0 0 1 0 0 0
# 0 0 0 0 0 0 1 0 0 0 1 1 0 0 1
# 1 0 1 0 0 1 0 1 1 1 1 0 1 1 1
# 0 0 0 0 0 1 1 1 0 0 0 0 0 1 0
# 0 0 1 0 1 1 0 1 1 0 0 0 1 0 0
# 10 20 4
# 1 0 1 1 1 1 1 1 1 1 0 0 1 1 1 0 1 1 0 1
# 1 1 0 1 1 1 0 0 1 0 0 0 1 1 1 1 0 0 1 0
# 1 1 0 1 1 0 0 0 1 1 1 1 1 0 0 1 1 0 1 0
# 0 0 0 1 1 0 0 0 0 1 0 0 1 0 1 1 1 0 1 0
# 0 1 1 0 1 0 1 0 1 0 0 1 0 0 0 0 1 1 1 1
# 1 0 1 0 1 0 1 1 0 0 0 0 1 1 1 0 0 0 0 0
# 0 1 0 0 1 1 0 0 0 0 0 1 1 0 0 1 1 0 1 1
# 1 0 0 0 0 1 0 1 1 0 1 1 0 1 0 0 1 1 1 0
# 0 1 1 0 0 1 0 1 0 0 0 0 0 0 0 1 1 1 0 1
# 0 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 0 0 1 0
# 13 20 5
# 1 1 0 1 0 0 0 1 1 1 1 0 0 0 1 1 1 0 0 0
# 1 1 1 1 0 1 0 1 0 0 0 0 1 0 0 0 0 1 0 0
# 1 0 1 0 1 1 0 1 0 1 1 0 0 0 0 1 1 0 1 0
# 0 0 1 1 0 1 1 0 1 0 0 1 1 0 0 0 1 1 1 1
# 0 0 1 0 0 1 0 0 1 0 0 0 0 1 0 0 0 0 1 1
# 0 0 1 0 0 0 0 0 0 0 0 0 1 1 1 0 0 1 0 1
# 0 0 0 1 0 0 0 0 0 0 1 1 0 0 0 1 0 0 1 0
# 1 1 1 0 0 0 1 0 0 1 1 1 0 1 0 1 0 0 1 1
# 0 1 1 1 1 0 0 0 1 1 0 1 0 0 0 0 1 0 0 1
# 0 0 0 0 1 0 1 0 0 0 1 0 0 0 0 1 1 1 1 1
# 0 1 0 0 1 1 0 0 1 0 0 0 0 1 0 1 0 0 1 0
# 0 0 1 1 0 0 1 0 0 0 1 0 1 1 0 1 1 1 0 0
# 0 0 0 1 0 0 1 0 0 0 1 0 1 1 0 0 1 0 1 0
