from collections import deque
from itertools import combinations

def solution(n, weak, dist):
    answer = 9999
    weak.sort()
    dist.sort(reverse = True)
    for i in range(1,3):
        if i == 2:
            weak.sort(reverse = True)
        queue = deque(weak)
        dist_queue = deque(dist)
        for w in weak:
            sub_dq = deque(dist_queue)
            sub_q = deque(queue)
            start = sub_q.popleft()
            front_dis = sub_dq.popleft()
            while sub_q and (sub_dq or front_dis):
                if i == 1:
                    distance = sub_q[0] - start
                else:
                    distance = start - sub_q[0]
                if distance < 0:
                    distance += n
                if distance <= front_dis:
                    front_dis -= distance
                else:
                    if sub_dq:
                        front_dis = sub_dq.popleft()
                    else:
                        break
                start = sub_q.popleft()
            if not sub_q:
                answer = min(answer, len(dist) - len(sub_dq))
            front = queue.popleft()
            queue.append(front)
    if answer == 9999:
        answer = -1
    return answer

def sol(n, weak, dist):
    W, F = len(weak), len(dist)
    repair_lst = [()]  # 현재까지 고칠 수 있는 취약점들 저장 (1,2,3)
    count = 0  # 투입친구 수
    dist.sort(reverse=True)  # 움직일 수 있는 거리가 큰 친구 순서대로

    # 고칠 수 있는 것들 리스트 작성
    for can_move in dist:
        repairs = []  # 친구 별 고칠 수 있는 취약점들 저장
        count += 1

        # 수리 가능한 지점 찾기
        for i, wp in enumerate(weak):
            start = wp  # 각 위크포인트부터 시작
            ends = weak[i:] + [n + w for w in weak[:i]]  # 시작점 기준 끝 포인트 값 저장
            can = [end % n for end in ends if end -
                   start <= can_move]  # 가능한 지점 저장
            repairs.append(set(can))

        # 수리 가능한 경우 탐색
        cand = set()
        for r in repairs:  # 새친구의 수리가능 지점
            for x in repair_lst:  # 기존 수리가능 지점
                new = r | set(x)  # 새로운 수리가능 지점
                if len(new) == W:  # 모두 수리가능 한 경우 친구 수 리턴
                    return count
                cand.add(tuple(new))
        repair_lst = cand
    return -1

o_dist = list(range(1,101))
for n in range(1, 201):
    o_weak = list(range(1, n))
    for i in range (1, min(15, n-1) + 1): # weak 개수 for 문
        for j in range (1, 9): # dist 개수 for 문
            com_weak_list = combinations(o_weak, i)
            com_dist_list = combinations(o_dist, j)
            for cwl in com_weak_list:
                for cdl in com_dist_list:
                    list_cwl = list(cwl)
                    list_cdl = list(cdl)
                    if sol(n,list_cwl, list_cdl) != solution(n, list_cwl, list_cdl):
                        print(n, list_cwl, list_cdl)


# solution(12,[1, 5, 6, 10],[1, 2, 3, 4]) # 2
# solution(12,[1, 3, 4, 9, 10],[3, 5, 7]) # 1
# solution(200,[0, 100],[1, 1]) # 2
# solution(50,[1],[6]) # 1
# solution(200, [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30]) # 3
# solution(200, [0, 10, 50, 80, 120, 160], [1, 10, 10, 30, 40]) # 3
# solution(4, [1, 3], [1, 2]) # 1
# solution(12, [10, 0], [1, 2]) # 1
# solution(30, [0, 3, 11, 21], [10, 4]) # 2
# solution(50, [49, 47, 42, 1],[2, 2, 10]) # 1