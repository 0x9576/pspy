from collections import deque

def solution(n, weak, dist):
    answer = 9999
    weak.sort()
    dist.sort(reverse = True)
    for i in range(1,5):
        if i > 2:
            weak.sort(reverse = True)
        queue = deque(weak)
        dist_queue = deque(dist)
        for w in weak:
            sub_dq = deque(dist_queue)
            sub_q = deque(queue)
            start = sub_q.popleft()
            front_dis = sub_dq.popleft()
            while sub_q and sub_dq:
                if i % 2 == 1:
                    distance = sub_q[0] - start
                else:
                    distance = start - sub_q[0]
                if distance < 0:
                    distance += n
                if distance <= front_dis:
                    front_dis -= distance
                else:
                    front_dis = sub_dq.popleft()
                start = sub_q.popleft()
                print(start, front_dis,distance, sub_q, sub_dq)
            if not sub_q:
                answer = min(answer, len(dist) - len(sub_dq))
            front = queue.popleft()
            queue.append(front)
            print()
    if answer == 9999:
        answer = -1
    print(answer)
    return answer

# solution(12,[1, 5, 6, 10],[1, 2, 3, 4])
# solution(12,[1, 3, 4, 9, 10],[3, 5, 7])
# solution(200,[0, 100],[1, 1])
# solution(50,[1],[6])
# solution(200, [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30])
# solution(12, [10, 0], [1, 2])
solution(30, [0, 3, 11, 21], [10, 4])