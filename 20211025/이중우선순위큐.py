import heapq as hq 

def solution(operations):
    answer = []
    minh = []
    maxh = []
    for x in operations:
        o, n = x.split()
        if o == 'I':
            hq.heappush(minh, int(n))
            hq.heappush(maxh, -int(n))
        else:
            if int(n) == -1:
                if minh:
                    hq.heappop(minh)
                    #최대힙 최대 값이 최소 힙 최소값보다 작으면 배열이 빈거
                    if not minh or minh[0] > -maxh[0]:
                        minh = []
                        maxh = []
            else:
                if maxh:
                    hq.heappop(maxh)
                    if not maxh or -maxh[0] < minh[0]:
                        minh = []
                        maxh = []
    
    if not maxh:
        answer = [0, 0]
    else:
        answer = [-maxh[0], minh[0]]

    return answer