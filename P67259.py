from collections import deque
import copy

def solution(board):
    n = len(board)
    q = deque()
    q.append((0, 0, 1))
    q.append((0, 0, 2))
    bd = []
    for _ in range(4):
        cp = copy.deepcopy(board)
        bd.append(cp)
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
                next_cost = bd[d[0]][r][c] + 100
            else:
                next_cost = bd[d[0]][r][c] + 600
            if 0 <= nr < n and 0 <= nc < n and bd[di][nr][nc] != 1:
                if bd[di][nr][nc] == 0 or bd[di][nr][nc] > next_cost:
                    bd[di][nr][nc] = next_cost
                    q.append((nr, nc, di))
    answer = 9999999999999
    for b in bd:
        if b[-1][-1] != 0:
            answer = min(answer, b[-1][-1])
    return answer