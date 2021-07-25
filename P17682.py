def solution(dartResult):
    answer = 0
    dart_array = []
    dic = {"S" : 1, "D" : 2, "T" : 3}
    pass_list = []
    for i in range(0, len(dartResult)):
        if i in pass_list:
            continue
        dr = dartResult[i]
        if dr == "*" or dr == "#":
            end = len(dart_array)
            start = end - 2
            if start < 0:
                start = 0
            if dr == "*":
                for i in range(start, end):
                    dart_array[i] = dart_array[i] * 2
            else:
                dart_array[-1] *= -1
        elif dr in dic:
            dart_array[-1] = dart_array[-1] ** dic[dr]
        elif dr == "1" and i < len(dartResult) - 1 and dartResult[i+1] == "0":
            dart_array.append(10)
            pass_list.append(i+1)
        else:
            dart_array.append(int(dr))
    for da in dart_array:
        answer += da
    return answer