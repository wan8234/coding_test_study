def solution(s):
    answer = len(s)
    
    for u in range(len(s) // 2, 0, -1):
        #이전 문자열 단위 
        prev = s[0:u]
        #몇번 연속 나왔는지
        cnt = 1
        #전체 문장
        sentence = ""
        #마지막 남은 문자열
        last = ""
        for x in range(u, len(s)+1, u):
            last = s[x:x+u]
            if s[x:x+u] == prev:
                cnt += 1
                check = True
            else:
                if cnt > 1:
                    sentence += str(cnt) + prev
                else:
                    sentence += prev
                prev = s[x:x+u]
                cnt = 1
        sentence += last
        answer = min(answer, len(sentence))
                
    
    return answer