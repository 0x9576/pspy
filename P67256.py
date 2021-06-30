def dis(t1, t2):
    a = abs(t1[0] - t2[0])
    b = abs(t1[1] - t2[1])
    return a+b

def solution(numbers, hand):
    pos = {}
    answer = ''
    lp, rp = (0, 3), (0, 3)
    for i in range(0, 9):
        pos[i+1] = (i % 3, i//3)
    pos[0] = (1, 3)

    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            answer += 'L'
            lp = pos[n]
        elif n == 3 or n == 6 or n == 9:
            answer += 'R'
            rp = pos[n]
        else:
            if dis(pos[n], lp) > dis(pos[n], rp):
                answer += 'R'
                rp = pos[n]
            elif dis(pos[n], rp) > dis(pos[n], lp):
                answer += 'L'
                lp = pos[n]
            else:
                if hand == "right":
                    answer += 'R'
                    rp = pos[n]
                else:
                    answer += 'L'
                    lp = pos[n]

    return answer