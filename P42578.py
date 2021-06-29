def solution(clothes):
    answer = 1
    dic = {}
    for clo in clothes:
        if clo[1] in dic:
            dic[clo[1]].append(clo[0])
        else:
            new_list = []
            new_list.append(clo[0])
            dic[clo[1]] = new_list
    for d in dic:
        answer *= len(dic[d]) + 1
    answer -= 1
    return answer