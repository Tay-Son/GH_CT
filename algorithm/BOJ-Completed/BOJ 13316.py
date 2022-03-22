import sys

N_ = int(sys.stdin.readline())
lst_ = [0 for _ in range(2 ** N_)]
for level_ in range(N_):
    num_ = 2 ** (N_ - level_ - 1)
    cch_ = 2 ** (N_ - level_)
    offset_ = 2 ** level_
    if level_ % 2:
        for idx_ in range(offset_, offset_ + 2 ** (level_)):
            lst_[idx_] = num_
            num_ += cch_
    else:
        for idx_ in range(offset_ + 2 ** (level_) - 1, offset_ - 1, -1):
            lst_[idx_] = num_
            num_ += cch_

lst_answer = []


def rec_(idx_, depth_):
    lst_answer.append(lst_[idx_])
    if depth_ < N_:
        depth_ += 1
        rec_(2 * idx_, depth_)
        rec_(2 * idx_ + 1, depth_)


rec_(1, 1)
print(' '.join(map(str, lst_answer)))
exit()
