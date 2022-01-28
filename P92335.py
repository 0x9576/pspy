def solution(n, k):
    answer = 0
    limit = 50000100
    prime_num = [True for i in range(limit)]
    prime_num[1] = False
    prime_num[0] = False
    for i in range(1, limit):
        if prime_num[i]:
            for j in range(i+i, limit, i):
                prime_num[j] = False
    num_str = ""
    a = 0
    while n >= k:
        a = n % k
        n //= k
        num_str = str(a) + num_str
    num_str = str(n) + num_str

    num_arr = num_str.split("0")
    for num in num_arr:
        if num != "" and prime_num[int(num)]:
            answer += 1
    return answer