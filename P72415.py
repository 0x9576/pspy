from collections import deque

q = deque()
def move (a, b, f, board,enter, ctrl, d,):
    if ctrl == 2 : ctrl = 3
    dir = [(1,0),(-1,0),(0,1),(0,-1)]
    x,y = min(3, max(0, a + ctrl * dir[d][0])), min(3, max(0, b + ctrl * dir[d][1]))
    if a != x or b != y:
        q.append((x,y,f+1,board,enter))

def is_empty(board):
    for bd1 in board:
        for bd2 in bd1:
            if bd2:
                return False
    return True

def solution(board, r, c):
    answer = 0
    enter = []
    q.append((r,c,0,board,enter))
    while q:
        front = q.popleft()
        a, b, f, bd,et = front[0], front[1], front[2], front[3], front[4]
        oet = et
        obd = bd
        print(front)
        if is_empty(bd):
            answer = f
            break

        if bd[a][b]:
            if len(et)==1:
                r1, c1 = et[0][0], et[0][1]
                if (r1 != a or c1 != b) and bd[r1][c1] == bd[a][b]:
                    et = []
                    bd[r1][c1], bd[a][b] = 0, 0
                    q.append((a, b, f + 1, bd, et))
                    bd, et = obd, oet
            else:
                et.append((a, b))
                q.append((a, b, f + 1, bd, et))
                et = oet

        for i in range(0,4):
            for j in range(1,3):
                move(a, b, f, bd,et, j, i)
    return answer


solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0)