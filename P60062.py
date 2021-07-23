from itertools import permutations

def solution(n, weak, dist):
    wl = len(weak)
    answer = len(dist) + 2
    for i in range(wl):
        weak.append(weak[i]+n)
    dist_perm = list(permutations(dist, len(dist)))

    for i in range(wl):  # i는 스타팅 지점
        for dist_tup in dist_perm:
            idx = 0
            possible = weak[i] + dist_tup[idx]
            flag = True
            for j in range(i, wl+i):
                if possible < weak[j]:
                    if idx >= len(dist_tup)-1:
                        flag = False
                        break
                    idx += 1
                    possible = weak[j] + dist_tup[idx]
            if flag:
                answer = min(answer, idx+1)
    if answer > len(dist):
        answer = -1
    return answer


"""
from collections import deque

def solution(n, weak, dist):
    answer = 9999
    weak.sort()
    dist.sort(reverse = True)
    for i in range(1,3):
        if i == 2:
            weak.sort(reverse = True)
        queue = deque(weak)
        dist_queue = deque(dist)
        for w in weak:
            sub_dq = deque(dist_queue)
            sub_q = deque(queue)
            start = sub_q.popleft()
            front_dis = sub_dq.popleft()
            while sub_q and (sub_dq or front_dis):
                if i == 1:
                    distance = sub_q[0] - start
                else:
                    distance = start - sub_q[0]
                if distance < 0:
                    distance += n
                if distance <= front_dis:
                    front_dis -= distance
                else:
                    if sub_dq:
                        front_dis = sub_dq.popleft()
                    else:
                        break
                start = sub_q.popleft()
            if not sub_q:
                answer = min(answer, len(dist) - len(sub_dq))
            front = queue.popleft()
            queue.append(front)
    if answer == 9999:
        answer = -1
    return answer
"""