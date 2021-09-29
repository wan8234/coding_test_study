import sys
input = sys.stdin.readline
n = int(input())

data = []

for i in range(n):
    data.append(int(input()))

def merge_sort(data):
    if len(data) <= 1:
        return data
    
    mid = len(data)//2
    left = data[:mid]
    right = data[mid:]

    l_data = merge_sort(left)
    r_data = merge_sort(right)

    return merge(l_data, r_data)

def merge(l_data, r_data):
    i = j = 0
    result = []

    while i < len(l_data) and j < len(r_data):
        if l_data[i] < r_data[j]:
            result.append(l_data[i])
            i += 1
        else:
            result.append(r_data[j])
            j += 1

    while i < len(l_data):
        result.append(l_data[i])
        i += 1
    
    while j < len(r_data):
        result.append(r_data[j])
        j += 1

    return result

data = merge_sort(data)
for i in data:
    print(i)