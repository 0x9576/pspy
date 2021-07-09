def solution(numbers):
    lis = []
    answer = ''
    for num in numbers:
        num2 = num / float(10 ** len(str(num)))
        lis.append((num2, num))

    sorted_lis = sorted(lis, key=lambda x: (-x[0], x[1]))
    print(sorted_lis)

    for l in sorted_lis:
        answer += str(l[1])
    return answer