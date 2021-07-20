def solution(s):
    s = s[1:-1]
    s += ","
    lis = []
    temp_set = set()
    st = ""
    for s1 in s:
        if s1 == "{":
            temp_set = set()
        elif s1 == "}":
            lis.append(temp_set)
        elif s1 == ",":
            temp_set.add(int(st))
            st = ""
        else:
            st += s1
    lis = sorted(lis, key=lambda x : len(x))
    answer = []
    for li_set in lis:
        for li in li_set:
            if int(li) not in answer:
                answer.append(int(li))
    return answer