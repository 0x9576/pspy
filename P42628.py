import heapq

def solution(operations):
    push, pop = 0, 0
    for op in operations:
        if push <= pop:
            max_hq, min_hq = [], []
        if op[0] == 'I':
            heapq.heappush(min_hq, int(op[2:]))
            heapq.heappush(max_hq, -int(op[2:]))
            push += 1
        else:
            if op[2] == "1":
                if max_hq:
                    heapq.heappop(max_hq)
                    pop += 1
            elif min_hq:
                heapq.heappop(min_hq)
                pop += 1
    if max_hq and min_hq:
        answer = [-max_hq[0], min_hq[0]]
    else:
        answer = [0, 0]
    return answer