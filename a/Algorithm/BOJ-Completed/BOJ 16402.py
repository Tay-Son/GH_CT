import sys

N_, M_ = map(int, sys.stdin.readline().split())
lst_p = [idx_ for idx_ in range(N_)]


def find(idx_):
    temp_ = lst_p[idx_]
    if temp_ != idx_:
        temp_ = find(temp_)
        lst_p[idx_] = temp_
    return temp_


def conquer(idx_c, idx_s):
    if find(idx_c) == idx_s:
        lst_p[idx_c] = idx_c
        lst_p[idx_s] = idx_c
    else:
        lst_p[find(idx_s)] = find(idx_c)


dct_idx = dict()
dct_kd = dict()
for idx_ in range(N_):
    str_kingdom = sys.stdin.readline().rstrip()
    dct_idx[str_kingdom[11:]] = idx_
    dct_kd[idx_] = str_kingdom

for _ in range(M_):
    lst_str = sys.stdin.readline().split(',')
    idx_a = dct_idx[lst_str[0][11:]]
    idx_b = dct_idx[lst_str[1][11:]]
    if int(lst_str[2]) == 1:
        conquer(idx_a, idx_b)
    else:
        conquer(idx_b, idx_a)

lst_ = []
for idx_ in range(N_):
    if find(idx_) == idx_:
        lst_.append(dct_kd[idx_])
lst_.sort()
print(len(lst_))
for each_ in lst_:
    print(each_)
exit()
