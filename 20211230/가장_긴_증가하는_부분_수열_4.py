import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

#i:[최대 증가하는 수열] 딕셔너리
dp = {i:[nums[i]] for i in range(n)}
#하나도 없을 경우 : 하나라도 출력해줘야함
result = [nums[0]]


for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            #현재 상황에서 최대 길이 수열이랑, 전 수열 + 1 했을 때랑 길이를 비교해서
            if len(dp[i]) < len(dp[j]) + 1:
                #큰 경우 전 수열 + 현재 숫자 
                dp[i] = dp[j] + [nums[i]]
                #최대값 result에 저장해두기
                if len(dp[i]) > len(result):
                    result = dp[i]

print(len(result))
for x in result:
    print(x, end=" ")
