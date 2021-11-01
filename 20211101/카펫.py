def solution(brown, yellow):
    # x * y == 갈색 + 노란색
    # (x-2)*(y-2) == 노란색
    x = (brown + 4 + ((brown +4)**2 -16*(brown + yellow)) **0.5) / 4
    y = (brown + yellow) / x
    answer = [max(x, y), min(x, y)]
    return answer
