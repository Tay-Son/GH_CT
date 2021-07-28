import sys


def func_(W_, ptr_s, lst_N_a, lst_N_b, lst_sa, lst_sb, lst_sc):
    for idx_ in range(ptr_s, len(lst_N_a)):
        lst_sa[idx_ + 1] = min(lst_sb[idx_] + 1, lst_sc[idx_] + 1)
        if lst_N_a[idx_] + lst_N_b[idx_] <= W_:
            lst_sa[idx_ + 1] = min(lst_sa[idx_ + 1], lst_sa[idx_] + 1)
        if idx_ != 0 \
                and lst_N_a[idx_ - 1] + lst_N_a[idx_] <= W_ \
                and lst_N_b[idx_ - 1] + lst_N_b[idx_] <= W_:
            lst_sa[idx_ + 1] = min(lst_sa[idx_ + 1], lst_sa[idx_ - 1] + 2)
        if idx_ != len(lst_N_a) - 1:
            lst_sb[idx_ + 1] = lst_sa[idx_ + 1] + 1
            if lst_N_a[idx_ + 1] + lst_N_a[idx_] <= W_:
                lst_sb[idx_ + 1] = min(lst_sb[idx_ + 1], lst_sc[idx_] + 1)
            lst_sc[idx_ + 1] = lst_sa[idx_ + 1] + 1
            if lst_N_b[idx_ + 1] + lst_N_b[idx_] <= W_:
                lst_sc[idx_ + 1] = min(lst_sc[idx_ + 1], lst_sb[idx_] + 1)


for _ in range(int(sys.stdin.readline())):
    N_, W_ = map(int, sys.stdin.readline().split())
    lst_N_a = list(map(int, sys.stdin.readline().split()))
    lst_N_b = list(map(int, sys.stdin.readline().split()))

    lst_sa = [0 for _ in range(N_ + 1)]
    lst_sb = [0 for _ in range(N_ + 1)]
    lst_sc = [0 for _ in range(N_ + 1)]
    lst_sb[0] = 1
    lst_sc[0] = 1

    func_(W_, 0, lst_N_a, lst_N_b, lst_sa, lst_sb, lst_sc)
    min_ = lst_sa[N_]

    if N_ > 1:
        if lst_N_a[0] + lst_N_a[N_ - 1] <= W_:
            lst_sa[1] = 1
            lst_sb[1] = 2
            if lst_N_b[0] + lst_N_b[1] <= W_:
                lst_sc[1] = 1
            else:
                lst_sc[1] = 2
            func_(W_, 1, lst_N_a, lst_N_b, lst_sa, lst_sb, lst_sc)
            min_ = min(min_, lst_sc[N_ - 1] + 1)
        if lst_N_b[0] + lst_N_b[N_ - 1] <= W_:
            lst_sa[1] = 1
            lst_sc[1] = 2
            if lst_N_a[0] + lst_N_a[1] <= W_:
                lst_sb[1] = 1
            else:
                lst_sb[1] = 2
            func_(W_, 1, lst_N_a, lst_N_b, lst_sa, lst_sb, lst_sc)
            min_ = min(min_, lst_sb[N_ - 1] + 1)
        if lst_N_a[0] + lst_N_a[N_ - 1] <= W_ and lst_N_b[0] + lst_N_b[N_ - 1] <= W_:
            lst_sa[1] = 0
            lst_sb[1] = 1
            lst_sc[1] = 1

            func_(W_, 1, lst_N_a, lst_N_b, lst_sa, lst_sb, lst_sc)
            min_ = min(min_, lst_sa[N_ - 1] + 2)
    print(min_)

exit()
