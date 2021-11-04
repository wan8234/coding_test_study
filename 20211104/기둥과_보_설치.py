# 기둥이 있을 수 있는 경우
    # y == 0일 경우
    # (x-1, y) or (x, y)에 '보'가 있는 경우
    # (x, y-1)에 기둥이 있는경우
# 보가 있을 수 있는 경우
    # (x, y-1) or (x+1, y-1)에 기둥이 있는 경우
    # (x-1, y) and (x+1, y)에 보가 있는 경우
# 그 외는 다 불가능

def isPossible(res):
    for x, y, a in res:
        # 기둥일 때
        if a == 0:
            if y == 0 or [x-1, y, 1] in res or [x, y, 1]  in res or [x, y-1, 0] in res:
#            if [x-1, y, 1] or [x, y, 1] or [x, y-1, 0] in res:
                continue
            return False   
        # 보일 때
        if a == 1:
            if [x, y-1, 0] in res or [x+1, y-1, 0] in res or ([x-1, y, 1] in res and [x+1, y, 1] in res):
                continue
            return False
    return True
    

def solution(n, build_frame):
    
    res = []
    
    for x, y, a, b in build_frame:
        case = [x, y, a]
        #설치
        if b == 1:
            res.append(case)
            if not isPossible(res):
                res.remove(case)
        #삭제
        elif case in res:
            res.remove(case)
            if not isPossible(res):
                res.append(case)
    answer = list(map(list, res))
    answer.sort()
    return answer
    
    
    #=------------------------------------
        # b가 생성일 때
        # a가 기둥일 경우
            # (x-1,y) or (x, y) 에 보가 있거나 (x,y-1)에 기둥이 있는지 확인
                # 있다면, 쌓는다
                # 없다면, 무시
        # a가 보일 경우
            # (x, y-1) or (x+1, y-1)에 기둥이 있거나, (x-1,y) and (x+1, y)에 보가 있는지 확인
                # 있다면, 생성
                # 없다면, 무시
    # b가 삭제일 때, 
        # a가 기둥일 경우
            # 
        # a가 보일 경우
            # (x-1, y)에 '보'가 있고 (x, y-1)에 기둥이 없을때 무시
            # (x+1, y)에 '보'가 있고 (x-1, y-1)에 기둥이 없을때 무시
            # (x-1, 
        

