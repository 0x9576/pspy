from collections import deque

def solution(food_times, k):
    ft = []
    for i in range(0, len(food_times)):
        ft.append((food_times[i], i))
    sorted_ft = sorted(ft)
    dq = deque(sorted_ft)
    rotate = 0
    while dq:
        len_dq = len(dq)
        front = dq.popleft()
        if front[0] <= rotate:
            continue
        fr = front[0]-rotate
        if len_dq * fr <= k:
            k -= len_dq * fr
            rotate += fr
        else:
            dq.appendleft(front)
            break
    if not dq:
        return -1
    sorted_ft = []
    while dq:
        front = dq.popleft()
        sorted_ft.append((front[0]-rotate, front[1]+1))
    sorted_ft = sorted(sorted_ft, key=lambda x: x[1])
    pos = k % len(sorted_ft)
    answer = sorted_ft[pos][1]
    return answer
