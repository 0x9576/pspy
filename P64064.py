from itertools import combinations
import copy
global_set = set()

def find_ban(dic, idx, id_set, banned_id):
    global global_set
    if idx == len(banned_id):
        if len(banned_id) == len(id_set):
            lis = list(id_set)
            lis.sort()
            s = ""
            for li in lis:
                s += li
            global_set.add(s)
        return
    key = banned_id[idx]
    pick_count = banned_id.count(key)
    comb = list(combinations(dic[key], pick_count))
    for c1 in comb:
        i_set = set(id_set)
        for c2 in c1:
            i_set.add(c2)
        find_ban(dic, idx + 1, i_set, banned_id)

def comp(user, ban):
    if len(user) != len(ban):
        return False
    for i in range(0, len(user)):
        if user[i] != ban[i] and ban[i] != '*':
            return False
    return True

def solution(user_id, banned_id):
    global global_set
    dic = {}
    for bid in banned_id:
        ban_set = set()
        for uid in user_id:
            if comp(uid, bid):
                ban_set.add(uid)
        dic[bid] = list(ban_set)
    find_ban(dic, 0, set(), banned_id)
    answer = len(global_set)
    return answer