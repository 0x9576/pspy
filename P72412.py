from itertools import combinations


def solution(info, query):
    answer = []
    dic = {}
    for inf in info:
        inf_list = inf.split()
        for i in range(0, 5):
            com_list = list(combinations(inf_list[:4], i))
            for tup in com_list:
                str = ' '.join(tup)
                if str not in dic:
                    dic[str] = []
                dic[str].append(int(inf_list[4]))

    for key in dic:
        dic[key].sort()

    for q in query:
        q = q.replace("and ", "")
        q = q.replace("- ", "")
        q_list = q.split()
        key = " ".join(q_list[:-1])
        if key not in dic:
            answer.append(0)
            continue
        score_list = dic[key]
        start = 0
        end = len(score_list)
        target = int(q_list[-1])
        while start < end:
            mid = (start + end) // 2
            if score_list[mid] >= target:
                end = mid
            else:
                start = mid + 1
        answer.append(len(score_list)-start)
    return answer