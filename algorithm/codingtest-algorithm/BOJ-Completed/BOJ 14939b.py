import sys

lst_bit = []
for num_ in range(1024):
    bin_ = bin(num_)[2:]
    cnt_ = bin_.count('1')
    bit_ = 0
    for idx_, each_ in enumerate(bin_[::-1]):
        if int(each_):
            if 0 < idx_:
                bit_ ^= 1 << (idx_ - 1)
            bit_ ^= 1 << idx_
            if idx_ < 9:
                bit_ ^= 1 << (idx_ + 1)
    lst_bit.append((bit_, cnt_))
#
# for idx_, (bit_, cnt_) in enumerate(lst_bit):
#     print(bin(idx_)[2:], bin(bit_)[2:], cnt_)

lst_ = []
for _ in range(10):
    tot_ = 0
    mag_ = 512
    for chr_ in sys.stdin.readline().strip():
        if chr_ == 'O':
            tot_ += mag_
        mag_ //= 2
    lst_.append(tot_)


#
# print(lst_)


def rec_(cnt_tot, depth_):
    if depth_ == 10:
        if not lst_[depth_ - 1]:
            # print(lst_)
            return cnt_tot
        else:
            return 101
    else:
        min_ = 101
        for num_ in range(1024):
            bit_, cnt_ = lst_bit[num_]
            if (depth_ == 0) or (depth_ != 0 and not lst_[depth_ - 1] ^ num_):
                if depth_ != 0:
                    lst_[depth_ - 1] ^= num_
                lst_[depth_] ^= bit_
                if depth_ != 9:
                    lst_[depth_ + 1] ^= num_
                min_ = min(min_, rec_(cnt_tot + cnt_, depth_ + 1))
                if depth_ != 0:
                    lst_[depth_ - 1] ^= num_
                lst_[depth_] ^= bit_
                if depth_ != 9:
                    lst_[depth_ + 1] ^= num_
        return min_


min_ = rec_(0, 0)
print(min_ if min_ != 101 else -1)

exit()
