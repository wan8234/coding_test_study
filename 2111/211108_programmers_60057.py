def solution(s):
    answer = len(s)
    
    for length in range(1, len(s)//2 + 1):
        result = ''
        string = s[:length]
        count = 1
        for token in range(length, len(s), length):
            temp = s[token: token + length]
            if temp == string:
                count += 1
            elif temp != string:
                if count != 1:
                    result += str(count)
                count = 1
                result += string
                string = temp
        if count != 1:
            result += str(count)
        result += string    
        answer = min(answer, len(result))
    return answer