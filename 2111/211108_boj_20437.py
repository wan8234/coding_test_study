from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())

def game(string):
    length = len(string)

    alpha = defaultdict(list)

    for i in range(length):
        if string.count(string[i]) >= K:
            alpha[string[i]].append(i)

    if not alpha:
        return -1,
    
    minimum = int(1e9)
    maximum = 0

    for distance in alpha.values():
        for i in range(len(distance) - K + 1):
            temp = distance[i + K - 1] - distance[i] + 1

            minimum = min(minimum, temp)
            maximum = max(maximum, temp)
    return minimum, maximum


for test_case in range(T):
    string = input().rstrip()
    K = int(input())

    print(*game(string))


#### USING SLIDING WINDOW(SHORT) ####
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    string = list(map(lambda x: ord(x) - 97, input().rstrip()))
    K = int(input())
    mini = len(string)
    maxi = -1
    
    pos = [[] for _ in range(26)]
    for idx, val in enumerate(string):
        pos[val].append(idx)
        
    for p in pos:
        for i in range(len(p) - K + 1):
            mini = min(mini, p[i + K - 1] - p[i] + 1)
            maxi = max(maxi, p[i + K - 1] - p[i] + 1)
    print(-1 if maxi == -1 else '{} {}'.format(mini, maxi))