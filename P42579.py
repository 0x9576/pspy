import operator


def solution(genres, plays):
    answer = []
    dic = {}
    dic2 = {}
    for i in range(0, len(genres)):
        if genres[i] not in dic:
            new_list = []
            dic[genres[i]] = new_list
            dic2[genres[i]] = 0
        dic[genres[i]].append((i, plays[i]))
        dic2[genres[i]] += plays[i]
    sorted_dic = sorted(dic2.items(), key=operator.itemgetter(1), reverse=True)
    for sd in sorted_dic:
        dic[sd[0]].sort(key=lambda x: x[1], reverse=True)
        co = 0
        for dsd in dic[sd[0]]:
            if co > 1:
                break
            answer.append(dsd[0])
            co += 1
    return answer