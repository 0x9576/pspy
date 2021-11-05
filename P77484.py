def solution(lottos, win_nums):
    unknown = 0
    minimum = 0
    for l in lottos:
        if l == 0:
            unknown += 1
        if l in win_nums:
            minimum += 1
    answer = [min(6,7- minimum-unknown) ,min(7- minimum,6)]
    return answer