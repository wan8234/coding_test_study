#### use bisect ####
from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0]

for a in arr:    
    if dp[-1] < a:
        dp.append(a)
    else:
        index = bisect_left(dp, a)
        dp[index] = a

print(len(dp) - 1)

#### use private function ####
# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))
# dp = [0]

# def binary(value):
#     left, right = 1, len(dp) - 1

#     while left < right:
#         mid = (left + right) // 2

#         if dp[mid] < value:
#             left = mid + 1
#         else:
#             right = mid
    
#     return right

# for a in arr:
#     if a > dp[-1]:
#         dp.append(a)
#     else:
#         dp[binary(a)] = a

# print(len(dp) - 1)
