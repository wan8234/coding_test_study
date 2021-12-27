import sys
input = sys.stdin.readline

N, K = map(int, input().split())
N = list(str(N))

#dp를 딕셔너리로 만들어서 "dp[(현재 num값, k(depth))] = 결과 값" 형식으로 저장해줄 것
dp = dict()

#교환
def swap(num, a, b):
    num[a], num[b] = num[b], num[a]
    return num


def dfs(num, k):
    if k == K:
        return int(''.join(num))

    #이미 실행했던 경우
    if (int(''.join(num)), k) in dp:
        return dp[(int(''.join(num)), k)]

    for i in range(len(N)):
        for j in range(len(N)):
            if i != j:
                #교환시 0이 맨 앞으로 가는 경우는 안됨
                if i == 0 and num[j] == '0':
                    continue

                #재귀 실행 -> temp에 k까지 실행한 경우의 값을 받게 됨
                temp = dfs(swap(num, i, j), k+1)
                #swap 실행하면서 num이 바뀜, 되돌려주기
                swap(num, i, j)

                #dp에 최대 결과값 저장하기
                if (int(''.join(num)), k) not in dp:
                    dp[(int(''.join(num)), k)] = temp
                else:
                    dp[(int(''.join(num)), k)] = max(temp, dp[(int(''.join(num)), k)])

    return dp[(int(''.join(num)), k)]


#교환 불가능한 경우
if (len(N) == 2 and N[1] == '0') or len(N) == 1:
    print(-1)
    sys.exit()
else:
    print(dfs(N, 0))