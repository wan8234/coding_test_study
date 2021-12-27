import sys
input = sys.stdin.readline

#1. 최대 만들 수 있는 자릿수
#2. 제일 큰 자릿수부터 큰 수로 바꾸기

N = int(input())
P = list(map(int, input().split()))
M = int(input())

iP = [(P[i], i) for i in range(N)]
iP.sort()

#최대 자릿수 만들기
room = [iP[0][1]] * (M//iP[0][0])
money = iP[0][0] * len(room)

#앞자리 0인 경우 처리해주기
if sum(room) == 0:
    while True:
        if len(P) == 1 or not room:
            room = [0]
            money = M
            break
        if money - iP[0][0] + iP[1][0] <= M:
            room[0] = iP[1][1]
            money = money - iP[0][0] + iP[1][0]
            break
        room.pop()
        money -= iP[0][0]

#앞자리부터 가능한 가장 큰 수로 바꿔주기
if room == [0]:
    print(0)
else:
    for i in range(len(room)):
        for j in range(N-1, room[i], -1):
            if i == 0 and j == 0:
                continue
            if money - P[room[i]] + P[j] <= M:
                money = money - P[room[i]] + P[j]
                room[i] = j
                break

    for x in room:
        print(x, end="")