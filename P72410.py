from string import ascii_lowercase
def solution(new_id):
    answer = new_id.lower()

    possible_list = list(ascii_lowercase) + ['.', '-', '_']
    for i in range(0,10):
        possible_list.append(str(i))
    for ch in answer:
        if ch not in possible_list:
            answer = answer.replace(ch, "")

    for i in range(len(answer)):
        answer = answer.replace("..", ".")

    if answer != "":
        if answer[0] == ".":
            answer = answer[1:]
    if answer != "":
        if answer[-1] == ".":
            answer = answer[:-1]

    if answer == "":
        answer = "a"

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[0:-1]
    if len(answer) <= 2:
        while 1:
            if len(answer) >= 3:
                break
            answer += answer[-1]

    return answer