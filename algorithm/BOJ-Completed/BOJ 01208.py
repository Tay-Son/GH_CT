import sys

N_, S_ = map(int, sys.stdin.readline().split())
lst_ = list(map(int, sys.stdin.readline().split()))

lst_aux = [0]
for each_ in lst_[:N_ // 2]:
    lst_temp = []
    for aux_ in lst_aux:
        lst_temp.append(aux_)
        lst_temp.append(aux_ + each_)
    lst_aux = lst_temp

dct_l = dict()
for each_ in lst_aux:
    if each_ not in dct_l:
        dct_l[each_] = 1
    else:
        dct_l[each_] += 1

lst_aux = [0]
for each_ in lst_[N_ // 2:]:
    lst_temp = []
    for aux_ in lst_aux:
        lst_temp.append(aux_)
        lst_temp.append(aux_ + each_)
    lst_aux = lst_temp

dct_r = dict()
for each_ in lst_aux:
    if each_ not in dct_r:
        dct_r[each_] = 1
    else:
        dct_r[each_] += 1

tot_ = -1 if not S_ else 0
for val_, cnt_ in dct_l.items():
    print(val_, cnt_)
    if S_ - val_ in dct_r:
        print('   ', S_ - val_, dct_r[S_ - val_])
        tot_ += cnt_ * dct_r[S_ - val_]
print(tot_)

exit()
