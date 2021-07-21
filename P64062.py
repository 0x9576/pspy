def solution(stones, k):
    left, right = 1, 200000000
    while left<=right:
        mid = (left+right) // 2
        cnt = 0
        for st in stones:
            if st - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt>=k:
            right = mid - 1
        else:
            left = mid + 1
    return left

"""
def solution(stones, k):
    answer = 0
    while 1:
        var_pass = 0
        for i in range(len(stones)):
            if stones[i] > 0:
                stones[i] -= 1
                var_pass = 0
            else :
                var_pass += 1
            if var_pass >= k:
                return answer
        answer += 1
    return answer
"""