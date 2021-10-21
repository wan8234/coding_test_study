r, c, k = map(int, input().split())
matrix = []
for _ in range(3):
    line = list(map(int, input().split()))
    matrix.append(line)

def R():
    #행, 열 최소 3
    maxi = 3

    for mr in range(len(matrix)):
        x = matrix[mr]
        new = []
        #행 돌면서 new에 (숫자, 개수) 값 저장
        #이미 있으면 +1, 없으면 새로 append하기
        for y in x:
            for j in range(len(new)):
                nx, ny = new[j]
                if nx == y:
                    new[j] = (y, new[j][1] + 1)
                    break
            else:
                if y != 0:
                    new.append((y, 1))
        #개수 우선 오름차순 정렬
        new = sorted(new, key=lambda k: (k[1], k[0]))
        temp = []
        #matrix 행 값 바꿔주기
        for newx, newy in new:
            temp.append(newx)
            temp.append(newy)
        matrix[mr] = temp
        #행 길이 값 가장 큰 값 저장
        maxi = max(maxi, len(matrix[mr]))
    # 가장 큰 행 길이 값에 맞춰서 나머지 0으로 채워주기
    for x in matrix:
        while len(x) < maxi:
            x.append(0)

def myzip(x):
    new = []
    for i in range(len(x[0])):
        new.append([])
        for j in range(len(x)):
            new[-1].append(x[j][i])
    return new


#100번 돌면서 진행
for i in range(101):
    rlen = len(matrix)
    clen = len(matrix[0])
    #탈출 조건
    if rlen >= r and clen >= c and matrix[r-1][c-1] == k:
        print(i)
        break
    if rlen >= clen:
        R()
    else:
        matrix = myzip(matrix)
        R()
        matrix = myzip(matrix)
#100번 넘으면 -1
else:
    print(-1)