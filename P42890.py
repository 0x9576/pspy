from itertools import combinations

def solution(relation):
    col = len(relation[0])
    row = len(relation)
    selected = []
    for i in range(1, col+1):
        lis = list(combinations(range(0,col), i))
        for l in lis:
            temp_set = set()
            for l1 in l:
                temp_set.add(l1)
            selected.append(temp_set)

    unique = []
    for s in selected:
        eset = set()
        for i in range(0, row):
            str = ""
            for st in s:
                str += relation[i][st]
            eset.add(str)
        if len(eset) == row:
            unique.append(s)

    selected = unique
    remove_set = set()
    for s1 in selected:
        for s2 in selected:
            if s1 != s2:
                if len(s2-s1)==0:
                    remove_set.add(selected.index(s1))
                if len(s1-s2)==0:
                    remove_set.add(selected.index(s2))

    answer = len(unique) - len(remove_set)
    return answer