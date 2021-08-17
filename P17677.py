import re

def solution(str1, str2):
    str_arr = [str1, str2]
    answer = 0
    lis_arr = [[], []]
    for k in range(0, 2):
        for i in range(0, len(str_arr[k]) - 1):
            st = str_arr[k][i] + str_arr[k][i + 1]
            st = re.sub('[^A-Za-z]', '', st)
            st = st.lower()
            if len(st) == 2:
                lis_arr[k].append(st)
    print(lis_arr)
    if len(lis_arr[0]) == 0 and len(lis_arr[1]) == 0:
        answer = 1
    else:
        uni, inter = [], []
        for lar in lis_arr[0]+lis_arr[1]:
            if lar not in uni:
                num_max = max(lis_arr[0].count(lar), lis_arr[1].count(lar))
                num_min = min(lis_arr[0].count(lar), lis_arr[1].count(lar))
                uni += [lar for _ in range(0, num_max)]
                inter += [lar for _ in range(0, num_min)]
        answer = len(inter) / len(uni)
    answer = int(answer * 65536)
    return answer