import sys

sys.setrecursionlimit(100009)


def idx_(in_):
    return abs(in_) * 2 + int(in_ > 0) - 2


def dfs_(idx_s, grp_, lst_iv, lst_):
    lst_iv[idx_s] = True
    for idx_e in grp_[idx_s]:
        if not lst_iv[idx_e]:
            dfs_(idx_e, grp_, lst_iv, lst_)
    lst_.append(idx_s)


N_, M_ = map(int, sys.stdin.readline().split())

grp_f = [[] for _ in range(N_ * 2)]
grp_r = [[] for _ in range(N_ * 2)]
for _ in range(M_):
    c_a, c_b = map(int, sys.stdin.readline().split())
    t_a, t_b = -c_a, -c_b

    grp_f[idx_(t_a)].append(idx_(c_b))
    grp_f[idx_(t_b)].append(idx_(c_a))
    grp_r[idx_(c_b)].append(idx_(t_a))
    grp_r[idx_(c_a)].append(idx_(t_b))

for idx_ in range(N_ * 2):
    grp_f[idx_].sort()
    grp_r[idx_].sort()

lst_iv = [False for _ in range(N_ * 2)]
stk_ = []
for idx_s in range(N_ * 2):
    if not lst_iv[idx_s]:
        dfs_(idx_s, grp_f, lst_iv, stk_)

is_ = True
lst_iv = [False for _ in range(N_ * 2)]
grd_ = []
while stk_:
    idx_s = stk_.pop()
    lst_temp = []
    if not lst_iv[idx_s]:
        dfs_(idx_s, grp_r, lst_iv, lst_temp)
    lst_temp.sort()
    ptr_ = 0
    print(lst_temp)
    while ptr_ < len(lst_temp) - 1:
        temp_ = lst_temp[ptr_]
        if not temp_ % 2:
            if temp_ + 1 == lst_temp[ptr_ + 1]:
                is_ = False
                break
        ptr_ += 1
    grd_.append(lst_temp)
    if not is_:
        break

print(int(is_))
if is_:
    lst_iv = [-1 for _ in range(N_)]
    for lst_ in grd_:
        print(lst_)
        for each_ in lst_:
            idx_target = each_ // 2
            if lst_iv[idx_target] == -1:
                if each_ % 2:
                    lst_iv[idx_target] = 0
                else:
                    lst_iv[idx_target] = 1
            else:
                break

    print(' '.join(map(str, lst_iv)))
exit()
