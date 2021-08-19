def all_A(name):
    for ch in name:
        if ch != "A":
            return False
    return True


def dfs(name, n, pos):
    if (all_A(name)):
        return n
    ppos, npos = pos + 1, pos - 1
    if ppos >= len(name):
        ppos = 0
    if npos < 0:
        npos = len(name) - 1
    dfs(name, n + 1, ppos)
    dfs(name, n + 1, npos)


def solution(name):
    name = list(name)
    answer = 0
    for i in range(0, len(name)):
        if "A" != name[i]:
            answer += min(ord(name[i]) - ord("A"), ord("Z") - ord(name[i]))
    answer += dfs(name, 0, 0)
    return answer