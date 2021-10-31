def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for i in range(3, total//2):
        if not total % i:
            row = total // i - 2
            col = i - 2
            if row * col == yellow:
                answer = [row + 2, col + 2]
                break
    
    return answer

# def solution(brown, yellow):
#     answer = []
#     total = brown + yellow
    
#     row = 1
#     col = yellow
#     for i in range(yellow):
#         carpet_row = row + 2
#         carpet_col = col + 2
#         if carpet_row * carpet_col == total:
#             answer = [carpet_col, carpet_row]
#             break
#         else:
#             row *= 2
#             col //= 2
    
#     return answer