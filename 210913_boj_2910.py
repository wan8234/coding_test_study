import sys
input = sys.stdin.readline

n, c = map(int, input().split())
message = list(map(int, input().split()))

priority = {}

for m in message:
    priority[m] = priority.get(m, 0) + 1

sorted_priority = sorted(priority.items(), key = lambda x : -x[1])

for k, v in sorted_priority:
    for i in range(v):
        print(k, end = " ")

