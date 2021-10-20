# 경사로 설치해서 활주로 이어지도록
# 경사로는 길이 x, 높이 1
# 지형 높이 차이가 1이어야함
# 높아졌다 낮아졌다 할 수 있음
# 낮은 지형의 높이가 경사로의 길이만큼 동일하게 연속되어야함
# 경사로가 지형 벗어나면 안됨
# 경사로는 겹칠 수 없음

def check(row):
    cnt = 1
    for i in range(1, N):
        if row[i] == row[i - 1]:
            cnt += 1
        elif row[i] - row[i - 1] == 1 and cnt >= X:
            cnt = 1
        elif row[i - 1] - row[i] == 1 and cnt >= 0:
            cnt = -X + 1
        else:
            return 0
    if cnt >= 0:
        return 1
    return 0

T = int(input())

for test_case in range(1, T + 1):
    result = 0
    N, X = map(int, input().split())
    land = []

    for i in range(N):
        land.append(list(map(int, input().split())))
        result += check(land[i])


    for i in range(N):
        for j in range(N):
            if i < j:
                land[i][j], land[j][i] = land[j][i], land[i][j]                
        result += check(land[i])

    print('#{} {}'.format(test_case, result))
    

#### CORRECT BUT COMPLICATED ####
# def build(land):
#     global result

#     for x in range(N):
#         before = land[x][0]
#         over_count = 0
#         under_count = 0
#         flag = 0
#         temp = [0] * N

#         for y in range(1, N):
#             if land[x][y] == before:
#                 if over_count != 0:
#                     over_count -= 1
#                 elif under_count != 0:
#                     under_count -= 1 
#                 continue
#             elif land[x][y] < before and abs(land[x][y] - before) == 1:
#                 if over_count != 0:
#                     break
#                 if y + X - 1 >= N:
#                     break
                
#                 under_count = 0
#                 over_count = X - 1
#                 before = land[x][y]

#                 for i in range(X):
#                     if land[x][y + i] != before or temp[y + i] != 0:
#                         flag = 1
#                         break
#                 if flag == 1:
#                     break

#                 for i in range(X):
#                     temp[y + i] = 1

#             elif land[x][y] > before and abs(land[x][y] - before) == 1:
#                 if over_count != 0 or under_count != 0:
#                     break
#                 if y - X < 0:
#                     break

#                 for i in range(1, X + 1):
#                     if land[x][y - i] != before or temp[y - i] != 0:
#                         flag = 1
#                         break
#                 if flag == 1:
#                     break

#                 for i in range(1, X + 1):
#                     temp[y - i] = 1

#                 under_count = X - 1
#                 before = land[x][y]

#             else:
#                 break
#         else:
#             result += 1

# T = int(input())

# for test_case in range(1, T + 1):
#     result = 0
#     N, X = map(int, input().split())
#     land = [list(map(int, input().split())) for _ in range(N)]

#     build(land)

#     for i in range(N):
#         for j in range(N):
#             if i < j:
#                 land[i][j], land[j][i] = land[j][i], land[i][j]

#     build(land)

#     print('#{} {}'.format(test_case, result))

