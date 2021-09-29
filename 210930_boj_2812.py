import sys
input = sys.stdin.readline

n, k = map(int, input().split())
number = list(input().strip()) # delete '\n'
stack = []

temp = k

for i in range(n):    
    while temp > 0 and stack and stack[-1] < number[i]:
        stack.pop()
        temp -= 1
    stack.append(number[i])
print(''.join(stack[:n - k]))

# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# temp = input()
# number = []
# for t in temp[:-1]:
#     number.append(int(t))

# def cutter(number):
#     global k

#     maximum = max(number)
#     while maximum > 0:
#         try:
#             i = number.index(maximum)
#         except:
#             maximum -= 1

#         if i > k:
#             maximum -= 1
#             continue
#         else:
#             k -= i

#         return number[i:]

# n -= k

# for i in range(k):
#     number = cutter(number)

#     if len(number) == n:
#         break

# if len(number) != n:
#     for i in range(len(number) - n):
#         minimum = min(number)
#         number.pop(number.index(minimum))

# result = ''
# for n in number:
#     result += str(n)

# print(int(result))