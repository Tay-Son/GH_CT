import sys

LIM_ = 123456

lst_ip = [True for _ in range(2 * LIM_ + 1)]
lst_ip[0], lst_ip[1] = False, False

for idx_ in range(2, int(len(lst_ip) ** .5)):
    if lst_ip[idx_]:
        for idx_sub in range(idx_ * 2, len(lst_ip), idx_):
            lst_ip[idx_sub] = False

lst_ = [0 for _ in range(len(lst_ip))]
tot_ = 0
for idx_, val_ in enumerate(lst_ip):
    tot_ += int(val_)
    lst_[idx_] = tot_

n_ = int(sys.stdin.readline())
while n_:
    print(lst_[2 * n_] - lst_[n_])
    n_ = int(sys.stdin.readline())
exit()
