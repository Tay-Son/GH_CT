import sys

CEF_ = 17

T_ = int(sys.stdin.readline())
for _ in range(T_):
    N_, M_ = map(int, sys.stdin.readline().split())
    cch_ = 2 ** CEF_
    lst_pos = [cch_ + cnt_ - 1 for cnt_ in range(N_ + 1)]
    tre_ = [0 for _ in range(cch_ * 3)] + [1 for _ in range(cch_)]

    curr_ = 1
    tre_[curr_] = 2 ** CEF_
    curr_ += 1
    for cnt_a in range(0, CEF_):
        curr_ += 2 ** cnt_a
        temp_ = 2 ** (CEF_ - cnt_a)
        for cnt_b in range(2 ** cnt_a):
            tre_[curr_] = temp_
            curr_ += 1
    new_ = cch_ - 1
    lst_ans = []

    for idx_target in map(int, sys.stdin.readline().split()):
        val_temp = lst_pos[idx_target]
        tot_ = 0

        idx_tre = 1
        for cnt_ in range(CEF_, -1, -1):
            idx_tre *= 2

            temp_ = 2 ** cnt_
            if val_temp >= temp_:
                val_temp -= temp_
                tot_ += tre_[idx_tre]
                idx_tre += 1
        lst_ans.append(tot_)

        idx_orig = lst_pos[idx_target] + 2 * cch_
        idx_new = new_ + 2 * cch_
        lst_pos[idx_target] = new_
        new_ -= 1
        tre_[idx_orig] = 0
        tre_[idx_new] = 1

        for _ in range(CEF_):
            idx_orig //= 2
            idx_new //= 2
            tre_[idx_orig] -= 1
            tre_[idx_new] += 1

    print(' '.join(map(str, lst_ans)))

exit()
