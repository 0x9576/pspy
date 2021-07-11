import heapq

def solution(jobs):
    hq = []
    answer = 0
    idx, time,complete = 0, 0, 0
    l = len(jobs)
    while idx < l or hq:
        while idx < l and jobs[idx][0] == time:
            jl = jobs[idx]
            heapq.heappush(hq, (jl[1], jl[0]))
            idx += 1
        if idx == l:
            while hq:
                time = complete
                top = heapq.heappop(hq)
                complete = time + top[0]
                answer += complete - top[1]
            break
        if complete == time and hq:
            top = heapq.heappop(hq)
            complete = time + top[0]
            answer += complete - top[1]
        time += 1

    answer = answer /  float(l)
    return int(answer)