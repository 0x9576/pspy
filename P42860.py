def all_A(name, visited):
    for i in range(0, len(name)):
        if name[i] != "A" and visited[i] == 0:
            return False
    return True


def solution(name):
    answer = 0
    size = len(name)
    for i in range(0, size):
        if "A" != name[i]:
            answer += min(ord(name[i]) - ord("A"), ord("Z") - ord(name[i]) + 1)
    pos = 0
    visited = [0 for _ in range(0, size)]
    visited[0] = 1

    for i in range(0, len(name)):
        if name[i] == "A":
            visited[i] = 1
    while 1:
        if all_A(name, visited):
            return answer
        left, right = pos, pos
        cnt = 0
        while 1:
            left -= 1
            right += 1
            if left < 0:
                left = size - 1
            if right >= size:
                right = 0
            cnt += 1
            if visited[right] == 0:
                visited[right] = 1
                answer += cnt
                pos = right
                break
            if visited[left] == 0:
                visited[left] = 1
                answer += cnt
                pos = left
                break
    return answer