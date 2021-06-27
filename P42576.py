def solution(participant, completion):
    answer = ""
    dict = {}
    for pt in participant:
        if pt in dict:
            dict[pt] += 1
        else:
            dict[pt] = 1
    for cp in completion:
        dict[cp] -= 1

    for pt in participant:
        if dict[pt] != 0:
            answer = pt
    return answer