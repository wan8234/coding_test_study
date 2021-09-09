n = int(input())

stack = list()
answer = list()
count = 0

for _ in range(n):
    
    num = int(input())

    while count < num:

        count += 1
        stack.append(count)
        answer.append('+')

    if num == stack[len(stack)-1]:  
        stack.pop()
        answer.append('-')
    else:   # stack top != input => fail
        print("NO") 
        exit(0)


for i in range(len(answer)):
    print(answer[i])