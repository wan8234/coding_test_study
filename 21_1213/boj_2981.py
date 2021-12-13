import sys

input = sys.stdin.readline


def get_gcd(a, b):  # 유클리드 호제법
    if b > a:
        temp = a
        a = b
        b = temp
    if b == 0:
        return a
    else:
        return get_gcd(b, a % b)

n = int(input())

arr = list()

for _ in range(n):
    arr.append(int(input()))

arr.sort()

diffs = [] # 연속된 숫자들의 차 구하기
for i in range(1, len(arr)):
    diffs.append(abs(arr[i] - arr[i - 1]))
 
 
gcd = diffs[0] # 숫자들의 차 들의 GCD 구하기
for i in range(1, len(diffs)):
    gcd = get_gcd(diffs[i], gcd)
 
results = []

for i in range(2, int(pow(gcd, 0.5)) + 1):
    
    if gcd % i == 0:  
        results.append(i)

        if gcd // i != i:  
            results.append(gcd//i)  

results.append(gcd)  
results.sort()

print(*results)