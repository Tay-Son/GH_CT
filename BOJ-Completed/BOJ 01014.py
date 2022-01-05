import sys

grd_aux = [[0, 1]]
for C_ in range(1, 10):
    lst_temp = []
    for num_ in range(2 ** C_, 2 ** (C_ + 1)):
        if not (num_ << 1 & num_) + (num_ >> 1 & num_):
            lst_temp.append(num_)
    grd_aux.append(lst_temp)

for _ in range(int(sys.stdin.readline())):
    R_, C_ = map(int, sys.stdin.readline().split())
    P_ = 2 ** C_

    lst_chr = []
    for idx_r in range(R_):
        lst_chr.append(int('0b' + ''.join(['0' if each_ == '.' else '1' for each_ in sys.stdin.readline().strip()]), 2))

    ans_ = 0
    grd_dp = [[0 for _ in range(P_)] for _ in range(R_)]
    for idx_c in range(C_):
        for num_ in grd_aux[idx_c]:
            if not num_ & lst_chr[0]:
                temp_ = sum(map(lambda x: int(x), bin(num_)[2:]))
                ans_ = max(ans_, temp_)
                grd_dp[0][num_] = temp_

    for idx_r in range(1, R_):
        for idx_c in range(C_):
            for num_a in grd_aux[idx_c]:
                max_ = 0
                if not num_a & lst_chr[idx_r]:
                    for idx_c_sub in range(C_):
                        for num_b in grd_aux[idx_c_sub]:
                            if not (num_b << 1 & num_a) + (num_b >> 1 & num_a):
                                temp_ = grd_dp[idx_r - 1][num_b] + sum(map(lambda x: int(x), bin(num_a)[2:]))
                                max_ = max(max_, temp_)
                grd_dp[idx_r][num_a] = max_
                ans_ = max(ans_, max_)

    print(ans_)

    for each_ in grd_dp:
        print(each_)
    print()

exit()
