from collections import deque
import math


def solution(progresses, speeds):
    answer = []
    q = deque(progresses)
    idx, ans = 1, 1
    cnt = math.ceil((100 - q.popleft()) / float(speeds[0]))
    while q:
        n = q.popleft()
        if speeds[idx] * cnt >= 100 - n:
            ans += 1
        else:
            answer.append(ans)
            ans = 1
            cnt = math.ceil((100 - n) / float(speeds[idx]))
        idx += 1
    answer.append(ans)
    return answer
