def solution(board, moves):
    answer = 0
    stack = []
    for m in moves:
        for i in range(0, len(board)):
            if board[i][m-1]:
                stack.append(board[i][m-1])
                board[i][m-1] = 0
                break
    flag = True
    while flag:
        flag = False
        for i in range(0, len(stack) - 1):
            if stack[i] == stack[i + 1]:
                answer += 2
                del stack[i]
                del stack[i]
                flag = True
                break
    return answer