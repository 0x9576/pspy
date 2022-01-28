def solution(board, skill):
    answer = 0
    # borad보다 행,열이 1만큼 큰 배열 생성
    arr = [[0 for c in range(len(board[0])+1)] for r in range(len(board)+1)]
    for s in skill:
        point(arr, s)
    # 가중합 만들기
    cal(arr)
    # 두개의 배열합을 board에 저장
    for i in range(len(arr)-1):
        for j in range(len(arr[0])-1):
            board[i][j] += arr[i][j]
    for b_list in board:
        for b in b_list:
            if b > 0:
                answer += 1
    return answer


def point(arr, skill):
    # 배열의 특정 부분만을 미리 지정 후 나중에 계산
    # 가중합을 구하면 구하고자 하는 배열이 나온다.
    if skill[0] == 1:
        skill[5] = -skill[5]
    arr[skill[1]][skill[2]] += skill[5]
    arr[skill[1]][skill[4] + 1] -= skill[5]
    arr[skill[3]+1][skill[2]] -= skill[5]
    arr[skill[3]+1][skill[4] + 1] += skill[5]


def cal(arr):
    # 가중합 계산
    # 왼쪽에서 오른쪽으로 가중합
    for i in range(0, len(arr)):
        for j in range(1, len(arr[0])):
            arr[i][j] += arr[i][j-1]
    # 위에서 아래로 가중합
    for j in range(0, len(arr[0])):
        for i in range(1, len(arr)):
            arr[i][j] += arr[i-1][j]