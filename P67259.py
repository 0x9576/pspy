import copy

answer = 999999999999
bd = [[], [], [], []]
def dfs(r, c, d):
    global bd
    global answer
    n = len(bd[0])
    if bd[n-1][n-1][d] != 0:
        answer = min(answer, bd[n-1][n-1][d] + 1)
    d1, d2 = d - 1, d + 1
    if d1 < 0:
        d1 += 4
    if d2 > 3:
        d2 -= 4
    d = [d, d1, d2]
    move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    for di in d:
        nr, nc = r + move[di][0], c + move[di][1]
        if d[0] != di:
            next_cost = 500
        else:
            next_cost = 100
        if 0 <= nr < n and 0 <= nc < n and bd[nr][nc] != 1:
            if bd[nr][nc][di] == 0 or bd[nr][nc][di] < bd[r][c][di]:
                bd[nr][nc][di] = bd[r][c][di] + next_cost
                dfs(nr, nc, di)

def solution(board):
    global bd
    global answer
    for i in range(0, 4):
        bd[i] = copy.deepcopy(board)
    bd[0][0][1] = -1
    bd[0][0][2] = -1
    # # 윗방향을 0을 기준삼아 시계방향으로
    dfs(0, 0, 1)
    dfs(0, 0, 2)
    print(bd)
    return answer

solution([[0,0,0],[0,0,0],[0,0,0]])