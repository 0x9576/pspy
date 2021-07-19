visited = [[]]
flag = True

def dfs(start_r, start_c, r, c, pla):
    global flag
    move = [[-1, 0], [1, 0], [0, 1], [0, 1]]
    for mv in move:
        nr, nc = r + mv[0], c + mv[1]
        if 0<=nr<5 and 0<=nc<5:
            if abs(start_r - nr) + abs(start_c - nc) <= 2:
                if visited[nr][nc] == 0:
                    if pla[nr][nc] == "O":
                        visited[nr][nc] = 1
                        dfs(start_r, start_c, nr, nc, pla)
                    if pla[nr][nc] == "P":  # 이것도 visited[nr][nc] == 0 조건 내에 있어야 한다.
                        flag = False
def solution(places):
    global flag
    global visited
    answer = []
    for pla in places:
        num = -1
        for i in range(0, 5):
            for j in range(0, 5):
                if pla[i][j] == "P":
                    visited = [[0] * 5 for _ in range(5)]
                    visited[i][j] = 1
                    flag = True
                    dfs(i, j, i, j, pla)
                    if not flag:
                        num = 0
        if num == -1:
            num = 1
        answer.append(num)
    return answer