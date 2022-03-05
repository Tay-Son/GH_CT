lst_m = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
from collections import deque


def solution(lst_p):
    lst_ = []
    for p_ in lst_p:
        date_, price_ = p_.split()
        _, m_, d_ = map(int, date_.split('/'))
        date_ = sum(lst_m[:m_]) + d_
        price_ = int(price_)
        lst_.append((date_, price_))
        lst_.append((date_ + 30, -price_))
    que_ = deque(sorted(lst_))

    lst_answer = [0, 0, 0, 0, 0]
    curr_ = 0

    print(que_)

    for today_ in range(365):
        while que_ and que_[0][0] <= today_:
            _, price_ = que_.popleft()
            curr_ += price_
        if curr_ < 10000:
            state_ = 0
        elif 10000 <= curr_ < 20000:
            state_ = 1
        elif 20000 <= curr_ < 50000:
            state_ = 2
        elif 50000 <= curr_ < 100000:
            state_ = 3
        else:
            state_ = 4
        lst_answer[state_] += 1
    return lst_answer

    #
    # for date_, price_ in sorted(lst_, key=lambda x: x[0]):
    #     print(date_, price_, curr_)
    #     if date_ > sum(lst_m):
    #         break
    #     else:
    #         curr_ += price_
    #         if price_ < 0:
    #             if curr_ < 10000:
    #                 state_temp = 0
    #             elif 10000 <= curr_ < 20000:
    #                 state_temp = 1
    #             elif 20000 <= curr_ < 50000:
    #                 state_temp = 2
    #             elif 50000 <= curr_ < 100000:
    #                 state_temp = 3
    #             else:
    #                 state_temp = 4
    #
    #             if state_ != state_temp:
    #                 lst_answer[state_] += date_ - date_s
    #                 date_s = date_
    #                 state_ = state_temp
    #
    # date_ = sum(lst_m)
    # lst_answer[state_] += date_ - date_s
    #
    # return lst_answer


for lst_p in [
    ["2019/01/01 5000", "2019/01/20 15000", "2019/02/09 90000"],
    ["2019/01/30 5000", "2019/04/05 10000", "2019/06/10 20000", "2019/08/15 50000", "2019/12/01 100000"]
]:
    print(solution(lst_p))
