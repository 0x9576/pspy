def solution(n, k, cmd):
    lis = [i for i in range(0, n)]
    answer = ''
    delete_list = []
    for c in cmd:
        if c[0] == "D":
            num = c[1:]
            k += int(num)
        elif c == "C":
            delete_list.append(lis[k])
            del lis[k]
            k = min(k, len(lis) - 1)
        elif c[0] == "U":
            num = c[1:]
            k -= int(num)
        else:
            top = delete_list.pop()
            if top > lis[-1]:
                lis.append(top)
            elif top < lis[0]:
                lis.insert(0, top)
                k += 1
            else:
                for i in range(0, len(lis) - 1):
                    if lis[i] < top < lis[i + 1]:
                        lis.insert(i + 1, top)
                        if i < k:
                            k += 1
                        break
    for i in range(0, n):
        if i in lis:
            answer += "O"
        else:
            answer += "X"
    return answer