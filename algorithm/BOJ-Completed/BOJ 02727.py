import sys


def rec_(num_, depth_):
    lst_ret = []
    if num_ == 1:
        lst_ret += [(depth_, 0)]
    elif not num_ % 2:
        lst_ret += rec_(num_ // 2, depth_ + 1)
    else:
        mag_ = 19
        while num_ < 3 ** mag_:
            mag_ -= 1
        lst_ret += [(depth_, mag_)]
        if 3 ** mag_ < num_:
            lst_ret += rec_(num_ - 3 ** mag_, depth_)
    return lst_ret


for _ in range(int(sys.stdin.readline())):
    lst_ans = rec_(int(sys.stdin.readline()), 0)
    print(len(lst_ans))
    for mag_2, mag_3 in lst_ans:
        print(mag_2, mag_3)
exit()
