N = int(input())

arr = list(map(int, input().split()))
up = [1] * N
down = [1] * N

for i in range(N):
    for j in range(i):
        # i번째까지 차례로 커지는 횟수를 저장
        if arr[i] > arr[j]:
            up[i] = max(up[i], up[j]+1)



for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        # i번째까지 차례로 작아지는 횟수를 저장
        if arr[i] > arr[j]:
            down[i] = max(down[i], down[j]+1)

answer = 0
# 가장 긴 바이토닉 수열의 길이 구하기
for i in range(N):
    answer = max(up[i] + down[i] -1 , answer)

print(answer)
