def solution(nums):
    dict = {}
    for n in nums:
        if n not in dict:
            dict[n] = 0
        dict[n] += 1
    size = len(dict)
    answer = min(len(nums)/2, size)
    return answer