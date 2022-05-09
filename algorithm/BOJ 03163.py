import sys

for _ in range(int(sys.stdin.readline())):
    N_, L_, K_ = map(int, sys.stdin.readline().split())
    lst_ = []
    cnt_ = 0

    lst_d_l = []
    lst_d_r = []

    for _ in range(N_):
        pos_, id_ = map(int, sys.stdin.readline().split())
        lst_.append([id_])
        lst_[-1].append(cnt_)
        if 0 < id_:
            lst_d_l.append(L_ - pos_ + 1)
            cnt_ += 1
        else:
            lst_d_r.append(pos_ + 1)
    lst_d_l.sort()
    lst_d_r.sort(reverse=True)
    print(lst_d_r)
    print(lst_d_l)
    print()

    cnt_c = 0
    for idx_ in range(N_ - 1, -1, -1):
        lst_[idx_].append(cnt_c)
        if lst_[idx_][0] < 0:
            cnt_c += 1
        print(lst_[idx_])
    print()

    for idx_ in range(N_):
        id_, cnt_, cnt_c = lst_[idx_]
        if 0 < id_:
            if cnt_ >= cnt_c:
                lst_[idx_].append(lst_d_l.pop())
            else:
                lst_[idx_].append(lst_d_r.pop())

        else:
            if cnt_ > cnt_c:
                lst_[idx_].append(lst_d_l.pop())
            else:
                lst_[idx_].append(lst_d_r.pop())
        print(lst_[idx_])

    lst_.sort(key=lambda x: x[0])
    lst_.sort(key=lambda x: x[-1])
    print(lst_[K_ - 1][0])

exit()
