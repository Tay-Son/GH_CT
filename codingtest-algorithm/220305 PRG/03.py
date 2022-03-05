from collections import deque


def func_h(input_, idx_, d_):
    c_ = input_ & (0b1111 << (4 * idx_))
    input_ -= c_
    if d_:
        c_ = ((c_ % (2 ** 3)) << 1) + ((0b1 << (4 * idx_)) if c_ & (0b1000 << (4 * idx_)) else 0)
    else:
        c_ = (c_ >> 1) + ((0b1000 << (4 * idx_)) if c_ & (0b1 << (4 * idx_)) else 0)
    return input_ + c_


def func_v(input_, idx_, d_):
    c_ = input_ & (0b1000100010001 << idx_)
    input_ -= c_
    if d_:
        c_ = ((c_ % (2 ** 11)) << 4) + ((0b1 << idx_) if c_ & (0b1000000000000 << idx_) else 0)
    else:
        c_ = (c_ >> 4) + ((0b1000000000000 << idx_) if c_ & (0b1 << idx_) else 0)
    return input_ + c_


def solution(grd_):
    lst_iv = [False for _ in range(2 ** 16)]

    state_ = 0
    mag_ = 1
    for each_lst in grd_[::-1]:
        for each_ in each_lst[::-1]:
            if each_ == 2:
                state_ += mag_
            mag_ *= 2

    que_ = deque()
    que_.append((state_, 0))
    while que_ and que_[0][0] != 0b00110011110011:
        state_, distance_ = que_.popleft()
        # print('0' * (16 - len(bin(state_)[2:])) + bin(state_)[2:], distance_, state_)
        if not lst_iv[state_]:
            lst_iv[state_] = distance_
            distance_ += 1
            for idx_ in range(4):
                que_.append((func_h(state_, idx_, True), distance_))
                que_.append((func_h(state_, idx_, False), distance_))
                que_.append((func_v(state_, idx_, True), distance_))
                que_.append((func_v(state_, idx_, False), distance_))
    #     break
    #
    # for state_, distance_ in que_:
    #     print('0' * (16 - len(bin(state_)[2:])) + bin(state_)[2:], distance_, state_)

    return que_[0][1]


for grd_ in [
    [[1, 1, 1, 1], [2, 1, 2, 2], [2, 2, 2, 1], [1, 1, 2, 2]],
    # [[1, 1, 1, 2], [1, 1, 1, 2], [2, 2, 2, 1], [1, 2, 2, 2]]
]:
    print(solution(grd_))
