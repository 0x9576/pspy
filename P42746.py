def solution(numbers):
    lis = []
    answer = ''
    for num in numbers:
        num = str(num)
        num2 = num
        for i in range(0 ,3):
            num2 += num
        num2 = num2[:4]
        lis.append((int(num2), num))
    sorted_lis = sorted(lis, key = lambda x : (-x[0]))
    for l in sorted_lis:
        answer += str(l[1])
    return str(int(answer))