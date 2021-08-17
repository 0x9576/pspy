def solution(n, lost, reserve):
    n -= len(lost)
    lost.sort()
    reserve.sort()
    del_list = []
    for l in lost:
        if l in reserve:
            del reserve[reserve.index(l)]
            del_list.append(l)
            n+=1
    for dl in del_list:
        del lost[reserve.index(dl)]
    for l in lost:
        los = [l-1,l+1]
        for lo in los:
            if lo in reserve:
                del reserve[reserve.index(lo)]
                n += 1
                break
    return n