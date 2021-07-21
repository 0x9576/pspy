from collections import deque

def solution(board):
    n = len(board)
    q = deque()
    q.append((0, 0, 1))
    q.append((0, 0, 2))
    while q:
        r, c, d = q.popleft()
        d1, d2 = d - 1, d + 1
        if d1 < 0:
            d1 += 4
        if d2 > 3:
            d2 -= 4
        d = [d, d1, d2]
        move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        for di in d:
            nr, nc = r + move[di][0], c + move[di][1]
            if di == d[0]:
                next_cost = board[r][c] + 100
            else:
                next_cost = board[r][c] + 600
            if 0 <= nr < n and 0 <= nc < n:
                if board[nr][nc] == 0 or board[nr][nc] >= next_cost:
                    board[nr][nc] = next_cost
                    q.append((nr, nc, di))
    print(board)
    return board[-1][-1]