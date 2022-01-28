import copy

answer = []
score_gap = 0


def solution(n, info):
    make_score(n, info, [])
    if len(answer) == 0:
        return [-1]
    else:
        return answer


def cal_priority(answer, ryan):
    for i in range(10,-1,-1):
        if answer[i] < ryan[i]:
            return True
        elif answer[i] > ryan[i]:
            return False
    return False


def cal_score_gap(apeach, ryan):
    score_gap = 0
    for i in range(11):
        if apeach[i] == 0 and ryan[i] == 0:
            score_gap += 0
        elif apeach[i] >= ryan[i]:
            score_gap -= 10-i
        else:
            score_gap += 10-i
    return score_gap


def make_score(n, apeach, ryan):
    global answer
    global score_gap
    if len(ryan) == 11:
        s_gap = cal_score_gap(apeach, ryan)
        if score_gap == s_gap and len(answer)==11:
            if cal_priority(answer, ryan):
                answer = copy.deepcopy(ryan)
                ryan = []
                return
        if score_gap < s_gap :
            score_gap = s_gap
            if n>0:
                ryan[10] += n
            answer = copy.deepcopy(ryan)
            ryan = []
        return
    else:
        for i in range(n+1): # 0->n
            ryan.append(i)
            make_score(n-i,apeach, ryan)
            ryan.pop()