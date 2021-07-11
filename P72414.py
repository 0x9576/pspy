def time_to_sec (time):
    tr = time.split(':')
    return int(tr[0])*3600 + int(tr[1])*60 + int(tr[2])

def sec_to_time (sec):
    time = [sec // 3600]
    sec %= 3600
    time.append(sec // 60)
    sec %= 60
    time.append(sec)
    ret = ""
    for t in time:
        if t < 10:
            ret += "0" + str(t) + ":"
        else:
            ret += str(t) + ":"
    return ret[:-1]

def solution(play_time, adv_time, logs):
    play_sec = time_to_sec(play_time)
    adv_sec = time_to_sec(adv_time)
    time = [0 for i in range(play_sec+2)]
    for l in logs:
        log = l.split("-")
        time[time_to_sec(log[0])+1] += 1
        time[time_to_sec(log[1])+1] += -1
    for i in range(0,play_sec+1):
        time[i+1] += time[i]
    for i in range(0,play_sec+1):
        time[i+1] += time[i]
    k,answer = 0, 0
    max_watch = -1
    while adv_sec + k <= play_sec:
        t = time[adv_sec + k] - time[k]
        if max_watch < t:
            max_watch = t
            answer = k
        k += 1
    return sec_to_time(answer)