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


N_ = int(sys.stdin.readline())
lst_p = [idx_ for idx_ in range(N_ + 1)]
lst_ = []
for _ in range(int(sys.stdin.readline())):
    idx_a, idx_b, weight_ = map(int, sys.stdin.readline().split())
    lst_.append((weight_, idx_a, idx_b))
lst_.sort()

cnt_ = 0
tot_ = 0
ptr_lst = 0

while cnt_ < N_ - 1:
    weight_, idx_a, idx_b = lst_[ptr_lst]
    if idx_a != idx_b and find_(lst_p, idx_a) != find_(lst_p, idx_b):
        union_(lst_p, idx_a, idx_b)
        cnt_ += 1
        tot_ += weight_
    ptr_lst += 1

print(tot_)

exit()
