def solution(words, queries):
    answer = []
    dic = {}
    for word in words:
        st = "?"
        temp = []
        for i in range(1, len(word)):
            temp.append(st + word[i:])
            temp.append(word[:len(word)-i] + st)
            st += "?"
        temp.append(st)
        for t in temp:
            if t not in dic:
                dic[t] = 0
            dic[t] += 1
    for q in queries:
        if q in dic:
            answer.append(dic[q])
        else:
            answer.append(0)
    return answer