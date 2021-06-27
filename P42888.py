def solution(record):
    answer = []
    tem = []
    dic = {}
    for r in record:
        rs = r.split(' ')
        if rs[0] == "Enter":
            dic[rs[1]] = rs[2]
            tem.append(rs[1]+"님이 들어왔습니다.")
        if rs[0] == "Leave":
            tem.append(rs[1]+"님이 나갔습니다.")
        if rs[0] == "Change":
            dic[rs[1]] = rs[2]

    for t in tem:
        anss = t.split("님")
        a = t.replace(anss[0], dic[anss[0]])
        answer.append(a)
    return answer
