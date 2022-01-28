def solution(rows, columns, queries):
    matrix = [[j + rows * i + 1 for j in range(columns)] for i in range(rows)]  # 행렬생성
    answer = []
    for query in queries:  # query 는 원소가 4개인 배열이다.
        x1, y1, x2, y2 = query[1] - 1, query[0] - 1, query[3] - 1, query[2] - 1
        # 좌표상 (x1,y1), (x2,y2)를 만들기 위함.
        # 문제에서 주어진걸 잘 보면 행,열과 좌표축이 바뀌어있음.
        right, down, left = matrix[y1][x2], matrix[y2][x2], matrix[y2][x1]
        minimum = min(right,down, left)
        # row가 y축이고, column이 x축이기 때문에, matrix[x][y] 가 아닌, matrix[y][x]형식이 되어야 함.
        # 때문에 for문을 다음과 같이 설정함.
        for x in range(x2-1, x1+1, -1): # 우측으로 옮기기
            matrix[y1][x + 1] = matrix[y1][x]
            minimum = min(minimum, matrix[y1][x+1])
        matrix[y1+1][x2] = right
        # 옮기는 도중에 행렬 요소들이 소실되기 때문에, 이러한 방법을 사용.
        for y in range(y2-1, y1+2, -1): # 하단으로 옮기기
            matrix[y+1][x2] = matrix[y][x2]
            minimum = min(minimum, matrix[y+1][x2])
        matrix[y2][x2-1] = down
        for x in range(x1+1, x2): # 좌측으로 옮기기
            matrix[y2][x-1] = matrix[y2][x]
            minimum = min(minimum, matrix[y2][x-1])
        matrix[y2-1][x1] = left
        for y in range(y1+1, y2): # 상단으로 옮기기
            matrix[y-1][x1] = matrix[y][x1]
            minimum = min(minimum, matrix[y-1][x1])
        answer.append(minimum)
        print(matrix)
    return answer