from itertools import permutations

n = int(input())
k = int(input())
nums = []
for _ in range(n):
    x = input().strip('\n')
    nums.append(x)

answer = set()
for i in permutations(nums, k):
    print(i)
    answer.add(''.join(i))

print(len(answer))