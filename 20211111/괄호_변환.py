def check(x):
    stack = []
    for i in x:
        if i == "(":
            stack.append(1)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if not stack:
        return True

def half(x):
    l, r = 0, 0
    c = 0
    for i in x:
        c += 1
        if i == "(":
            l += 1
        else:
            r += 1
        if l != 0 and l == r:
            break
    return x[0:c], x[c:]

def solution(p):
    answer = ''
    
    if check(p):
        return p
    
    u, v = half(p)

    if check(u):
        return u + solution(v)
    
    else:
        temp = "(" + solution(v) + ")"
        new_u = ""
        for i in u[1:-1]:
            if i == "(":
                new_u += ")"
            else:
                new_u += "("
        return temp + new_u


print(solution("()))((()"))
print(solution(")("))
