def solution(k, room_number):
    answer = []
    lis = [0 for _ in range(k+1)]
    for rn in room_number:
        if lis[rn] == 1:
            for i in range(rn+1, k):
                if lis[i] == 0:
                    rn = i
                    break
        lis[rn] = 1
        answer.append(rn)
    return answer