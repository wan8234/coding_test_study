from collections import deque
from itertools import combinations
import sys, copy
input = sys.stdin.readline

N, K = map(int, input().split())
idx = [i for i in range(len(str(N)))]
idx_comb = list(combinations(idx, 2))
queue = deque()
queue.append(N)

def bfs():
    numbers = set()
    result = 0
    length = len(queue)
    for _ in range(length):
        num = queue.popleft()
        string_num = list(str(num))
        
        for x, y in idx_comb:
            temp = copy.deepcopy(string_num)
            temp[x], temp[y] = temp[y], temp[x]
            
            if temp[0] == '0':
                continue
            new_number = int(''.join(temp))
            if new_number not in numbers:
                result = max(result, new_number)
                numbers.add(new_number)
                queue.append(new_number)
    return result
    
result = 0
while K:
    result = bfs()
    K -= 1
print(result if result != 0 else -1)
            