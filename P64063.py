def find_room(dic, want):
    if want not in dic:
        dic[want] = want + 1
        return want
    alter = find_room(dic, dic[want])
    dic[want] = alter + 1
    return alter

def solution(k, room_number):
    answer = []
    dic = {}
    for rn in room_number:
        room = find_room(dic, rn)
        answer.append(room)
    return answer