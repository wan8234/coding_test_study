#### ONLY PYPY ####
# import sys
# input = sys.stdin.readline

# first = input().rstrip()
# second = input().rstrip()

# answer = 0

# dp = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]

# for i in range(1, len(first) + 1):
#   for j in range(1, len(second) + 1):
#       if (first[i - 1] == second[j - 1]):
#           dp[i][j] = dp[i - 1][j - 1] + 1
#           answer = max(dp[i][j], answer)

# #answer = max(map(max, dp))
# print(answer)

#### SOLVE 1 ####
import sys
input = sys.stdin.readline
 
first = input().rstrip()
second = input().rstrip()

answer = 0
dp = [0] * (len(second) + 1)

for i in range(len(first)):
    temp = [0] * (len(second) + 1)
    for j in range(len(second)):
        if first[i] == second[j]:
            temp[j + 1] = dp[j] + 1
			
    answer = max(answer, max(temp))
    dp = temp[:]
print(answer)

#### SOLVE 2 ####
import sys
input = sys.stdin.readline

first = input().rstrip()
second = input().rstrip()

answer = 0
dp = [0] * (len(second) + 1)

for i in range(len(first)):
    for j in range(len(second) - 1, -1, -1):
        if first[i] == second[j]:
            dp[j] = dp[j - 1] + 1
            if answer < dp[j]:
                answer = dp[j]
        else:
            dp[j] = 0
			
print(answer)
