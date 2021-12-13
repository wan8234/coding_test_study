import sys
import math
input = sys.stdin.readline

# 숫자 : N, 몫 : K
# 나머지가 R로 같다면
# N[0] = M * K[0] + R
# N[1] = M * K[1] + R
# M을 구하기 위해 R을 제거 => 2번째 식에서 1번째 식을 빼기
# N[1] - N[0] = M * (K[1] - K[0])
# M은 N[1] - N[0]과 K[1] - K[0]의 약수
# 약수는 최대공약수의 약수

n = int(input())
N = []
gcd = 0
for i in range(n):
    x = int(input())
    N.append(x)
    if i == 1:
        gcd = N[1] - N[0]
    gcd = math.gcd(gcd, abs(N[i] - N[i-1]))

result = []
for i in range(2, int(gcd ** 0.5 + 1)):
    if gcd % i == 0:
        result.append(i)
        result.append(gcd // i)
        # 약수 한번에 두개 구하기
        # gcd = x * y  => x, gcd // x

#마지막으로 gcd 추가, 중복 제거
result.append(gcd)
result = list(set(result))
result.sort()
for x in result:
    print(x, end= " ")