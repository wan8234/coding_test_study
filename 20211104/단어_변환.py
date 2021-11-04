def solution(begin, target, words):
    answer = 0
    stack = [begin] # 비교 단어 후보군
    visited = [False] * len(words)
    
    if target not in words:
        return answer
    
    while stack:
        # 비교할 단어
        word = stack.pop()
        
        if word == target:
            return answer
        
        for i in range(len(words)):
            cnt = 0
            for j in range(len(word)):
                #비교 대상과 word와 스펠링 틀린 갯수 비교
                if words[i][j] != word[j]:
                    cnt += 1
            # 스펠링이 1개만 틀릴 경우
            if cnt == 1:
                # 이미 방문 했을 경우 무시
                if visited[i]:
                    continue
                else:
                    visited[i] = True
                    #1개 틀린 것들을 비교 단어 후보군에 추가
                stack.append(words[i])
        answer += 1
    
    return answer
