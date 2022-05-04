import datetime

lst_wd = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']


def solution(a, b):
    dt_ = datetime.date(2016, a, b)
    print(dt_)
    return lst_wd[(dt_.weekday()) % 7]
