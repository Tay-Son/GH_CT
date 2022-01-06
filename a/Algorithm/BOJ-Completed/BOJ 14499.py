import sys

R_, C_, c_r, c_c, K_ = map(int, sys.stdin.readline().split())
grd_ = []
for _ in range(R_):
    grd_.append(list(map(int, sys.stdin.readline().split())))

dct_dice = {'U': 0, 'N': 0, 'E': 0, 'W': 0, 'S': 0, 'D': 0}

lst_com = list(map(int, sys.stdin.readline().split()))
for com_ in lst_com:
    if com_ == 1:
        t_r, t_c = c_r, c_c + 1
        if 0 <= t_c < C_:
            c_r, c_c = t_r, t_c
            dct_dice['W'], dct_dice['U'], dct_dice['E'], dct_dice['D'] = \
                dct_dice['D'], dct_dice['W'], dct_dice['U'], dct_dice['E']
            print(dct_dice['U'])
            if not grd_[c_r][c_c]:
                grd_[c_r][c_c] = dct_dice['D']
            else:
                dct_dice['D'] = grd_[c_r][c_c]
                grd_[c_r][c_c] = 0
    elif com_ == 2:
        t_r, t_c = c_r, c_c - 1
        if 0 <= t_c < C_:
            c_r, c_c = t_r, t_c
            dct_dice['W'], dct_dice['U'], dct_dice['E'], dct_dice['D'] = \
                dct_dice['U'], dct_dice['E'], dct_dice['D'], dct_dice['W']
            print(dct_dice['U'])
            if not grd_[c_r][c_c]:
                grd_[c_r][c_c] = dct_dice['D']
            else:
                dct_dice['D'] = grd_[c_r][c_c]
                grd_[c_r][c_c] = 0
    elif com_ == 3:
        t_r, t_c = c_r - 1, c_c
        if 0 <= t_r < R_:
            c_r, c_c = t_r, t_c
            dct_dice['N'], dct_dice['U'], dct_dice['S'], dct_dice['D'] = \
                dct_dice['U'], dct_dice['S'], dct_dice['D'], dct_dice['N']
            print(dct_dice['U'])
            if not grd_[c_r][c_c]:
                grd_[c_r][c_c] = dct_dice['D']
            else:
                dct_dice['D'] = grd_[c_r][c_c]
                grd_[c_r][c_c] = 0
    elif com_ == 4:
        t_r, t_c = c_r + 1, c_c
        if 0 <= t_r < R_:
            c_r, c_c = t_r, t_c
            dct_dice['N'], dct_dice['U'], dct_dice['S'], dct_dice['D'] = \
                dct_dice['D'], dct_dice['N'], dct_dice['U'], dct_dice['S']
            print(dct_dice['U'])
            if not grd_[c_r][c_c]:
                grd_[c_r][c_c] = dct_dice['D']
            else:
                dct_dice['D'] = grd_[c_r][c_c]
                grd_[c_r][c_c] = 0

exit()
