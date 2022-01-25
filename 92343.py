answer = 0


def solution(info, edges):
    edges_dict = {}
    accessible_set = set()
    accessible_set.add(0)
    for edge in edges:
        if edge[0] not in edges_dict:
            edges_dict[edge[0]] = []
        edges_dict[edge[0]].append(edge[1])
    for root_child in edges_dict[0]:
        accessible_set.add(root_child)
    print(accessible_set)
    find(0, edges_dict, info, accessible_set, 0)
    return answer


def find(start, edges_dict, info, accessible_set, score):
    global answer
    if info[start] == 0:
        score += 1
    else:
        score -= 1
    if score <= 0:
        return
    answer = max(answer, score)
    accessible_set.remove(start)
    for destination in edges_dict[start]:
        accessible_set.add(destination)
    for start in accessible_set:
        find(start, edges_dict, info, accessible_set, score)

solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])