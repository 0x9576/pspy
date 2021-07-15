from collections import deque
from itertools import permutations
import copy

answer = 9999
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
                des.append((a, b))
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

def req(a,b ,index, nums, board, dic, case):
    case0 = case
    o = copy.deepcopy(board)
    global answer
    if index == len(nums):
        answer = min(answer, case)
        return
    pos_list = dic[nums[index]]
    case += bfs(a, b, pos_list[0][0], pos_list[0][1], board)[2]
    case += bfs(pos_list[0][0], pos_list[0][1], pos_list[1][0], pos_list[1][1], board)[2]
    board[pos_list[0][0]][pos_list[0][1]], board[pos_list[1][0]][pos_list[1][1]] = 0, 0
    req(pos_list[1][0], pos_list[1][1], index+1, nums, board, dic, case)

    case = case0
    board = copy.deepcopy(o)

    case += bfs(a, b, pos_list[1][0], pos_list[1][1], board)[2]
    case += bfs(pos_list[1][0], pos_list[1][1], pos_list[0][0], pos_list[0][1], board)[2]
    board[pos_list[0][0]][pos_list[0][1]], board[pos_list[1][0]][pos_list[1][1]] = 0, 0
    req(pos_list[0][0], pos_list[0][1], index+1, nums, board, dic, case)

def solution(board, r, c):
    o = copy.deepcopy(board)
    global answer
    dic = {}
    answer = 9999
    nums = []
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                if board[i][j] not in dic:
                    nums.append(board[i][j])
                    dic[board[i][j]] = []
                dic[board[i][j]].append((i, j))
    perm = list(permutations(nums, len(nums)))
    for p1 in perm:
        req(r, c, 0, p1, board, dic, 0)
        board = copy.deepcopy(o)
    return answer
