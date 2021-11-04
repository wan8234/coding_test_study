def solution(begin, target, words):
    global answer
    answer = 51
    
    def dfs(w, words, c):
        global answer
        if w == target:
            answer = min(answer, c)
            return
        for x in words:
            cnt = 0
            for i in range(len(x)):
                if w[i] == x[i]:
                    cnt += 1
            if cnt == len(x) - 1:
                words.remove(x)
                dfs(x, words, c+1)
                words.append(x)
                
    dfs(begin, words, 0)
    
    if answer == 51:
        answer = 0
    
    return answer

