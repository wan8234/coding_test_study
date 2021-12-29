import sys
input = sys.stdin.readline

N, M = map(int, input().split())

matrix = []
for _ in range(N):
    line = list(map(int, input().strip('\n')))
    matrix.append(line)

K = int(input())

#한 행을 다 켜려고 할 때
#나머지 행 들 중에서 몇 개의 행이 같이 켜지는 지를 찾아서 (행의 조건이 같은 경우)
#그 중의 최대 값을 찾는다!

#i번째 행을 다 켰을 때 다 켜지는 행 개수를 저장할 배열
cnt = [0] * N

#한 행을 다 켜려면
#1. K가 꺼진 전구(0)의 개수보다 많아야함
#2. K가 홀수면 0의 개수도 홀수여야함 ( 반대도 마찬가지 )
#   -> 홀짝이 다르면 전구를 다 켤 수 없음

#K의 홀짝
OorE = K % 2

for i in range(N):
    #i번째 행의 0 개수
    zero = matrix[i].count(0)
    #0 개수가 K 이하이고 K의 홀짝과 같으면
    if zero <= K and zero % 2 == OorE:
        for j in range(N):
            #i번재 행과 같은 행이 있으면 같이 켤 수 있다
            if matrix[i] == matrix[j]:
                cnt[i] += 1

print(max(cnt))