N = int(input())    # 센서
K = int(input())    # 집중국
arr = list(map(int, input().split()))
arr.sort()

cost = []
for i in range(1,N):
    cost.append(arr[i] - arr[i-1])
cost.sort(reverse = True)

del cost[0:K-1]
print(sum(cost))
