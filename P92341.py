import math


def solution(fees, records):
    time = {}
    total_time = {}
    car_nums = []
    answer = []

    for record in records:
        record_arr = record.split()
        # 차번호 저장
        if record_arr[1] not in car_nums:
            car_nums.append(record_arr[1])
        # 입차 저장
        if record_arr[1] not in time:
            time[record_arr[1]] = record_arr[0]
        else: # 입차가 되어있다면 -> 출차임.
            if record_arr[1] not in total_time:
                total_time[record_arr[1]] = 0  # 첫 출차라면 딕셔너리에 등록
            total_time[record_arr[1]] += get_gap_minute(record_arr[0], time[record_arr[1]])
            # 일단은 총 시간만 계산해준다.
            del time[record_arr[1]]
            # 입차내역에서 삭제

    for key in time: # 23:59까지 출차하지 않은 차들 계산
        if key not in total_time:
            total_time[key] = 0  # 첫 출차라면 딕셔너리에 등록
        total_time[key] += get_gap_minute("23:59", time[key])
    car_nums.sort()
    for car_num in car_nums:
        answer.append(calculate_fee(total_time[car_num], fees))
    return answer


def get_gap_minute(out_time, in_time):  # 시간 문자열을 분단위 정수로 변환해줌.
    arr_out_time = out_time.split(':')
    arr_in_time = in_time.split(':')
    return (int(arr_out_time[0])-int(arr_in_time[0])) \
           * 60 + (int(arr_out_time[1])-int(arr_in_time[1]))


def calculate_fee(duration, fees):
    # 경과 시간을 넣으면, 요금을 반환.
    if fees[0] >= duration:
        return fees[1]
    else:
        total_fee = fees[1]
        total_fee += math.ceil((duration - fees[0]) / fees[2]) * fees[3]
        return total_fee

