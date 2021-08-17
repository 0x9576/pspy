def solution(citations):
    answer = 0
    citations.sort()
    size = len(citations)
    print(citations)
    for i in range(0, 1001):
        if i in citations:
            idx = citations.index(i)
            if size - idx >= i >= idx+1:
                print(size-idx, i , idx+1)
                answer = i
    return answer