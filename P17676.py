def solution(lines):
    answer = 0
    time = []
    for line in lines:
        line_arr = line.split()
        se = get_start_end(line_arr[1], line_arr[2])
        time.append(se)
    for i in range(len(time)):
        count = 0
        for j in range(i, len(time)):
            if time[i][1] > time[j][0] - 1000:
                count += 1
        answer = max(count, answer)
    return answer


def get_start_end(end, processing):
    processing_time = int(float(processing[:-1]) * 1000)
    end_time = str_to_time(end)
    return end_time - processing_time + 1, end_time


def str_to_time(str_time):
    ret = 0
    str_time_arr = str_time.split(':')
    ret += int(str_time_arr[0]) * 3600000  # 시
    ret += int(str_time_arr[1]) * 60000  # 분
    s_ms = str_time_arr[2].split('.')  # 초, 밀리초
    ret += int(s_ms[0]) * 1000  # 초
    ret += int(s_ms[1])  # 밀리초
    return ret