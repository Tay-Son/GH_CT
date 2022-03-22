import sys

R_, C_ = map(int, sys.stdin.readline().split())
grd_ = []
lst_W = []
for idx_r in range(R_):
    lst_temp = []
    for idx_c, chr_ in enumerate(sys.stdin.readline().rstrip()):
        if chr_ == 'W':
            lst_W.append((idx_r, idx_c))

        if chr_ == '.':
            lst_temp.append('D')
        else:
            lst_temp.append(chr_)
    grd_.append(''.join(lst_temp))

for idx_r, idx_c in lst_W:
    for o_r, o_c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        t_r, t_c = idx_r + o_r, idx_c + o_c
        if 0 <= t_r < R_ and 0 <= t_c < C_:
            if grd_[t_r][t_c] == 'S':
                print(0)
                break
else:
    print(1)
    for each_ in grd_:
        print(each_)

exit()
