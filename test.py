from collections import deque

def solution(board):
    n = len(board)
    q = deque()
    q.append((0, 0, 1))
    q.append((0, 0, 2))
    board[0][0] = 0
    while q:
        r, c, d = q.popleft()
        move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        for di in d:
            nr, nc = r + move[di][0], c + move[di][1]
            if di == d:
                next_cost = board[r][c] + 100
            else:
                next_cost = board[r][c] + 600
            if 0 <= nr < n and 0 <= nc < n:
                if board[nr][nc] == 0 or board[nr][nc] >= next_cost:
                    board[nr][nc] = next_cost
                    q.append((nr, nc, di))
    return board[-1][-1]