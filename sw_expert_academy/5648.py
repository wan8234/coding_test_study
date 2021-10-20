# 원자들은 2차원 평면에서 이동
# 두 개 이상의 원자 충돌할 경우 각자 에너지 방출하고 소멸
# 상하좌우 움직임
# 1초에 1만큼 움직임

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def move(atom):
    global result
    count = 0

    for _ in range(4002):
        board = {}
        for x, y, direct, k in atom:
            x += dx[direct]
            y += dy[direct]

            if -2000 <= x <= 2000 and -2000 <= y <= 2000:
                if (x, y) in board:
                    board[(x, y)].append([x, y, direct, k])
                else:
                    board[(x, y)] = [[x, y, direct, k]]
            else:
                count += 1

        atom = []
        for b in board:
            if len(board[b]) == 1:
                atom.append(board[b][0])
            else:
                for a in board[b]:
                    result += a[3]
                    count += 1
        
        if count >= N - 1:
            return

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    result = 0
    atom = []

    for _ in range(N):
        y, x, direct, K = map(int, input().split())
        y *= 2
        x *= 2

        atom.append([x, y, direct, K])
    move(atom)
    
    print('#{} {}'.format(test_case, result))

#### TIME OVER (31 CORRECT) ####
# dx = [1, -1, 0, 0]
# dy = [0, 0, -1, 1]

# def move(atom):
#     global result

#     for _ in range(4002):
#         if len(atom) == 1:
#             return

#         for a in atom:
#             if a[3] != 0: 
#                 a[0] += dx[a[2]]
#                 a[1] += dy[a[2]]
#                 if not -2000 <= a[0] <= 2000 or not -2000 <= a[1] <= 2000:
#                     a[3] = 0

#         length = len(atom)

#         for i in range(length):
#             if not atom[i][3]:
#                 continue
#             for j in range(length):
#                 if i != j:
#                     if atom[j][3] and atom[i][0] == atom[j][0] and atom[i][1] == atom[j][1]:
#                         result += atom[i][3] + atom[j][3]
#                         atom[i][3] = 0
#                         atom[j][3] = 0
        
#         for i in range(length - 1, -1, -1):
#             if atom[i][3] == 0:
#                 atom.pop(i)

# T = int(input())

# for test_case in range(1, T + 1):
#     N = int(input())
#     result = 0
#     atom = []

#     for _ in range(N):
#         y, x, direct, K = map(int, input().split())
#         y *= 2
#         x *= 2

#         atom.append([x, y, direct, K])
#     move(atom)
    
#     print('#{} {}'.format(test_case, result))