import sys

N_ = int(sys.stdin.readline()) - 1
lst_d = list(map(int, sys.stdin.readline().split()))
lst_p = list(map(int, sys.stdin.readline().split()[:-1]))

tot_ = 0
lst_temp = [0]
for d_ in lst_d:
    tot_ += d_
    lst_temp.append(tot_)
lst_d = lst_temp

lst_ = [(lst_p[idx_], lst_d[idx_], idx_) for idx_ in range(N_)]

tot_ = 0
cle_ = N_
for p_, d_, i_ in sorted(lst_):
    if i_ < cle_:
        tot_ += p_ * (lst_d[cle_] - d_)
        cle_ = i_

print(tot_)

print(lst_d)
print(lst_p)

exit()
