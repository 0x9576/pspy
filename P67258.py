def solution(gems):
    all = len(set(gems))
    dict = {gems[0] : 1}
    left, right = 0, 0
    answer = [0, 999999]
    while left<=right:
        if len(dict) == all:
            if answer[1] - answer[0] > right - left:
                answer = [left+1, right +1]
            else:
                dict[gems[left]] -= 1
                if dict[gems[left]] == 0:
                    del dict[gems[left]]
                left += 1
        else:
            right += 1
            if right >= len(gems):
                break
            if gems[right] not in dict:
                dict[gems[right]] = 0
            dict[gems[right]] += 1
    return answer