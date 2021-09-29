import sys
input = sys.stdin.readline

n = int(input())
weight = list(map(int, input().split()))

weight.sort()
num = 1

for w in weight:
    if num < w:
        break
    num += w
print(num)

# import sys
# input = sys.stdin.readline

# n = int(input())
# weight = list(map(int, input().split()))

# weight.sort(reverse = True)

# def greedy(num):
#     for w in weight:
#         if num >= w:
#             num -= w
#         if num == 0:
#             break
#     if num == 0:
#         return False
#     else:
#         return True   

# for num in range(1, 1000001):
#     if greedy(num):
#         break

# print(num)
