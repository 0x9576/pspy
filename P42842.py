def solution(brown, yellow):
    total = brown + yellow
    row = total / 2
    col = 2
    while 1:
        r, c, b = row, col, brown
        b -= r * 2
        c -= 2
        b -= c * 2
        if b == 0:
            answer = [row, col]
            break
        col += 1
        row = total / col
    return answer