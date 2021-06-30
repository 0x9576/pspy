from collections import deque


def solution(priorities, location):
    printing = {}
    tup_list = []
    i = 0
    for pr in priorities:
        tup_list.append((pr,i))
        i+=1
    q = deque(tup_list)
    priorities.sort(reverse=True)
    idx = 0
    while q:
        n = q.popleft()
        if n[0] >= priorities[idx]:
            idx += 1
            printing[n[1]] = idx
        else:
            q.append(n)
    answer = printing[location]
    return answer