# 충전기 위치 주어짐
# 거리 계산은 x좌표 뺀 값 + y좌표 뺀 값
# 지도는 가로,세로 10
# 사용자는 총 2명, A는 (1,1) B는 (10,10)에서 출발
# 사용자는 초기 0초 부터 충전 가능
# 같은 지역에선 충전기 공유(효율 반반)
# 겹칠 경우 한쪽 씩 쓰는게 유리한 경우 있음
# BC 정보는 X,Y좌표, 충전범위(C), 처리량(P)

dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]
 
def power(u):
    p = [0] * A
    for i in range(A):
        if abs(u[0] - ap[i][1] + 1) + abs(u[1] - ap[i][0] + 1) <= ap[i][2]:
            p[i] = ap[i][3]
    return p
 
def calculate(p1, p2):
    ret = 0
    if A == 1:
        return max(p1[0], p2[0])
 
    for i in range(A):
        for j in range(A):
            if i != j:
                ret = max(p1[i] + p2[j], ret)
    return ret
 
T = int(input())
for test_case in range(1, T + 1):
    M, A = map(int, input().split())
    ma = list(map(int, input().split()))
    mb = list(map(int, input().split()))
    ap = [list(map(int, input().split())) for _ in range(A)]
 
    ua = [0, 0]
    ub = [9, 9]
    result = 0
    result += calculate(power(ua), power(ub))
 
    for i in range(M):
        ua[0] += dx[ma[i]]
        ua[1] += dy[ma[i]]
        ub[0] += dx[mb[i]]
        ub[1] += dy[mb[i]]
        result += calculate(power(ua), power(ub))
 
    print('#{} {}'.format(test_case, result))

# dx = [0, -1, 0, 1, 0]
# dy = [0, 0, 1, 0, -1]

# def move(first, second):
#     global result
#     fx, fy = 0, 0
#     sx, sy = 9, 9

#     fbc = []
#     sbc = []

#     for data in BC:
#         if (fx, fy) in breadth[(data[0], data[1])]:
#             fbc.append(data)
#         if (sx, sy) in breadth[(data[0], data[1])]:
#             sbc.append(data)

#     temp = 0
#     if fbc != [] and sbc == []:
#         for f in fbc:
#             temp = max(temp, f[3])
#     elif fbc == [] and sbc != []:
#         for s in sbc:
#             temp = max(temp, s[3])
#     elif fbc == [] and sbc == []:
#         temp = 0
#     else:
#         for f in fbc:
#             for s in sbc:
#                 plus = f[3] + s[3]
#                 if f == s:
#                     plus //= 2
                    
#                 temp = max(temp, plus)

#     result += temp

#     for i in range(M):
#         fbc = []
#         sbc = []

#         fx = fx + dx[first[i]]
#         fy = fy + dy[first[i]]

#         sx = sx + dx[second[i]]
#         sy = sy + dy[second[i]]

#         for data in BC:
#             if (fx, fy) in breadth[(data[0], data[1])]:
#                 fbc.append(data)
#             if (sx, sy) in breadth[(data[0], data[1])]:
#                 sbc.append(data)

#         temp = 0
#         if fbc != [] and sbc == []:
#             for f in fbc:
#                 temp = max(temp, f[3])
#         elif fbc == [] and sbc != []:
#             for s in sbc:
#                 temp = max(temp, s[3])
#         elif fbc == [] and sbc == []:
#             temp = 0
#         else:
#             for f in fbc:
#                 for s in sbc:
#                     plus = f[3] + s[3]
#                     if f == s:
#                         plus //= 2
                    
#                     temp = max(temp, plus)

#         result += temp

# T = int(input())

# for test_case in range(1, T + 1):
#     result = 0
#     M, A = map(int, input().split())
#     BC = []
#     breadth = {}
#     table = [[0] * 10 for _ in range(10)]

#     first = list(map(int, input().split()))
#     second = list(map(int, input().split()))

#     for _ in range(A):
#         temp = list(map(int, input().split()))
#         temp[0], temp[1] = temp[1], temp[0]
#         temp[0] -= 1
#         temp[1] -= 1
#         BC.append(temp)

