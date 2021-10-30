def solution(brown, yellow):
    answer = []
    x, y = 1, 1
    
    while True:
        #갈색부분, 노란색부분 계산해서 비교
        if 2 * x + 2 * (y - 2) == brown and (x-2) * (y-2) == yellow:
            break
        #x가 y보다 커야되니까 x부터 +1 해주고
        #x y 같아지면 x + 1, y = 1 해주면서 완전탐색
        if x == y:
            x += 1
            y = 1
        else:
            y += 1
    answer = [x, y]
    return answer