from itertools import combinations
def solution(orders, course):
    dic = {}
    all_set = set()
    answer = []
    for od in orders:
        for i in range(2, len(od)+1):
            com_list = list(combinations(od, i))
            for tup in com_list:
                tup_list = list(tup)
                tup_list.sort()
                st = ''.join(tup_list)
                all_set.add(st)
                if dic.get(st) == None:
                    dic[st] = 1
                else:
                    dic[st] += 1

    mx_dict = {}
    for co in course:
        mx = 0
        for alls in all_set:
            if len(alls) == co:
                mx = max(dic[alls], mx)
        mx_dict[co] = mx

    for co in course:
        for alls in all_set:
            if len(alls) == co:
                if mx_dict[co] >= 2 and dic[alls] == mx_dict[co]:
                    answer.append(alls)
    answer.sort()


    return answer