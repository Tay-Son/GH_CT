import sys
sys.setrecursionlimit(100009)

V_, E_ = map(int, sys.stdin.readline().split())
grp_f = [[] for _ in range(V_ + 1)]
grp_r = [[] for _ in range(V_ + 1)]
for _ in range(E_):
    idx_s, idx_e = map(int, sys.stdin.readline().split())
    grp_f[idx_s].append(idx_e)
    grp_r[idx_e].append(idx_s)

for idx_s in range(1, V_ + 1):
    grp_f[idx_s].sort()

lst_iv = [False for _ in range(V_ + 1)]
stk_ = []


def dfs_(idx_s, grp_, lst_):
    lst_iv[idx_s] = True
    for idx_e in grp_[idx_s]:
        if not lst_iv[idx_e]:
            dfs_(idx_e, grp_, lst_)
    lst_.append(idx_s)


for idx_s in range(1, V_ + 1):
    if not lst_iv[idx_s]:
        dfs_(idx_s, grp_f, stk_)

tot_ = 0
lst_iv = [False for _ in range(V_ + 1)]
grd_ = []
while stk_:
    lst_temp = []
    idx_s = stk_.pop()
    if not lst_iv[idx_s]:
        tot_ += 1
        dfs_(idx_s, grp_r, lst_temp)
    if lst_temp:
        grd_.append(sorted(lst_temp))
grd_.sort(key=lambda x: x[0])
print(tot_)
for lst_ in grd_:
    print(' '.join(map(str, lst_)) + " -1")

exit()
