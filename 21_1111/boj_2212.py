import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

sensor = list(map(int,input().split()))

if k >= n:
    print(0)
    exit(0)

sensor.sort()

sensor_distance = list()

for i in range(len(sensor)-1):
    sensor_distance.append(sensor[i+1]-sensor[i])

sensor_distance.sort()


for _ in range(k-1):
    sensor_distance.pop()

print(sum(sensor_distance))