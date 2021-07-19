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