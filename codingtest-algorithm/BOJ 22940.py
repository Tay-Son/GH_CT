    import sys


    def row_c(row_a, row_b, c_):
        for idx_, val_b in enumerate(row_b):
            row_a[idx_] += c_ * val_b
        return row_a


    def row_m(row_, m_):
        for idx_c in range(len(row_)):
            row_[idx_c] *= m_
        return row_


    def GJ_(mat_):
        N_ = len(mat_)
        for idx_r in range(N_):
            mat_[idx_r] += [1 if idx_c == idx_r else 0 for idx_c in range(N_)]

        mat_.sort(key=lambda x: x[:N_], reverse=True)

        for idx_r in range(N_):
            if mat_[idx_r][idx_r] == 1:
                pass
            elif mat_[idx_r][idx_r] == 0:
                return 0
            else:
                mat_[idx_r] = row_m(mat_[idx_r], 1 / mat_[idx_r][idx_r])

            for idx_r_sub in range(idx_r):
                if mat_[idx_r_sub][idx_r]:
                    mat_[idx_r_sub] = row_c(mat_[idx_r_sub], mat_[idx_r], -mat_[idx_r_sub][idx_r] / mat_[idx_r][idx_r])

            for idx_r_sub in range(idx_r + 1, N_):
                if mat_[idx_r_sub][idx_r]:
                    mat_[idx_r_sub] = row_c(mat_[idx_r_sub], mat_[idx_r], -mat_[idx_r_sub][idx_r] / mat_[idx_r][idx_r])

        for each_ in mat_:
            print(each_)

        lst_ = []
        for idx_r in range(N_):
            val_ = mat_[idx_r][N_]
            int_ = int(val_)
            if val_ - int_ > .5:
                int_ += 1
            lst_.append(int_)

        return lst_


    N_ = int(sys.stdin.readline())
    mat_ = [list(map(int, sys.stdin.readline().split())) for _ in range(N_)]
    print(' '.join(map(str, GJ_(mat_))))

    exit()
