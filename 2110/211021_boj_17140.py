from collections import Counter
import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(3)]
result = -1

def calc():
    global arr

    max_len = 0
    length = len(arr)
    new_arr = []

    for i in range(length):
        count = Counter(arr[i]).most_common()
        count.sort(key = lambda x: (x[1], x[0]))
        temp = []

        for num, amount in count:
            if num != 0:
                temp.append(num)
                temp.append(amount)
        
        new_arr.append(temp)
        max_len = max(max_len, len(temp))
    
    for a in new_arr:
        if len(a) < max_len:
            temp = [0 for _ in range(max_len - len(a))]
            a.extend(temp)
    
    arr = new_arr

for i in range(101):
    if len(arr) > r - 1 and len(arr[0]) > c - 1 and arr[r - 1][c - 1] == k:
        result = i
        break
    if len(arr) < len(arr[0]):
        arr = list(zip(*arr))
        calc()
        arr = list(zip(*arr))
    else:
        calc()

print(result)