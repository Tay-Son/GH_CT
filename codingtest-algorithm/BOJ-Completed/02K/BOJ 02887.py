import sys


def find_(lst_p, idx_):
    temp_ = lst_p[idx_]
    if temp_ != idx_:
        temp_ = find_(lst_p, temp_)
        lst_p[idx_] = temp_
    return temp_


def union_(lst_p, idx_a, idx_b):
    p_a, p_b = find_(lst_p, idx_a), find_(lst_p, idx_b)
    if p_a < p_b:
        lst_p[p_b] = p_a
    else:
        lst_p[p_a] = p_b


N_ = int(sys.stdin.readline())
lst_ = []
lst_p = [idx_ for idx_ in range(N_)]
lst_x = []
lst_y = []
lst_z = []
for idx_ in range(N_):
    X_, Y_, Z_ = map(int, sys.stdin.readline().split())
    lst_x.append((X_, idx_))
    lst_y.append((Y_, idx_))
    lst_z.append((Z_, idx_))

lst_x.sort()
lst_y.sort()
lst_z.sort()

for idx_ in range(N_ - 1):
    lst_.append((lst_x[idx_ + 1][0] - lst_x[idx_][0], lst_x[idx_ + 1][1], lst_x[idx_][1]))
    lst_.append((lst_y[idx_ + 1][0] - lst_y[idx_][0], lst_y[idx_ + 1][1], lst_y[idx_][1]))
    lst_.append((lst_z[idx_ + 1][0] - lst_z[idx_][0], lst_z[idx_ + 1][1], lst_z[idx_][1]))

lst_.sort()

cnt_ = 0
tot_ = 0
idx_lst = 0

while cnt_ < N_ - 1:
    weight_, idx_a, idx_b, = lst_[idx_lst]
    if find_(lst_p, idx_a) != find_(lst_p, idx_b):
        union_(lst_p, idx_a, idx_b)
        cnt_ += 1
        tot_ += weight_
    idx_lst += 1

print(tot_)

exit()
