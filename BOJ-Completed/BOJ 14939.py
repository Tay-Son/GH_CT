import sys

grd_ = [[1 if each_ == 'O' else 0 for each_ in list(sys.stdin.readline().rstrip())] for _ in range(10)]

for each_ in grd_:
    print(each_)

def rec_(cnt_, tot_):
    print(cnt_,tot_)
    if cnt_ == 100:
        if not sum([sum(each_) for each_ in grd_]):
            print('tot')
            return tot_
        else:
            return 101
    else:
        r_, c_ = divmod(cnt_, 10)

        if r_ >= 2 and sum(grd_[r_ - 2]):
            # print(sum(grd_[r_ - 2]))
            return 101
        else:
            min_ = rec_(cnt_ + 1, tot_)

            c_ = grd_[r_][c_]
            if r_ != 0:
                c_ += grd_[r_ - 1][c_]
            if r_ != 9:
                c_ += grd_[r_ + 1][c_]
            if c_ != 0:
                c_ += grd_[r_][c_ - 1]
            if c_ != 9:
                c_ += grd_[r_][c_ + 1]

            if c_:
                grd_[r_][c_] = 0 if grd_[r_][c_] else 1
                if r_ != 0:
                    grd_[r_ - 1][c_] = 0 if grd_[r_ - 1][c_] else 1
                if r_ != 9:
                    grd_[r_ + 1][c_] = 0 if grd_[r_ + 1][c_] else 1
                if c_ != 0:
                    grd_[r_][c_ - 1] = 0 if grd_[r_][c_ - 1] else 1
                if c_ != 9:
                    grd_[r_][c_ + 1] = 0 if grd_[r_][c_ + 1] else 1

                min_ = min(min_, rec_(cnt_ + 1, tot_ + 1))

                grd_[r_][c_] = 0 if grd_[r_][c_] else 1
                if r_ != 0:
                    grd_[r_ - 1][c_] = 0 if grd_[r_ - 1][c_] else 1
                if r_ != 9:
                    grd_[r_ + 1][c_] = 0 if grd_[r_ + 1][c_] else 1
                if c_ != 0:
                    grd_[r_][c_ - 1] = 0 if grd_[r_][c_ - 1] else 1
                if c_ != 9:
                    grd_[r_][c_ + 1] = 0 if grd_[r_][c_ + 1] else 1

            return min_


tot_ = rec_(0, 0)
print(tot_ if not tot_ == 101 else -1)

exit()

import sys

grd_ = [[1 if each_ == 'O' else 0 for each_ in list(sys.stdin.readline().rstrip())] for _ in range(10)]

exit()