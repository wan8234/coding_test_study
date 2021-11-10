def solution(p):
    answer = ''
    answer = parenCheck(p)
    return answer

def parenCheck(line):
    if line == '':
        return ''
    length = len(line)
    
    check = 0
    for i in range(length):
        if line[i] == '(':
            check += 1
        elif line[i] == ')':
            check -= 1
        if check == 0:
            break
    u = line[:i + 1]
    v = line[i + 1:]
    
    check = 0
    pivot = 0
    length = len(u)
    for i in range(length):
        if u[i] == '(':
            check += 1
        elif u[i] == ')':
            check -= 1
        if check < 0:
            pivot = 1
            break
    if pivot == 0:
        return u + parenCheck(v)
    else:
        empty = '('
        empty += parenCheck(v)
        empty += ')'
        u = u[1:-1]
        length = len(u)
        temp = ''
        for i in range(length):
            if u[i] == '(':
                temp += ')'
            else:
                temp += '('
        u = temp
        
        return empty + u