import sys


def find_(lst_p, idx_):
    temp_ = lst_p[idx_]
    if temp_ != idx_:
        temp_ = find_(lst_p, temp_)
        lst_p[idx_] = temp_
    return temp_


def union_(lst_p, idx_a, idx_b):
    p_a, p_b = find_(lst_p, idx_a), find_(lst_p, idx_b)
    lst_p[p_b] = p_a


N_, M_ = map(int, sys.stdin.readline().split())
lst_p = [idx_ for idx_ in range(N_ + 1)]
lst_ = []
for _ in range(M_):
    idx_a, idx_b, weight_ = map(int, sys.stdin.readline().split())
    lst_.append((weight_, idx_a, idx_b))
lst_.sort()

cnt_ = 0
tot_ = 0
max_ = 0
idx_lst = 0

while cnt_ < N_ - 1:
    weight_, idx_a, idx_b = lst_[idx_lst]
    if find_(lst_p, idx_a) != find_(lst_p, idx_b):
        union_(lst_p, idx_a, idx_b)
        cnt_ += 1
        tot_ += weight_
        max_ = max(max_, weight_)

    idx_lst += 1

print(tot_ - max_)
exit()
