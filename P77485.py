def solution(rows, columns, queries):
    answer = []
    board = [[columns * i + j + 1 for j in range(columns)] for i in range(rows)]
    for q in queries:
        answer.append(rotate(board, q[0]-1, q[1]-1, q[2]-1, q[3]-1))
    return answer

def left_to_right(board, row, start, end, move_list):
    ret = board[row][end]
    move_list.append(ret)
    for i in range(end, start, -1):
        board[row][i] = board[row][i-1]
        move_list.append(board[row][i-1])
    return ret

def top_to_bottom(board, col, start, end, move_list):
    ret = board[end][col]
    move_list.append(ret)
    for i in range(end, start, -1):
        board[i][col] = board[i-1][col]
        move_list.append(board[i-1][col])
    return ret

def right_to_left(board, row, start, end, move_list):
    ret = board[row][end]
    move_list.append(ret)
    for i in range(end, start):
        board[row][i] = board[row][i+1]
        move_list.append(board[row][i+1])
    return ret

def bottom_to_top(board, col, start, end, move_list):
    ret = board[end][col]
    move_list.append(ret)
    for i in range(end, start):
        board[i][col] = board[i+1][col]
        move_list.append(board[i+1][col])
    return ret

def rotate(board, lr, lc, hr, hc):
    move_list = []
    ltr = left_to_right(board, lr, lc, hc, move_list)
    ttb = top_to_bottom(board, hc, lr, hr, move_list)
    rtl = right_to_left(board, hr, hc, lc, move_list)
    btt = bottom_to_top(board, lc, hr, lr, move_list)
    board[lr+1][hc] = ltr
    board[hr][hc-1] = ttb
    board[hr-1][lc] = rtl
    board[lr][lc+1] = btt
    move_list.sort()
    return move_list[0]