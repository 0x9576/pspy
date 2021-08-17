import heapq
from collections import deque

def solution(jobs):
    answer = 0
    jobs.sort()
    hq = jobs
    jobs = deque(jobs)
    print(hq)
    print(jobs[0][0])
    while jobs:
        while answer >= jobs[0][0]:
            front = jobs.popleft()
            heapq.heappush(hq, (front[1], front[0]))
        if hq:
            hq_front = heapq.heappop(hq)
            answer += hq_front[0]
        else:
            answer += 1
    while hq:
        hq_front = heapq.heappop(hq)
        answer += hq_front[0]
    return answer