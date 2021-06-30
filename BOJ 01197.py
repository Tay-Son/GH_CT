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


V_, E_ = map(int, sys.stdin.readline().split())
lst_p = [idx_ for idx_ in range(V_ + 1)]
lst_ = list()

for _ in range(E_):
    A_, B_, C_ = map(int, sys.stdin.readline().split())
    lst_.append((C_, A_, B_))
lst_.sort()

tot_ = 0
cnt_ = 0
ptr_lst = 0

while cnt_ < V_ - 1:
    weight_, idx_a, idx_b = lst_[ptr_lst]
    if find_(lst_p, idx_a) != find_(lst_p, idx_b):
        union_(lst_p, idx_a, idx_b)
        tot_ += weight_
        cnt_ += 1
    ptr_lst += 1
print(tot_)

exit()
