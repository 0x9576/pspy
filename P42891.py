def solution(food_times, k):
    answer = 0
    ft_len = len(food_times)
    ft = []
    for i in range(0, ft_len):
        ft.append((food_times[i], i))
    sorted_ft = sorted(ft, reverse=True)
    while k >= sorted_ft[-1][0] * ft_len:
        k -= sorted_ft[-1][0] * ft_len
        sorted_ft.pop()

    sorted_ft = sorted(sorted_ft, key=lambda x: x[1])
    while 1:
        top = (sorted_ft[0][0] - 1, sorted_ft[0][1])
        sorted_ft = sorted_ft[1:-1]
        if top[0] > 0:
            sorted_ft.append(top)
        k -= 1
        if k == 0:
            break
        if not sorted_ft:
            break

    if sorted_ft:
        answer = sorted_ft[0][1] + 1
    else:
        answer = -1
    return answer
