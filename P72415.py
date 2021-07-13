from collections import deque
from itertools import permutations
import copy

q = deque()
def bfs (sr,sc, dr, dc, board):
    visited = [[0 for col in range(4)] for row in range(4)]
    q.append((sr, sc))
    visited[sr][sc] = 1
    while q:
        if visited[dr][dc]:
            break
        front = q.popleft()
        a, b = front[0], front[1]
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        des = []
        for di in dir:
            x, y = min(3, max(0, a + di[0])), min(3, max(0, b + di[1]))
            des.append((x, y))

        for i in range(1, 4):
            if a == 3:
                des.append((a,b))
                break
            if a + i == 3 or board[a+i][b]:
                des.append((a+i, b))
                break
        for i in range(1, 4):
            if a == 0:
                des.append((a, b))
                break
            if a - i == 0 or board[a - i][b]:
                des.append((a - i, b))
                break
        for i in range(1, 4):
            if b == 3:
                des.append((a, b))
                break
            if b + i == 3 or board[a][b+i]:
                des.append((a, b+i))
                break
        for i in range(1, 4):
            if b == 0:
                des.append((a, b))
                break
            if b - i == 0 or board[a][b-i]:
                des.append((a, b-i))
                break
        for de in des:
            x, y = de[0], de[1]
            if not visited[x][y]:
                visited[x][y] = visited[a][b] + 1
                q.append((x, y))
    while q:
        q.pop()
    return [dr, dc, visited[dr][dc]]

def solution(board, r, c):
    o = copy.deepcopy(board)
    answer = 9999
    nums = []
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                nums.append((board[i][j],i,j))
    nums.sort()
    lis = []
    print(nums)
    for i in range(0, len(nums)-1, 2):
        lis.append((nums[i], nums[i+1]))
        lis.append((nums[i+1], nums[i]))
    print(lis)

    perm = list(permutations(lis, len(lis)//2))
    print(perm)
    # print(perm)
    # for p1 in perm:
    #     board = copy.deepcopy(o)
    #     case1, case2 = 0, 0
    #     a, b = r, c
    #     for p2 in p1:
    #         des = []
    #         for i in range(4):
    #             for j in range(4):
    #                 if board[i][j] == p2:
    #                     des.append((i, j))
    #         res1 = bfs(a, b, des[0][0], des[0][1], board)
    #         case1 += res1[2]
    #         res2 = bfs(res1[0], res1[1], des[1][0], des[1][1], board)
    #         case1 += res2[2]
    #
    #         res3 = bfs(a, b, des[1][0], des[1][1], board)
    #         case2 += res3[2]
    #         res4 = bfs(res3[0], res3[1], des[0][0], des[0][1], board)
    #         case2 += res4[2]
    #         board[des[1][0]][des[1][1]] = 0
    #         board[des[0][0]][des[0][1]] = 0
    #
    #         if case1 > case2:
    #             a, b = res4[0], res4[1]
    #             case1 = case2
    #         else:
    #             a, b = res2[0], res2[1]
    #             case2 = case1
    #     answer = min(answer, case1, case2)

    return answer


#solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0)