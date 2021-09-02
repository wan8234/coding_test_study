n = int(input())
sequence = []
stack = []
result = []
index = 0

def check():
    global index
    while sequence[index] == stack[-1]:
        result.append('-')
        index += 1
        stack.pop()
        
        if not stack:
            break

for _ in range(n):
    sequence.append(int(input()))

for i in range(1, n + 1):
    result.append('+')
    stack.append(i)
    check()

if stack:
    print("NO")
else:
    for val in result:
        print(val)

