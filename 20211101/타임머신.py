import sys
input = sys.stdin.readline

N, M = map(int, input().split())

#노선 저장
line = []
for _ in range(M):
    x = list(map(int, input().split()))
    line.append(x)

#거리 배열(최대값으로 초기화)
answer = [int(1e9)] * (N+1)

#벨만포드 알고리즘
def bf():
    answer[1] = 0
    #도시 개수만큼 반복
    for i in range(N):
        #경로 전체 검사
        for j in range(M):
            #s 시작도시 e 끝도시 c 가중치
            s, e, c = line[j]
            #answer[e] : 현재까지 구한 e까지의 최소 거리
            #answer[s] + c : 지금 검사하는 도시를 거쳐서 e까지 갔을 때의 거리
            if answer[s] != int(1e9) and answer[e] > answer[s] + c:
                #거쳐서 가는 게 더 빠르다면 그 값을 저장
                answer[e] = answer[s] + c
                #도시 개수만큼 한바퀴 돌았는데 아직도 값이 변한다 ( 계속 줄어든다 )면 무한으로 시간이 되돌아가는 것
                if i == N-1:
                    return True
    return False

#return 값이 True이면 무한으로 시간이 돌아가는 거니까 -1 출력하고 끝
if bf():
    print(-1)
else:
    #도시 2부터 N까지의 거리 출력
    for i in range(2, N+1):
        #최대값인 경우 경로가 없는 것 = -1 출력
        if answer[i] == int(1e9):
            print(-1)
        #거리값 출력
        else:
            print(answer[i])

    