import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = list(input().strip('\n'))

k = K
answer = []

#큰 수 : 앞 자리 수가 커야함
for i in range(N):
    while k > 0 and answer:
        #넣으려는 숫자가 앞 자리 수보다 클 때 : 앞 숫자를 지우고 현재 숫자를 넣음
        if answer[-1] < num[i]:
            answer.pop()
            k -= 1
        else:
            break
    answer.append(num[i])

#앞 숫자가 제일 큰 것만 고려해서 집어넣는 방식이라서
#뒤에 애들은 고려하지 않으므로 지울 횟수가 남아있을 때, 뒤의 숫자는 지우지 않음
# N-K번째까지만 출력하는 조건이 있어야함
print(''.join(answer[:N-K]))
