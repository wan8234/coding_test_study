import sys

input = sys.stdin.readline

n,m = map(int,input().split()) #n = num of tree, m = length of tree

tree = list(map(int,input().split()))

#for i in range(len(t)):
#    tree.append(int(t[i]))

left,right = 1,max(tree)

while left <= right:

    mid = (left+right) // 2

    cutted = 0

    for i in tree:
        if i >= mid:
            cutted += i - mid

    if cutted >= m:
        left = mid+1
    else:
        right = mid -1

print(right)
