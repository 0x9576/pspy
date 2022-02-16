def solution(n, k, cmd):
    answer = ''
    dll = {0: [-1, 1], n-1: [n - 2, -1]}
    # 양방향 연결리스트
    # 좌: 현재노드, 우: 이전노드, 다음노드
    # 이전, 다음 노드가 없다면 -1로 설정한다.
    deleted_stack = []
    # 삭제된 노드를 저장하는 스택이다.
    for i in range(0, n-2):
        insert(i, i + 2, i + 1, dll)
    for c in cmd:
        print(dll)
        print(k)
        if c[0] == "D":
            for _ in range(int(c[1:])):
                k = dll[k][1]  # 다음노드로 간다.
        elif c[0] == "U":
            for _ in range(int(c[1:])):
                k = dll[k][0]  # 이전 노드로 간다.
        elif c[0] == "C":
            ret = delete(k, dll)
            deleted_stack.append(ret)
            # 복구를 위해서 스택에 삭제된 노드의 정보를 저장한다.
            if ret[2] != -1:
                k = ret[2]  # -1이 아니라면 다음 노드로 변경
            else:
                k = ret[1]  # -1이라면 이전 노드로 변경
        else:
            node = deleted_stack.pop()
            restore(node, dll)

    for i in range(n):
        if i in dll:
            answer += 'O'
        else:
            answer += 'X'

    return answer


def insert(pre, nex, node, dll):
    dll[node] = [pre, nex]


def delete(k, dll):
    # k는 삭제되어야 하는 노드다.
    # 이전 노드와 다음 노드를 dll을 통해서 알아낸다.
    pre_node = dll[k][0]
    next_node = dll[k][1]
    # 이전노드의 다음: 다음노드와 연결
    if pre_node != -1:
        dll[pre_node][1] = next_node
    # 다음 노드의 이전: 이전 노드와 연결
    if next_node != -1:
        dll[next_node][0] = pre_node
    del dll[k]  # 노드삭제
    # 삭제된 노드정보 반환.
    return (k, pre_node, next_node)


def restore(node, dll):
    print(node)
    pre_node = node[1]
    next_node = node[2]
    node = node[0]
    dll[node] = [pre_node, next_node]
    if pre_node != -1:
        dll[pre_node][1] = node
    # 이전 노드의 다음을 복구
    if next_node != -1:
        dll[next_node][0] = node
    # 다음 노드의 이전을 복구
    return
