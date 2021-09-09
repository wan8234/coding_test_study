import sys

def merge(left, right):
    result = []

    while len(left) > 0 or len(right)>0:

        if len(left) > 0 and len(right) > 0:
 
            if left[0] <= right[0]:
                result.append(left[0])
                left=left[1:]
            else:
                result.append(right[0])
                right = right[1:]
 
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

def merge_sort(arr):
    
    if len(arr) <= 1:
        return arr

    middle = len(arr)//2

    left = merge_sort(arr[middle:])
    right = merge_sort(arr[:middle])

    return merge(left,right)



input = sys.stdin.readline
n = int(input())

num_list = list()

for _ in range(n):
    num_list.append(int(input()))

for item in merge_sort(num_list):
    print(item)