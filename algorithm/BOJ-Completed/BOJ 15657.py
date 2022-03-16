import sys

N_, M_ = map(int, sys.stdin.readline().split())
set_ = set(map(int, sys.stdin.readline().split()))
lst_ = sorted(list(set_))

lst_temp = []


def rec_(depth_):
    if depth_ == M_:
        print(' '.join(map(str, [lst_[idx_] for idx_ in lst_temp])))
    else:
        depth_ += 1
        temp_ = lst_temp[-1] if lst_temp else 0
        for idx_ in range(temp_, len(lst_)):
            lst_temp.append(idx_)
            rec_(depth_)
            lst_temp.pop()


rec_(0)

exit()
