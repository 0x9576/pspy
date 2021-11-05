def solution(table, languages, preference):
    dict = {}
    for i in range(0, len(languages)):
        dict[languages[i]] = preference[i]
    for t in table:
        arr = t.split()
        job = arr[0]
        if job not in dict:
            dict[job] = 0
        score = 5
        for i in range(1, len(arr)):
            if arr[i] in dict:
                dict[job] += dict[arr[i]] * score
            score -= 1
    max_value, answer = -1, "zzzzzzzz"
    for key in dict:
        if dict[key] > max_value or (dict[key] == max_value and answer > key):
            answer = key
            max_value = dict[key]
    return answer
