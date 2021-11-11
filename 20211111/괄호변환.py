# u,v로 분리
def divide(p):
    left = 0
    right = 0

    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return p[:i + 1], p[i + 1:]

# "올바른 괄호 문자열"인지 판단
def isCorrect(p):
    cnt = 0 
    for i in p:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return True # 쌍이 맞는 경우에 True 반환

def solution(p):
    answer = ''
    # 1.입력이 빈 문자열인 경우
    if p == '':
        return answer
    
    # 2. u,v로 분리
    u, v = divide(p)
    
    # 3. u가 "올바른 괄호 문자열"이면, v에 대해 1단계부터 다시 수행
    if isCorrect(u):
        answer = u + solution(v)
    # 4. u가 "올바른 괄호 문자열"이 아닐 경우
    else:
        # 4-1,2,3
        answer = '('
        answer += solution(v)
        answer += ')'
        # 4-4. 첫번째와 마지막 문자 제거
        u = list(u[1:-1]) 
        # 4-4. 나머지는 반대로해서 붙임     
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
        
    return answer
