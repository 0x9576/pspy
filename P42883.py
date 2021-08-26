def solution(number, k):
    stack = []
    for n in number:
        while stack and k > 0 and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)
    if k:
        stack = stack[:-k]
    answer = ' '.join(stack)
    return answer