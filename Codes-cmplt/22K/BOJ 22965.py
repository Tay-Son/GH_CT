import sys

N_ = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))
lst_t = [0 for _ in range(200001)]

for idx_ in range(N_):
    idx_t = lst_[idx_]
    lst_t[idx_t] = idx_

lst_sub = [0 for _ in range(N_)]
lst_.sort()
for idx_ in range(N_):
    idx_t = lst_[idx_]
    idx_sub = lst_t[idx_t]
    lst_sub[idx_sub] = idx_

K_ = 1
for idx_ in range(N_ - 1):
    if lst_sub[idx_] + 1 != lst_sub[idx_ + 1]:
        if K_ > 2:
            break
        else:
            K_ += 1
print(K_)

exit()
