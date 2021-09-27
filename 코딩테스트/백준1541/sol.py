import sys

input = sys.stdin.readline


# '-' 기준으로 입력값을 문자열로 나눔
n = input().split('-')

answer = 0

# -를 기준으로 나누어진 각 숫자들의 합을 구한다
for i in n[0].split('+'):
    answer += int(i)

#  첫 문자열을 제외한 다음 숫자들을 모두 빼면 결과값 나옴

for i in n[1:]:
    for j in i.split('+'):
        answer -= int(j)


print(answer)