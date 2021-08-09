import sys

N_ = int(sys.stdin.readline())
grd_ = []

for _ in range(N_):
    grd_.append(list(map(lambda x: 'B' if x == '.' else x, sys.stdin.readline().rstrip())))

for idx_n in range(N_):
    is_c = False
    for idx_m in range(N_):
        temp_ = grd_[idx_n][idx_m]
        if is_c:
            if temp_ == 'B':
                grd_[idx_n][idx_m] = '.'
            elif temp_ == 'X':
                is_c = False
        elif temp_ == 'O':
            is_c = True
    for idx_m in range(N_ - 1, -1, -1):
        temp_ = grd_[idx_n][idx_m]
        if is_c:
            if temp_ == 'B':
                grd_[idx_n][idx_m] = '.'
            elif temp_ == 'X':
                is_c = False
        elif temp_ == 'O':
            is_c = True

for idx_m in range(N_):
    is_c = False
    for idx_n in range(N_):
        temp_ = grd_[idx_n][idx_m]
        if is_c:
            if temp_ == 'B':
                grd_[idx_n][idx_m] = '.'
            elif temp_ == 'X':
                is_c = False
        elif temp_ == 'O':
            is_c = True
    for idx_n in range(N_ - 1, -1, -1):
        temp_ = grd_[idx_n][idx_m]
        if is_c:
            if temp_ == 'B':
                grd_[idx_n][idx_m] = '.'
            elif temp_ == 'X':
                is_c = False
        elif temp_ == 'O':
            is_c = True

for each_ in grd_:
    print(''.join(each_))

exit()