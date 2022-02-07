import sys

sys.setrecursionlimit(100000)


def solution(nodeinfo):
    answer = [[], []]
    node_info_pos = []
    for i in range(len(nodeinfo)):
        x = nodeinfo[i][0]
        y = nodeinfo[i][1]
        node_info_pos.append((y, x, i))
    node_info_pos.sort(reverse=True)
    # y좌표 높은 순으로 정렬.
    root = node_info_pos[0][2]
    tree_dict = {root: [-1, -1]}
    for node in node_info_pos:
        if node[2] not in tree_dict:
            insert_node(tree_dict, node[2], nodeinfo, root)
    preorder(root, tree_dict, answer[0])
    postorder(root, tree_dict, answer[1])
    return answer


def insert_node(tree_dict, node, node_info, c_node):
    # 방향확인
    goto = 1
    if node_info[c_node][0] > node_info[node][0]:
        # x좌표가 더 작다면 왼쪽자식 대상임.
        goto = 0
    if tree_dict[c_node][goto] == -1:
        # -1 이라면 아직 그쪽에 자식 노드가 없음을 뜻함.
        tree_dict[c_node][goto] = node
        # 새로운 자식노드 생성
        tree_dict[node] = [-1, -1]
    else:
        # -1 이 아니라면 더 깊이가서 맞는 자리를 찾아야 함.
        insert_node(tree_dict, node, node_info, tree_dict[c_node][goto])


def preorder(node, tree_dict, ans):
    if node == -1:
        return
    ans.append(node + 1)
    preorder(tree_dict[node][0], tree_dict, ans)  # left
    preorder(tree_dict[node][1], tree_dict, ans)  # right


def postorder(node, tree_dict, ans):
    if node == -1:
        return
    postorder(tree_dict[node][0], tree_dict, ans)  # left
    postorder(tree_dict[node][1], tree_dict, ans)  # right
    ans.append(node + 1)