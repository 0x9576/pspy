def solution(answers):
    count = [(0,1),(0,2),(0,3)]
    give_up_math = [[1, 2, 3, 4, 5],[2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for i in range(0, 20):
        for j in range(0,3):
            give_up_math[j] += give_up_math[j]
    for i in range(0, len(answers)):
        for j in range(0, 3):
            if give_up_math[j][i] == answers[i]:
                count[j] = (count[j][0]+1, count[j][1])
    count.sort(reverse=True)
    answer = [count[0][1]]
    for i in range(1,3):
        if count[i][0] == count[0][0]:
            answer.append(count[i][1])
    answer.sort()
    return answer