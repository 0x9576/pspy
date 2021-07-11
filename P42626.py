import heapq
def solution(scoville, K):
    answer = 0
    hq = []
    for sc in scoville:
        heapq.heappush(hq, sc)
    while hq:
        top = heapq.heappop(hq)
        if top >= K:
            break
        answer += 1
        if not hq:
            return -1
        top2 = heapq.heappop(hq)
        s = top + (top2 *2)
        heapq.heappush(hq, s)
    return answer