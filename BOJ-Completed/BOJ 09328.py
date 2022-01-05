import sys
from collections import deque


def chr_id(chr_):
    return ord(chr_.lower()) - ord('a')


for _ in range(int(sys.stdin.readline())):
    R_, C_ = map(int, sys.stdin.readline().split())
    grd_iv = [[False for _ in range(C_)] for _ in range(R_)]

    que_ = deque()
    grd_door = [[] for _ in range(26)]
    lst_h_k = [False for _ in range(26)]
    tot_ = 0

    grd_ = []
    for idx_r in range(R_):
        row_ = sys.stdin.readline().rstrip()
        for idx_c, val_ in enumerate(row_):
            if ((idx_c in [0, C_ - 1]) or (idx_r in [0, R_ - 1])) and val_ != '*':
                grd_iv[idx_r][idx_c] = True
                if not 'A' <= val_ <= 'Z':
                    que_.append((idx_r, idx_c))
                    if val_ == '$':
                        tot_ += 1
                    elif 'a' <= val_ <= 'z':
                        lst_h_k[chr_id(val_)] = True
                else:
                    grd_door[chr_id(val_)].append((idx_r, idx_c))
        grd_.append(row_)

    str_temp = sys.stdin.readline().rstrip()
    if str_temp != '0':
        for chr_ in str_temp:
            lst_h_k[chr_id(chr_)] = True
            for c_r, c_c in grd_door[chr_id(chr_)]:
                if grd_iv[c_r][c_c]:
                    que_.append((c_r, c_c))

    while que_:
        i_r, i_c = que_.pop()
        for o_r, o_c in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            t_r, t_c = i_r + o_r, i_c + o_c
            if 0 <= t_r < R_ and 0 <= t_c < C_ and not grd_iv[t_r][t_c]:
                chr_ = grd_[t_r][t_c]
                if chr_ == '.':
                    grd_iv[t_r][t_c] = True
                    que_.append((t_r, t_c))

                elif chr_ == '$':
                    grd_iv[t_r][t_c] = True
                    que_.append((t_r, t_c))
                    tot_ += 1

                elif 'a' <= chr_ <= 'z':
                    if not lst_h_k[chr_id(chr_)]:
                        lst_h_k[chr_id(chr_)] = True

                        for c_r, c_c in grd_door[chr_id(chr_)]:
                            if grd_iv[c_r][c_c]:
                                que_.append((c_r, c_c))
                    grd_iv[t_r][t_c] = True
                    que_.append((t_r, t_c))

                elif 'A' <= chr_ <= 'Z':
                    grd_iv[t_r][t_c] = True
                    if lst_h_k[chr_id(chr_)]:
                        que_.append((t_r, t_c))
                    else:
                        grd_door[chr_id(chr_)].append((t_r, t_c))
    print(tot_)
exit()
