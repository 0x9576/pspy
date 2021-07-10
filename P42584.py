def solution(prices):
    size = len(prices)
    answer = [0 for i in range(size)]
    stack = []
    for i in range(0, size):
        answer[i] = len(prices) - i -1

    for i in range(size):
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            answer[top] = i - top
        stack.append(i)
    return answer