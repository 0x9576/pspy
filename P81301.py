def solution(s):
    eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    dic = {}
    for i in range(0, 10):
        dic[eng[i]] = str(i)
    for key in dic:
        s = s.replace(key, dic[key])
    answer = int(s)
    return answer