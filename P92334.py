def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    dict_reported = {}
    send_email = {}
    order = {}
    i = 0
    for id in id_list:
        order[id] =i
        i += 1

    for rep in report:
        rep_arr = rep.split()
        if rep_arr[1] not in dict_reported:
            dict_reported[rep_arr[1]] = set()
        dict_reported[rep_arr[1]].add(rep_arr[0])

    for key in dict_reported:
        if len(dict_reported[key]) >= k:
            for mail in dict_reported[key]:
                if mail not in send_email:
                    send_email[mail] = 0
                send_email[mail] += 1

    for key in send_email:
        answer[order[key]] = send_email[key]

    return answer