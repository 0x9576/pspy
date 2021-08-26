from collections import deque


def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    dq = deque(people)
    while dq:
        if len(dq) == 1:
            answer += 1
            break
        front = dq.popleft()
        top = dq[-1]
        if front + top <= limit:
            dq.pop()
        answer += 1
    return answer