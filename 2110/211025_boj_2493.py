import sys
input = sys.stdin.readline

N = int(input())
tower = list(map(int, input().split()))
stack = []
answer = [0] * N

for i in range(N):
    while stack:
        if stack[-1][1] > tower[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, tower[i]])

print(*answer)

# import sys
# input = sys.stdin.readline

# N = int(input())
# tower = list(map(int, input().split()))
# answer = [0] * N

# pivot = tower[-1]
# before = tower[-1]
# count = 1
# for i in range(N - 2, -1, -1):
#     if tower[i] < pivot:
#         count += 1
#     else:
#         for j in range(i + 1, i + 1 + count):
#             answer[j] = i + 1
#         count = 1
#         pivot = tower[i]

# print(*answer)