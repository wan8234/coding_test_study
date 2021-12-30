N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        # i번째까지 차례로 커지는 횟수를 저장
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

index = dp.index(max(dp))
answer = []
cnt = max(dp)

while index >= 0:
    if dp[index] == cnt:
        answer.append(str(arr[index]))
        cnt -= 1
    index -= 1

answer.reverse()
print(' '.join(answer))

