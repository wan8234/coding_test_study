from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

time = [-1] * 100001
count = [0] * 100001

def bfs():    
    global time
    global count

    queue = deque()
    queue.append(N)

    time[N] = 0
    count[N] = 1

    while queue:
        pos = queue.popleft()
        for new_pos in [pos - 1, pos + 1, pos * 2]:
            if 0 <= new_pos < 100001:
                if time[new_pos] == -1:
                    time[new_pos] = time[pos] + 1
                    count[new_pos] = count[pos]
                    queue.append(new_pos)
                elif time[new_pos] == time[pos] + 1:
                    count[new_pos] += count[pos]
    
bfs()

print(time[K])
print(count[K])

#### MEMORY OVER ####
# from collections import deque
# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())

# time = abs(N - K)
# count = 0

# def bfs():
#     global time
#     global count

#     queue = deque()
#     queue.append([N, 0])

#     while queue:
#         distance, move = queue.popleft()
#         if move > time:
#             continue

#         if distance == K:
#             if move == time:
#                 count += 1                
#             elif move < time:
#                 time = move
#                 count = 1
#             continue

#         queue.append([distance + 1, move + 1])
#         if distance - 1 >= 0:
#             queue.append([distance - 1, move + 1])
#         if distance != 0:
#             queue.append([distance * 2, move + 1])
# bfs()

# print(time)
# print(count)
