def solution(board):
    answer = 0
    visited = []
    visited.append(((0, 0), (0, 1), 0))
    answer = move(visited, board, (0, 0), (0, 1), 0)
    return answer


def move(visited, board, loc1, loc2, count):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    if final(board, loc1, loc2):
        return count
    for i in range(4):
        next1 = loc1[0]+dr[i], loc1[1]+dc[i]
        next2 = loc2[0]+dr[i], loc2[1]+dc[i]
        if is_possible(board, next1) and is_possible(board, next2) and check_visited(next1, next2, visited, count):
            visited.append((next1, next2, count))
            move(visited, board, next1, next2, count+1)
    rotate_list = get_rotate_list(loc1, loc2)
    for rotate in rotate_list:
        next1 = rotate[0]
        next2 = rotate[1]
        if is_possible(board, next1) and is_possible(board, next2) and check_visited(next1, next2, visited, count):
            visited.append((next1, next2, count))
            move(visited, board, next1, next2, count+1)


def get_rotate_list(loc1, loc2):
    rotate_list = []
    if loc1[0] == loc2[0]:  # 수평상태 -> 행변경
        rotate_list.append((loc1, (loc2[0] + 1, loc1[1])))
        rotate_list.append((loc1, (loc2[0] - 1, loc1[1])))
        # 회전축 변경
        rotate_list.append(((loc1[0] + 1, loc2[1]), loc2))
        rotate_list.append(((loc1[0] - 1, loc2[1]), loc2))
    else:   # 수직상태 -> 열변경
        rotate_list.append((loc1, (loc1[0], loc2[1]+1)))
        rotate_list.append((loc1, (loc1[0], loc2[1]-1)))
        # 회전축 변경
        rotate_list.append(((loc2[0], loc1[1]+1), loc2))
        rotate_list.append(((loc2[0], loc1[1]-1), loc2))
    return rotate_list


def is_possible(board, loc):
    # 한 점이 갈 수 있는 위치에 있나?
    size = len(board)
    if 0 <= loc[0] < size and 0 <= loc[1] < size:
        if not board[loc[0]][loc[1]]:
            return True
    return False


def check_visited(loc1, loc2, visited, count):
    for v in visited:
        if ((loc1[0] == v[0][0] and loc1[1] == v[0][1] and loc2[0] == v[1][0] and loc2[1] == v[1][1])
                or (loc2[0] == v[0][0] and loc2[1] == v[0][1] and loc1[0] == v[1][0] and loc1[1] == v[1][1])):
            if v[2] <= count:
                return False
    return True


def final(board, loc1, loc2):
    size = len(board)
    if loc1[0] == size-1 and loc1[1] == size-1:
        return True
    elif loc2[0] == size-1 and loc2[1] == size-1:
        return True
    return False

