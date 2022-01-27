def solution(board, aloc, bloc):
    answer = req(board, aloc, bloc, 0)[1]
    return answer


def get_move_list(board, loc):
    row = len(board)
    col = len(board[0])
    move_list = []
    # 아래
    if loc[0] + 1 < row and board[loc[0] + 1][loc[1]]:
        move_list.append((loc[0] + 1, loc[1]))
    # 위
    if loc[0] - 1 >= 0 and board[loc[0] - 1][loc[1]]:
        move_list.append((loc[0] - 1, loc[1]))
    # 오른쪽
    if loc[1] + 1 < col and board[loc[0]][loc[1] + 1]:
        move_list.append((loc[0], loc[1] + 1))
    # 왼쪽
    if loc[1] - 1 >= 0 and board[loc[0]][loc[1] - 1]:
        move_list.append((loc[0], loc[1] - 1))
    return move_list


def req(board, loc, o_loc, count):
    if board[loc[0]][loc[1]] == 0: # 발판이 없다면 바로 패배
        return [0, count]
    move_list = get_move_list(board, loc)
    possible = False  # 승리가 가능한가?
    ret = [0, 0]
    if move_list:
        for move in move_list:
            board[loc[0]][loc[1]] = 0  # 원래 있었던 곳 0으로
            # 이번엔 상대가 움직일 차례다. 결과가 나온다.
            result = req(board, (o_loc[0], o_loc[1]), (move[0], move[1]), count + 1)
            board[loc[0]][loc[1]] = 1  # 다시 돌려놓는다.
            if result[0] == 0:  # 상대가 졌다면, 내가 이김
                if not possible:  # 못이기는 줄 알았으면
                    possible = True  # 바꾸어줌
                    ret = [1, result[1]]
                else:  # 이기는 줄 알고있었다면,
                    ret[1] = min(ret[1], result[1])  # 가장 적은 수로 이기는 것으로 바꾸어줌.
            else:  # 상대가 이겼다면, 내가 짐.
                if not possible:  # 못이기는 줄 알았고있으면,
                    ret[1] = max(ret[1], result[1])  # 최대한 시간을 끌어야 함.
                # 이기는 줄 알았다면 바꿀 필요 없음. 그냥 이기는 사례를 반환하면 됨. (져주면 안된다)
        return ret
    else:  # 움직일 곳이 없다.
        return [0, count]
