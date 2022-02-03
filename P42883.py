def solution(number, k):
    size = len(number)
    dic = {}
    for i in range(size):
        dic[i] = number[i]
    for _ in range(k):
        l_value, cnt = "10", 0
        for key in dic:
            if cnt > 0 and dic[key]>l_value:
                del dic[l_pos]
                break
            cnt += 1
            l_value,l_pos = dic[key], key
            if len(dic)==cnt:
                del dic[key]
    answer = ''
    for key in dic:
        answer += dic[key]
    return answer