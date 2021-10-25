for tc in range(1, int(input()) + 1):

    n = int(input())

    atoms = []

    for i in range(n):
        x, y, d, e = map(int, input().split())
        x *= 2
        y *= 2
        atoms.append([x, y, d, e])

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    count = 0
    energy = 0

    while 1:

        dic = {}

        for i in range(len(atoms)):
            atoms[i][0] += dx[atoms[i][2]]
            atoms[i][1] += dy[atoms[i][2]]
            try:
                dic[(atoms[i][0], atoms[i][1])].append(atoms[i])
            except:
                dic[(atoms[i][0], atoms[i][1])] = [atoms[i]]

        atoms = []
        
        for i in dic.keys():
            if len(dic[i]) > 1:
                for atom in dic[i]:
                    energy += atom[3]
                    count += 1
            else:
                x = dic[i][0][0]
                y = dic[i][0][1]
                if -4001 < x < 4001 and -4001 < y < 4001:
                    atoms.append(dic[i][0])
                else:
                    count += 1
        if count == n:
            break

    print('#{} {}'.format(tc, energy))
