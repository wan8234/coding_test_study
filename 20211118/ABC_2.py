import sys
input = sys.stdin.readline

n, k = map(int, input().split())

answer = ''
check = [[[0 for _ in range(k+1)] for _ in range(n+1)] for _ in range(n+1)]

def solution(case, a, b, S):
    global answer

    #조건 개수가 k 넘어가면 return
    if case > k:
        return

    #S의 길이가 n일때 조건 개수가 같으면 
    if len(S) == n:
        if case == k:
            answer = S
        return
    
    #이미 해봤던 계산 - pass
    if check[a][b][case] != 0:
        return

    check[a][b][case] = 1

    # 뒤에 들어갈 문자가 A, B, C
    solution(case, a+1, b, S+'A')
    solution(case+a, a, b+1, S+'B')
    solution(case+a+b, a, b, S+'C')

solution(0, 0, 0, '')
if answer == '':
    print(-1)
else:
    print(answer)