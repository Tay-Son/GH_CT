def solution(str_):
    N_ = len(str_)
    max_ = 0

    for idx_ in range(N_):
        offset_ = 0
        while 0 <= idx_ - offset_ - 1 \
                and idx_ + offset_ + 1 < N_ \
                and str_[idx_ - offset_ - 1] == str_[idx_ + offset_ + 1]:
            offset_ += 1
        max_ = max(max_, 2 * offset_ + 1)

    for idx_ in range(N_ - 1):
        offset_ = 0
        while 0 <= idx_ - offset_ \
                and idx_ + offset_ + 1 < N_ \
                and str_[idx_ - offset_] == str_[idx_ + offset_ + 1]:
            offset_ += 1
        max_ = max(max_, 2 * offset_)

    return max_


for str_ in [
    "abcdcba",
    "abacde"
]:
    print(solution(str_))
    print()
