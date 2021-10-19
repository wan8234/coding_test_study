# 아래층으로 최대한 빨리 내려가야함
# P는 사람, S는 계단 입구
# 이동 완료 시간은 모든 사람들이 내려간 시간(계단 내려가는 시간 포함)
# 이동시간 = 거리 계산
# 계단 내려가는 시간 - 1분 후 아래칸 내려갈 수 있음, 최대 동시 3명
# 초과할 경우 한명이 다 내려갈때까지 대기, 계단마다 K 길이(시간)
# 이동 완료가 최소 되는 경우 찾기

def down(on_stair, stair_num):
    count, wait = 0, 0
    now = []

    while on_stair or wait or now:
        while wait:
            if len(now) == 3:
                break
            now.append(stair_num[2])
            wait -= 1
        
        for i in range(len(on_stair) - 1, -1, -1):
            on_stair[i] -= 1
            if on_stair[i] <= 0:
                on_stair.pop(i)
                wait += 1
        for i in range(len(now) - 1, -1, -1):
            now[i] -= 1
            if now[i] <= 0:
                now.pop(i)
        count += 1
    return count

def move(idx):
    global result

    if idx == len(people):
        stair1, stair2 = [], []
        for i in range(len(people)):
            if visited[i] == 1:
                stair1.append(dist1[i])
            elif visited[i] == 2:
                stair2.append(dist2[i])
        
        temp = max(down(stair1, stairs[0]), down(stair2, stairs[1]))
        result = min(result, temp + 1)
        return

    visited[idx] = 1
    move(idx + 1)
    visited[idx] = 2
    move(idx + 1)
    visited[idx] = 0

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    result = int(1e9)
    people = []
    stairs = []
    room = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if room[i][j] == 1:
                people.append([i, j])
            elif room[i][j] > 1:
                stairs.append([i, j, room[i][j]])

    dist1, dist2 = [0] * len(people), [0] * len(people)

    for i in range(len(people)):
        px, py = people[i]
        dist1[i] = abs(px - stairs[0][0]) + abs(py - stairs[0][1])
        dist2[i] = abs(px - stairs[1][0]) + abs(py - stairs[1][1])
    
    visited = [0] * len(people)
    move(0)

    print('#{} {}'.format(test_case, result))


#### TEST CASE 49 CORRECT ####
# import copy

# def move(people, stairs, index, queue):
#     if index == len(people):
#         check(stairs, queue)
        
#         return

#     length = len(stairs)
#     px, py = people[index]

#     for i in range(length):
#         sx, sy = stairs[i]
#         distance = abs(sx - px) + abs(sy - py)

#         queue.append([distance, i])
#         temp = copy.deepcopy(queue)
#         move(people, stairs, index + 1, queue)
#         queue = temp
#         queue.pop()

# def check(stairs, queue):
#     global result
#     count = 0
#     length = len(stairs)
#     waiting = [[] for _ in range(length)]    

#     while True:
#         if not queue and waiting == [[] for _ in range(length)]:
#             result = min(result, count)
#             break
#         temp = []
#         count += 1

#         if count > result:
#             return

#         for q in queue:
#             remain_distance, stair_index = q
#             if remain_distance > 0:
#                 q[0] -= 1
#                 temp.append(q)
#             elif remain_distance == 0:
#                 if len(waiting[stair_index]) < 3:
#                     waiting[stair_index].append(room[stairs[stair_index][0]][stairs[stair_index][1]] + 1)
#                 elif len(waiting[stair_index]) >= 3 and 1 in waiting[stair_index]:
#                     waiting[stair_index].append(room[stairs[stair_index][0]][stairs[stair_index][1]] + 1)
#                 else:
#                     temp.append(q)
        
#         new_temp = []
#         for wait in waiting:
#             wait_temp = []
#             for w in wait:
#                 if w - 1 > 0:
#                     wait_temp.append(w - 1)
#             new_temp.append(wait_temp)
        
#         queue = temp
#         waiting = new_temp

# T = int(input())

# for test_case in range(1, T + 1):
#     N = int(input())
#     result = int(1e9)
#     people = []
#     stairs = []
#     room = [list(map(int, input().split())) for _ in range(N)]

#     for i in range(N):
#         for j in range(N):
#             if room[i][j] == 1:
#                 people.append([i, j])
#             elif room[i][j] > 1:
#                 stairs.append([i, j])

#     move(people, stairs, 0, [])

#     print('#{} {}'.format(test_case, result))

# 10
# 5
# 0 1 1 0 0
# 0 0 1 0 3
# 0 1 0 1 0
# 0 0 0 0 0
# 1 0 5 0 0
# 5
# 0 0 1 1 0
# 0 0 1 0 2
# 0 0 0 1 0
# 0 1 0 0 0
# 1 0 5 0 0
# 6
# 0 0 0 1 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 1 0 0 0 0
# 2 0 1 0 0 0
# 0 0 2 0 0 0
# 6
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 1 0 0 0 0 0
# 0 0 0 2 0 4
# 7
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 4
# 0 0 0 0 1 0 0
# 1 0 0 1 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 2 0 0 0 0 0
# 7
# 0 0 0 0 0 0 0
# 7 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 2 0 0 0 0 1 0
# 0 0 0 0 0 0 0
# 8
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 2
# 0 0 0 0 0 0 0 0
# 2 0 0 0 0 0 0 0
# 0 0 0 0 0 1 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 1 0
# 0 0 0 0 1 0 0 0
# 8
# 3 0 0 0 0 0 5 0
# 0 0 0 0 0 0 0 0
# 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 1 0 1 1 0 0 0 0
# 0 0 0 0 0 0 1 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 9
# 0 0 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 8
# 7 0 0 0 0 1 0 0 0
# 0 0 0 0 0 1 1 0 0
# 0 0 0 0 0 0 0 0 0
# 1 0 0 0 0 1 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 10
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 1 0 0 0 0 0
# 0 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 3 0 1 0 1 0 0 0 0 2
# 1 1 0 0 1 0 1 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0