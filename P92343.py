import copy
answer = 0


def solution(info, edges):
    edges_list = []
    for i in range(100):
        edges_list.append([])
    # accessible_list는 현재 갈 수 있는 노드의 리스트를 저장함.
    accessible_list = [0]
    # edges_list는 해당 노드에서 갈 수 있는 노드의 리스트를 저장함.
    for edge in edges:
        edges_list[edge[0]].append(edge[1])
    for root_child in edges_list[0]:
        accessible_list.append(root_child)
    # 시작점은 0(root)임
    find(0, edges_list, info, accessible_list, 0, 0)
    return answer


def find(start, edges_list, info, accessible_list, sheep, wolf):
    accessible_list.remove(start)
    global answer
    # 늑대 및 양 추가
    if info[start] == 0:
        sheep += 1
    else:
        wolf += 1
    if sheep <= wolf:
        return
    # answer = 최대로 모을 수 있는 양의 마릿수
    answer = max(answer, sheep)
    # 지금 노드에서 갈 수 있는 노드를 추가
    for destination in edges_list[start]:
        if destination not in accessible_list:
            accessible_list.append(destination)
    # 갈 수 있는 모든 노드에 하나씩 접근함.
    for s in accessible_list:
        # deepcopy를 써서 리스트의 얕은복사를 막음
        new_list = copy.deepcopy(accessible_list)
        find(s, edges_list, info, new_list, sheep, wolf)