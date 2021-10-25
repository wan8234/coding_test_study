T = int(input())
for t in range(T):
    N = int(input())
    atom = []
    dx = [0, 0, -0.5, 0.5]
    dy = [0.5, -0.5, 0, 0]
    dic = dict()
    for _ in range(N):
        line = list(map(int, input().split()))
        dic[(line[0], line[1])] = [(line[2], line[3])]

    answer = 0
    for _ in range(4000):
        #move
        if len(dic) <= 1:
            break
        tempdic = dict()
        for i in dic:
            x, y = i
            d, e = dic[i][0]
            nx = x + dx[d]
            ny = y + dy[d]
            if -1000 <= nx <= 1000 and -1000 <= ny <= 1000:
                if (nx, ny) in tempdic:
                    tempdic[(nx, ny)].append(dic[i][0])
                else:
                    tempdic[(nx, ny)] = dic[i]
        dic = tempdic

        #bomb
        bomb = []
        for i in dic:
            if len(dic[i]) > 1:
                for x in dic[i]:
                    answer += x[1]
                bomb.append(i)

        for x in bomb:
            dic.pop(x)

    print("#",t+1, " ", answer, sep="")
