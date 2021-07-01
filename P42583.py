from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque()
    load = 0
    while truck_weights:
        answer += 1
        if q and q[0][1]+bridge_length <= answer:
            load -= q.popleft()[0]
        if weight-load >= truck_weights[-1]:
            top = truck_weights.pop()
            load += top
            q.append((top, answer))
    while q:
        answer += 1
        if q[0][1]+bridge_length <= answer:
            load -= q.popleft()[0]
    return answer