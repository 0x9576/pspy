import heapq
from collections import deque

def solution(jobs):
    answer,time = 0, 0
    jobs.sort()
    hq = []
    size = len(jobs)
    jobs = deque(jobs)
    while jobs or hq:
        while jobs and time >= jobs[0][0]:
            front = jobs.popleft()
            heapq.heappush(hq, (front[1], front[0]))
        if hq:
            hq_front = heapq.heappop(hq)
            answer += hq_front[0]+time-hq_front[1]
            time += hq_front[0]
        else:
            time += 1
    return int(answer / float(size))