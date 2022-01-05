import sys

Q_, W_ = map(int, sys.stdin.readline().split())
C_, V_ = map(int, sys.stdin.readline().split())

lst_ = []
for _ in range(W_):
    lst_.append(tuple(map(int, sys.stdin.readline().split())))
lst_.sort(key=lambda x: -x[2])

lst_p = [idx_ for idx_ in range(Q_)]


def find(idx_):
    temp_ = lst_p[idx_]
    if temp_ != idx_:
        temp_ = find(temp_)
        lst_p[idx_] = temp_
    return temp_


def union(idx_a, idx_b):
    p_a = find(idx_a)
    p_b = find(idx_b)
    lst_p[p_b] = p_a


for idx_a, idx_b, weight_ in lst_:
    union(idx_a, idx_b)
    if find(C_) == find(V_):
        print(weight_)
        break

exit()
