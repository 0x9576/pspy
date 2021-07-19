from itertools import permutations
import copy

def solution(expression):
    answer = 0
    lis = ['+', '*', '-']
    perm_lis = permutations(lis, 3)
    expression_list = []
    st = ""
    for ex in expression:
        if ex in lis:
            expression_list.append(st)
            expression_list.append(ex)
            st = ""
        else:
            st += ex
    expression_list.append(st)
    ex_list = copy.copy(expression_list)
    for perm_li in perm_lis:
        expression_list = copy.copy(ex_list)
        for li in perm_li:
            while li in expression_list:
                i = expression_list.index(li)
                expression_list[i] = str(eval(expression_list[i - 1] + expression_list[i] + expression_list[i + 1]))
                del expression_list[i - 1]
                del expression_list[i]
        answer = max(answer, abs(int(expression_list[0])))
    return answer