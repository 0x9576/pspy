import copy
answer = 0


def solution(info, edges):
    edges_dict = {}
    accessible_list = [0]
    for edge in edges:
        if edge[0] not in edges_dict:
            edges_dict[edge[0]] = []
        edges_dict[edge[0]].append(edge[1])
    for root_child in edges_dict[0]:
        accessible_list.append(root_child)
    find(0, edges_dict, info, accessible_list, 0)
    return answer


def find(start, edges_dict, info, accessible_list, score):
    accessible_list.remove(start)
    global answer
    if info[start] == 0:
        score += 1
    else:
        score -= 1
    if score <= 0:
        return
    answer = max(answer, score)
    for destination in edges_dict[start]:
        if destination not in accessible_list:
            accessible_list.append(destination)
    for s in accessible_list:
        new_list = copy.deepcopy(accessible_list)
        find(s, edges_dict, info, new_list, score)

solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])