import sys

N_, M_ = map(int, sys.stdin.readline().split())

lst_do = [0 for _ in range(N_)]
lst_su = [0 for _ in range(N_)]
for idx_ in range(N_ - 1, -1, -1):
    c_do, c_su = map(int, sys.stdin.readline().split())
    lst_do[idx_] = c_do
    lst_su[idx_] = c_su
#

is_do_win = 2
grd_do = []
grd_su = []
ptr_do = 0
ptr_su = 0
for count_ in range(M_):
    if count_ % 2 == 0:
        grd_do.append(lst_do[ptr_do])
        ptr_do += 1
        if ptr_do >= len(lst_do):
            is_do_win = -1
            break
    else:
        grd_su.append(lst_su[ptr_su])
        ptr_su += 1
        if ptr_su >= len(lst_su):
            is_do_win = 1
            break

    if (grd_do and grd_do[-1] == 5) or (grd_su and grd_su[-1] == 5):
        lst_do += grd_su + grd_do
        grd_do = []
        grd_su = []
    elif grd_do and grd_su and grd_do[-1] + grd_su[-1] == 5:
        lst_su += grd_do + grd_su
        grd_do = []
        grd_su = []

if is_do_win == 2:
    temp_ = (len(lst_do) - ptr_do) - (len(lst_su) - ptr_su)
    if temp_ > 0:
        is_do_win = 1
    elif temp_ == 0:
        is_do_win = 0
    else:
        is_do_win = -1

if is_do_win == 1:
    print('do')
elif is_do_win == -1:
    print('su')
elif is_do_win == 0:
    print('dosu')

exit()