from itertools import permutations

def is_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    perm = []
    for i in range(1, len(numbers) + 1):
        perm += list(permutations(numbers, i))
    print(perm)
    s = set()
    for p in perm:
        num = int(''.join(p))
        if num not in s:
            s.add(num)
            if is_prime(num):
                answer += 1
    return answer