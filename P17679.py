def solution(m, n, board):
    answer = 0
    bd = []
    for b in board:
        new_lis = list(b)
        bd.append(new_lis)
    board = bd
    while 1:
        del_list = []
        for i in range(0, m-1):
            for j in range(0, n-1):
                if board[i][j] != 'a' and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    del_list.append((i,j))
                    del_list.append((i+1,j))
                    del_list.append((i,j+1))
                    del_list.append((i+1,j+1))
        if not del_list:
            break
        for dl in del_list:
            if board[dl[0]][dl[1]] != 'a':
                answer +=1
                board[dl[0]][dl[1]] = 'a'
        while 1:
            co = 0
            for i in range(0, m - 1):
                for j in range(0, n):
                    if board[i][j] != 'a' and board[i + 1][j] == 'a':
                        co += 1
                        board[i + 1][j] = board[i][j]
                        board[i][j] = 'a'
            if co == 0:
                break
        print(board)
    return answer