# 10
# 6 2
# 3 3 3 2 1 1
# 3 3 3 2 2 1
# 3 3 3 3 3 2
# 2 2 3 2 2 2
# 2 2 3 2 2 2
# 2 2 2 2 2 2
# 6 4
# 3 2 2 2 1 2 
# 3 2 2 2 1 2 
# 3 3 3 3 2 2 
# 3 3 3 3 2 2 
# 3 2 2 2 2 2 
# 3 2 2 2 2 2 
# 7 2
# 1 1 1 1 2 1 1 
# 1 1 1 2 2 2 1 
# 2 2 2 2 2 2 2 
# 2 2 2 2 2 2 2 
# 2 2 2 2 2 2 2 
# 2 2 2 2 2 2 2 
# 2 2 2 2 2 2 2 
# 8 3
# 2 2 2 3 3 4 2 2 
# 2 2 2 3 3 4 2 2 
# 2 2 2 2 2 2 2 2 
# 2 2 2 2 2 2 2 2 
# 2 2 2 2 1 1 2 2 
# 2 1 1 1 1 1 1 1 
# 2 1 1 1 1 1 1 1 
# 2 1 1 1 1 1 1 1 
# 8 4
# 1 1 1 1 1 1 1 1 
# 1 1 1 1 1 1 1 1 
# 1 1 1 1 1 1 1 1 
# 2 1 1 1 1 1 1 1 
# 2 1 1 1 1 1 1 1 
# 2 1 1 1 1 1 1 1 
# 1 1 1 1 1 1 1 2 
# 1 1 1 1 1 1 1 2 
# 9 4
# 4 4 3 3 3 3 2 2 2 
# 4 4 3 3 1 1 2 2 3 
# 3 3 2 2 1 1 1 1 2 
# 1 1 1 1 1 1 1 1 1 
# 1 1 1 1 1 1 1 1 1 
# 2 2 1 1 1 1 1 1 1 
# 2 2 1 1 1 1 1 1 1 
# 2 2 2 2 2 2 1 1 1 
# 3 3 3 3 2 2 2 2 1 
# 10 2
# 2 2 3 5 3 1 1 1 1 1 
# 2 2 3 5 3 1 1 1 1 1 
# 3 3 4 5 4 3 2 1 1 2 
# 3 3 4 5 4 3 2 1 1 2 
# 5 5 5 5 5 5 3 1 1 3 
# 4 4 4 5 5 5 4 3 3 3 
# 4 4 4 5 5 5 5 5 5 3 
# 4 4 4 4 4 5 5 5 5 3 
# 4 4 4 4 4 5 5 5 5 3 
# 5 5 4 4 4 5 5 5 5 4 
# 12 4
# 4 4 4 5 5 4 4 4 4 4 4 4 
# 5 5 5 5 5 5 5 5 5 5 5 4 
# 4 4 4 5 5 4 4 4 5 5 5 4 
# 3 3 4 5 5 4 3 4 5 5 5 4 
# 3 3 4 5 5 4 3 4 5 5 5 4 
# 2 2 3 4 4 4 4 4 4 4 4 5 
# 2 2 3 4 4 4 4 4 4 4 4 5 
# 2 2 3 3 3 4 5 3 2 2 4 4 
# 3 3 3 4 4 4 5 4 3 3 4 4 
# 3 3 4 5 5 5 5 5 5 5 5 4 
# 3 3 4 5 5 5 5 5 5 5 5 4 
# 4 4 4 4 4 4 5 5 5 5 5 4 
# 15 3
# 5 4 4 3 3 3 2 2 2 3 4 4 4 4 4 
# 5 4 4 3 3 3 2 2 2 3 4 4 4 4 4 
# 5 5 5 5 4 4 2 2 3 4 4 4 4 4 5 
# 5 4 4 3 3 3 2 2 3 4 4 4 4 4 4 
# 5 3 3 1 2 2 3 3 3 4 4 4 4 4 4 
# 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 
# 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 
# 2 3 3 4 3 3 3 3 3 3 3 4 4 4 3 
# 2 3 3 4 3 3 3 3 3 3 3 4 4 4 3 
# 3 4 4 4 4 4 3 3 3 3 3 3 4 4 4 
# 5 5 5 4 4 4 4 4 3 3 3 3 4 4 5 
# 5 5 5 4 4 4 4 4 3 3 3 3 4 4 5 
# 5 5 5 5 4 4 4 4 3 3 2 2 3 3 4 
# 5 5 5 5 5 5 4 4 3 3 2 1 2 2 3 
# 5 5 5 5 5 5 4 4 3 3 2 1 2 2 3 
# 20 3
# 3 3 3 2 2 2 2 3 3 3 4 4 4 4 4 4 5 5 5 5 
# 3 3 3 2 2 2 2 3 3 3 4 4 4 4 4 4 5 5 5 5 
# 5 3 3 2 2 2 2 2 3 3 4 4 4 4 5 5 5 5 5 5 
# 4 3 3 1 1 1 1 1 2 3 4 4 4 5 5 5 5 5 5 5 
# 4 2 2 1 1 1 1 1 2 3 4 5 5 5 5 5 5 5 5 5 
# 4 3 3 2 2 2 2 1 2 3 4 5 5 5 5 5 5 5 5 5 
# 4 4 4 4 4 3 3 2 3 4 5 5 5 5 5 5 5 5 5 5 
# 4 3 3 3 3 3 3 3 4 4 4 5 5 5 5 5 5 4 4 4 
# 4 3 3 3 3 3 3 3 4 4 4 5 5 5 5 5 5 4 4 4 
# 4 3 3 3 3 4 4 4 4 4 5 5 5 5 5 5 5 5 5 5 
# 3 3 3 3 3 4 4 4 4 4 5 5 5 5 5 5 5 5 5 5 
# 3 3 3 3 3 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 
# 3 3 3 3 4 4 4 4 5 5 5 5 5 5 5 5 5 5 5 5 
# 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5 5 4 4 4 
# 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5 5 4 4 4 
# 5 5 5 5 5 5 5 5 5 5 5 5 4 4 4 4 4 4 4 4 
# 5 5 5 5 5 5 5 5 5 5 5 5 3 3 3 3 4 4 4 4 
# 5 5 5 5 5 5 5 5 5 5 5 5 3 3 2 2 3 3 4 4 
# 5 5 5 5 5 5 5 5 5 5 5 5 3 3 2 2 3 3 4 4 
# 5 5 5 5 5 5 5 5 4 4 4 4 3 3 3 3 4 4 4 4 
