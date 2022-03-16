def solution(N_, T_, M_, lst_time):
    lst_temp = []
    for time_ in lst_time:
        h_, m_ = time_.split(':')
        lst_temp.append(int(m_) + int(h_) * 60)
    lst_time = lst_temp
    lst_time.sort()

    ptr_wait = -1
    ptr_take = -1
    max_ = min(540, lst_time[0] - 1)

    for time_bus in range(540, 540 + T_ * N_, T_):
        while ptr_wait + 1 < len(lst_time) and lst_time[ptr_wait + 1] <= time_bus:
            ptr_wait += 1
        on_station = ptr_wait - ptr_take
        ptr_take += min(on_station, M_)
        if on_station < M_:
            max_ = max(max_, time_bus)
        else:
            max_ = max(max_, lst_time[ptr_take] - 1)
    h_, m_ = map(str, divmod(max_, 60))
    str_answer = '0' * (2 - len(h_)) + h_ + ':' + '0' * (2 - len(m_)) + m_

    return str_answer

    ptr_wait = 0
    ptr_take = 0
    max_ = min(lst_time[0] - 1, 540)

    for time_bus in range(540, 540 + T_ * (N_ - 1), T_):
        while ptr_wait < len(lst_time) and lst_time[ptr_wait] <= time_bus:
            ptr_wait += 1
        on_station = ptr_wait - ptr_take
        ptr_take += min(on_station, M_)
        if on_station < M_:
            max_ = max(max_, time_bus)
        elif ptr_take < len(lst_time):
            max_ = max(max_, lst_time[ptr_take] - 1)

    time_bus = 540 + T_ * (N_ - 1)
    while ptr_wait < len(lst_time) and lst_time[ptr_wait] <= time_bus:
        ptr_wait += 1
    on_station = ptr_wait - ptr_take
    if on_station >= M_:
        max_ = max(max_, lst_time[ptr_take + M_ - 1] - 1)
    else:
        max_ = max(max_, time_bus)

    h_, m_ = map(str, divmod(max_, 60))
    str_answer = '0' * (2 - len(h_)) + h_ + ':' + '0' * (2 - len(m_)) + m_

    return str_answer


print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