#     for i in range(10):
#         for j in range(10):
#             for data in BC:
#                 if abs(i - data[0]) + abs(j - data[1]) <= data[2]:
#                     if (data[0], data[1]) not in breadth:
#                         breadth[(data[0], data[1])] = []
#                     breadth[(data[0], data[1])].append((i, j))
    
#     move(first, second)

#     print('#{} {}'.format(test_case, result))

# 5
# 20 3
# 2 2 3 2 2 2 2 3 3 4 4 3 2 2 3 3 3 2 2 3
# 4 4 1 4 4 1 4 4 1 1 1 4 1 4 3 3 3 3 3 3
# 4 4 1 100
# 7 10 3 40
# 6 3 2 70
# 40 2
# 0 3 0 3 3 2 2 1 0 4 1 3 3 3 0 3 4 1 1 3 2 2 2 2 2 0 2 3 2 2 3 4 4 3 3 3 2 0 4 4 
# 0 1 0 3 4 0 4 0 0 1 1 1 0 1 4 4 4 4 4 3 3 3 0 1 0 4 3 2 1 4 4 3 2 3 2 2 0 4 2 1 
# 5 2 4 140
# 8 3 3 490
# 60 4
# 0 3 3 3 0 1 2 2 2 1 2 2 3 3 4 4 0 3 0 1 1 2 2 3 2 2 3 2 2 0 3 0 1 1 1 4 1 2 3 3 3 3 3 1 1 4 3 2 0 4 4 4 3 4 0 3 3 0 3 4 
# 1 1 4 1 1 1 1 1 1 4 4 1 2 2 3 2 4 0 0 0 4 3 3 4 3 3 0 1 0 4 3 0 4 3 2 3 2 1 2 2 3 4 0 2 2 1 0 0 1 3 3 1 4 4 3 0 1 1 1 1 
# 6 9 1 180
# 9 3 4 260
# 1 4 1 500
# 1 3 1 230
# 80 7
# 2 2 2 2 2 2 0 2 2 0 4 0 2 3 3 2 3 3 0 3 3 3 4 3 3 2 1 1 1 0 4 4 4 1 0 2 2 2 1 1 4 1 2 3 4 4 3 0 1 1 0 3 4 0 1 2 2 2 1 1 3 4 4 4 4 4 4 3 2 1 4 4 4 4 3 3 3 0 3 3 
# 4 4 1 1 2 1 2 3 3 3 4 4 4 4 4 1 1 1 1 1 1 1 1 0 3 3 2 0 4 0 1 3 3 3 2 2 1 0 3 2 3 4 1 0 1 2 2 3 2 0 4 0 3 4 1 1 0 0 3 2 0 0 4 3 3 4 0 4 4 4 4 0 3 0 1 1 4 4 3 0 
# 4 3 1 170
# 10 1 3 240
# 10 5 3 360
# 10 9 3 350
# 9 6 2 10
# 5 1 4 350
# 1 8 2 450
# 100 8
# 2 2 3 2 0 2 0 3 3 1 2 2 2 2 3 3 0 4 4 3 2 3 4 3 3 2 3 4 4 4 2 2 2 0 2 2 4 4 4 4 1 1 1 2 2 2 4 3 0 2 3 3 4 0 0 1 1 4 1 1 1 1 2 2 1 1 3 3 3 0 3 2 3 3 0 1 3 3 0 1 1 3 3 4 0 4 1 1 2 2 4 0 4 1 1 2 2 1 1 1 
# 4 4 4 0 4 1 1 4 1 1 1 1 3 2 1 2 1 1 4 4 1 0 2 3 4 4 4 4 4 0 1 0 2 2 2 0 2 2 2 2 2 2 3 0 0 1 4 3 3 2 0 0 4 4 4 0 2 0 4 1 1 2 2 0 4 4 0 0 2 0 2 3 3 0 2 3 0 3 4 0 4 3 4 4 3 4 1 1 2 2 2 0 0 1 0 4 1 1 1 4 
# 3 4 2 340
# 10 1 1 430
# 3 10 4 10
# 6 3 4 400
# 7 4 1 80
# 4 5 1 420
# 4 1 2 350
# 8 4 4 300
