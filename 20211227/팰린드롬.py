import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

dp = [[0] * N for _ in range(N)]

for i in range(N):
    for s in range(N):
        e = s + i
        #범위 넘음
        if e >= N:
            break

        #수열 길이가 1이면 무조건 팰린드롬
        if i == 0: #e==s
            dp[s][e] = 1
            continue

        #수열 길이가 2이고 좌우가 같으면 팰린드롬
        if i == 1:
            if num[s] == num[e]:
                dp[s][e] = 1
                continue

        #s, e가 같고 s+1 ~ e-1까지가 팰린드롬이면 팰린드롬
        if num[s] == num[e] and dp[s+1][e-1] == 1:
            dp[s][e] = 1



M = int(input())
for _ in range(M):
    x, y = map(int, input().split())
    print(dp[x-1][y-1])


# def F(x, y):
#     if x == y:
#         return True
#     temp = num[x-1:y]
#     l = len(temp)
#     if temp[:l // 2] == temp[:-(l//2) - 1:-1]:
#         return True
#     else:
#         return False

# def F(x, y):
#     if x == y:
#         return True
#     temp = num[x-1:y]
#     i, j = 0, len(temp)-1
#     while i < j:
#         if temp[i] == temp[j]:
#             i += 1
#             j -= 1
#         else:
#             return False
#     else:
#         return True
