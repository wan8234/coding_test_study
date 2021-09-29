import sys
input = sys.stdin.readline

string = input().split('-')
num = []
for s in string:
    temp = 0
    line = s.split('+')
    for l in line:
        temp += int(l)
    num.append(temp)

result = num[0]
for i in range(1, len(num)):
    result -= num[i]
print(result)
        
# import sys
# input = sys.stdin.readline

# string = input()
# digit = [str(i) for i in range(10)]

# result = 0
# num = ''
# temp = 0
# plus = 1
# minus = 0

# for s in string:
#     if s in digit:
#         num += s
#     else:
#         if s == '+':
#             temp += int(num)
#             num = ''
#         elif s == '-':
#             temp += int(num)
#             num = ''

#             if plus == 1:                
#                 result += temp
#                 temp = 0
#                 plus = 0
#                 minus = 1
#             elif minus == 1:
#                 result -= temp
#                 temp = 0

# temp += int(num)
# if temp != 0:
#     if plus == 1:
#         result += temp
#     elif minus == 1:
#         result -= temp
    
# print(result)