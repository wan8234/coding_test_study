def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif stuff == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True               

def solution(n, build_frame):
    answer = []
    
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        if operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer)

#### SHORT TIME ####

# def is_installable(x, y, is_beam, beam_board, pillar_board):
#     if is_beam:
#         return (pillar_board[x][y - 1] or pillar_board[x + 1][y - 1]) or ((x >= 1 and beam_board[x - 1][y]) and beam_board[x + 1][y])
#     else:
#         return (y == 0) or ((x >= 1 and beam_board[x - 1][y]) or beam_board[x][y]) or pillar_board[x][y - 1]

# def install(x, y, is_beam, beam_board, pillar_board, is_install):
#     if is_beam:
#         beam_board[x][y] = is_install
#     else:
#         pillar_board[x][y] = is_install

# def check_validity(res, beam_board, pillar_board):
#     for x, y, is_beam in res:
#         if not is_installable(x, y, is_beam, beam_board, pillar_board):
#             return False
#     return True

# def solution(board_sz, insts):
#     res = []
#     beam_board = [[False] * (board_sz + 1) for _ in range(board_sz + 1)]
#     pillar_board = [[False] * (board_sz + 1) for _ in range(board_sz + 1)]
#     for x, y, is_beam, is_install in insts:
#         if is_install:
#             if is_installable(x, y, is_beam, beam_board, pillar_board):
#                 install(x, y, is_beam, beam_board, pillar_board, is_install)
#                 res.append([x, y, is_beam])
#         else:
#             install(x, y, is_beam, beam_board, pillar_board, is_install)
#             if check_validity(res, beam_board, pillar_board):
#                 res.remove([x, y, is_beam])
#             else:
#                 install(x, y, is_beam, beam_board, pillar_board, True)
#     return sorted(res)